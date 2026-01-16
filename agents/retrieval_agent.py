class RetrievalAgent:
    def __init__(self, store):
        self.store = store

    def retrieve(self, query):
        return self.store.search(query)
