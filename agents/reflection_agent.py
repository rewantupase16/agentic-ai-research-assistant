class ReflectionAgent:
    def reflect(self, question, answer):
        if len(answer) < 20:
            return "Answer too short — likely incomplete."
        if "I don't know" in answer:
            return "Agent lacked sufficient knowledge."
        return "Response quality acceptable."
