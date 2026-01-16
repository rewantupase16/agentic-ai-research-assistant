import time
import json

class EvaluationLogger:
    def __init__(self, path="evaluation/logs.json"):
        self.path = path

    def log(self, question, answer, reflection):
        record = {
            "question": question,
            "answer": answer,
            "reflection": reflection,
            "timestamp": time.time()
        }

        try:
            with open(self.path, "r") as f:
                data = json.load(f)
        except:
            data = []

        data.append(record)

        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)
