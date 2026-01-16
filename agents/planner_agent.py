class PlannerAgent:
    def decide(self, query):
        q = query.lower()

        if any(w in query.lower() for w in ["pdf", "export", "download"]):
            return ["retrieve", "synthesize"]

        if q.startswith("research:"):
            return ["research"]

        if q.startswith("goal:"):
            return ["autonomous"]

        if any(w in q for w in ["latest", "current", "today", "news"]):
            return ["tool", "synthesize"]
        
        if any(w in q for w in ["pdf", "export", "download", "report"]):
            return ["retrieve", "synthesize", "tool"]

        if any(w in q for w in ["summarize", "explain", "overview"]):
            return ["retrieve", "synthesize"]

        if any(w in q for w in ["remember", "recall", "my name"]):
            return ["memory", "synthesize"]

        return ["retrieve", "memory", "synthesize"]

