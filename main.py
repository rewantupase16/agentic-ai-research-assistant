from agents.planner_agent import PlannerAgent
from agents.retrieval_agent import RetrievalAgent
from agents.memory_agent import MemoryAgent
from agents.synthesis_agent import SynthesisAgent
from agents.reflection_agent import ReflectionAgent
from agents.autonomous_agent import AutonomousAgent
from agents.research_agent import ResearchAgent
from agents.experiment_agent import ExperimentAgent
from agents.tool_agent import ToolAgent

from memory.vector_store import VectorStore
from evaluation.logger import EvaluationLogger
from tools.pdf_exporter import export_pdf


# ---------- Initialize Agents ----------
planner = PlannerAgent()
store = VectorStore()
retriever = RetrievalAgent(store)
memory = MemoryAgent()
synthesizer = SynthesisAgent()
reflector = ReflectionAgent()
autonomous = AutonomousAgent()
researcher = ResearchAgent()
experimenter = ExperimentAgent()
tool = ToolAgent()
logger = EvaluationLogger()


# ---------- Core Agent Engine ----------
def run_agent(query):
    memory.remember("User", query)

    plan = planner.decide(query)

    # ---------- PDF Export Intent ----------
    if any(word in query.lower() for word in ["pdf", "export", "download", "save as"]):
        docs = retriever.retrieve(query)
        knowledge = "\n".join([d.page_content for d in docs])

        context = f"""
    Retrieved Knowledge:
    {knowledge}
    """

        report = synthesizer.generate(
            context,
            "Write a clean, well-structured research report suitable for PDF export."
        )

        export_pdf(report)
        memory.remember("AURA", report)

        return "PDF generated successfully as research_report.pdf"


    # ---------- Research Mode ----------
    if "research" in plan:
        topic = query.replace("research:", "").strip()

        outline = researcher.build_outline(topic)
        docs = retriever.retrieve(topic)
        tool_data = tool.web_search(topic)

        knowledge = "\n".join([d.page_content for d in docs])

        context = f"""
Research Topic:
{topic}

Retrieved Documents:
{knowledge}

Web Data:
{tool_data}
"""

        experiments = experimenter.generate_experiments(topic)
        context += experiments

        report = synthesizer.generate(
            context,
            f"Write a full research report with these sections: {outline}"
        )

        export_pdf(report)
        memory.remember("AURA", report)
        return report

    # ---------- Autonomous Mode ----------
    if "autonomous" in plan:
        goal = query.replace("goal:", "").strip()
        steps = autonomous.create_plan(goal)

        output = f"### 🎯 Goal\n{goal}\n\n### 🧭 Plan\n"
        for i, step in enumerate(steps, 1):
            output += f"{i}. {step}\n"

        memory.remember("AURA", output)
        return output

    # ---------- Standard Agent Mode ----------
    docs, tool_data = [], ""

    if "retrieve" in plan:
        docs = retriever.retrieve(query)

    if "tool" in plan:
        tool_data = tool.web_search(query)


    knowledge = "\n".join([d.page_content for d in docs])
    history = memory.recall()

    context = f"""
Conversation History:
{history}

Retrieved Knowledge:
{knowledge}

Tool Output:
{tool_data}
"""

    answer = synthesizer.generate(context, query)

    memory.remember("AURA", answer)

    reflection = reflector.reflect(query, answer)
    logger.log(query, answer, reflection)

    return answer
