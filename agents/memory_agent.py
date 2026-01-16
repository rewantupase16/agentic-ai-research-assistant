import json
import os

class MemoryAgent:
    def __init__(self, path="memory.json"):
        self.path = path
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                self.history = json.load(f)
        else:
            self.history = []

    def remember(self, role, message):
        self.history.append({"role": role, "message": message})
        with open(self.path, "w") as f:
            json.dump(self.history, f, indent=2)

    def recall(self, k=6):
        recent = self.history[-k:]
        return "\n".join([f"{m['role']}: {m['message']}" for m in recent])
