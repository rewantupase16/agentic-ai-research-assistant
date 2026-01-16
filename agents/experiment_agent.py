class ExperimentAgent:
    def generate_experiments(self, topic):
        return f"""
Experiments and Evaluation:
We evaluate the system on multi-turn reasoning, factual accuracy, latency, hallucination rate, and memory retention for the topic: {topic}. Performance metrics include response quality and retrieval effectiveness.
"""
