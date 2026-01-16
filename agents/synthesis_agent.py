from groq import Groq
from config import GROQ_API_KEY


class SynthesisAgent:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
        self.model = self._select_working_model()

    def _select_working_model(self):
        models = self.client.models.list().data
        for m in models:
            name = m.id.lower()
            if any(k in name for k in ["instruct", "chat", "llama", "mixtral"]):
                return m.id
        return models[0].id

    def generate(self, context, query):
        """
        Generates clean, IEEE-style academic text suitable for PDF export.
        Includes safety sanitization and fallback logic.
        """

        system_message = """
You are AURA, an academic research-writing assistant embedded in a software system.

Guidelines:
- Write formal, neutral, academic content.
- Avoid sensitive, harmful, or policy-restricted material.
- If content cannot be generated safely, provide a high-level academic overview.
- NEVER output safety labels, moderation tags, or internal codes.
- NEVER mention model limitations.
"""

        user_message = f"""
Write a formal IEEE-style research paper.

MANDATORY STRUCTURE:
Title
Abstract
Keywords
1. Introduction
2. Background / Related Work
3. Methodology
4. Results and Discussion
5. Conclusion
References

RULES:
- Use formal academic tone.
- Abstract must be a single concise paragraph.
- Section headers must be explicit.
- Use citation placeholders like [1], [2], [Doc1], [Web1].
- Do NOT fabricate detailed references.
- Do NOT use markdown, bullet points, or emojis.
- Write clean paragraphs suitable for PDF generation.

CONTEXT:
{context}

TASK:
{query}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            temperature=0.1,
            max_tokens=900
        )

        output = response.choices[0].message.content.strip()

        # ---------- SAFETY SANITIZATION ----------
        blocked_markers = [
            "unsafe",
            "s1",
            "s2",
            "policy",
            "violation",
            "moderation"
        ]

        if (
            len(output) < 100
            or any(marker in output.lower() for marker in blocked_markers)
        ):
            return self._safe_fallback(query)

        return output

    def _safe_fallback(self, query):
        """
        Guaranteed-safe academic fallback to prevent PDF corruption.
        """
        return f"""
Title

An Academic Overview of {query}

Abstract

This paper presents a high-level academic overview of the selected topic, focusing on established concepts, methodologies, and research directions. The discussion is intentionally neutral and avoids sensitive or restricted content while maintaining scholarly rigor.

Keywords

Artificial Intelligence, Research Systems, Agentic AI, Academic Writing

1. Introduction

The topic under study has received increasing attention within the academic and research community due to its theoretical and practical relevance.

2. Background and Related Work

Prior research has explored foundational principles and applications related to this domain, forming the basis for continued investigation.

3. Methodology

This work adopts a conceptual and literature-driven methodology, synthesizing existing knowledge into a structured academic narrative.

4. Results and Discussion

The analysis highlights key insights and implications from a systems and research perspective, emphasizing academic understanding rather than empirical claims.

5. Conclusion

The paper concludes by summarizing the discussion and outlining potential directions for future research.

References

[1] Placeholder academic reference.
"""

