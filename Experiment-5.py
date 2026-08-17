import numpy as np
import pandas as pd


class BooleanRetrieval:

    def __init__(self):
        self.index = {}
        self.documents_matrix = None

    def index_document(self, doc_id, text):
        terms = text.lower().split()

        for term in terms:
            if term not in self.index:
                self.index[term] = set()

            self.index[term].add(doc_id)

    def create_documents_matrix(self, documents):
        terms = list(self.index.keys())

        self.documents_matrix = np.zeros(
            (len(documents), len(terms)), dtype=int
        )

        for i, (doc_id, text) in enumerate(documents.items()):
            for term in text.lower().split():
                self.documents_matrix[i][terms.index(term)] = 1

    def print_documents_matrix_table(self):
        df = pd.DataFrame(
            self.documents_matrix,
            columns=self.index.keys()
        )
        print(df)

    def print_all_terms(self):
        print("All terms:")
        print(list(self.index.keys()))

    def boolean_search(self, query):
        words = query.lower().split()

        # Start with first word
        result = self.index.get(words[0], set())

        i = 1

        while i < len(words):

            operator = words[i]

            # AND NOT
            if operator == "and" and i + 2 < len(words) and words[i + 1] == "not":
                term = words[i + 2]
                result = result - self.index.get(term, set())
                i += 3

            # AND
            elif operator == "and":
                term = words[i + 1]
                result = result & self.index.get(term, set())
                i += 2

            # OR
            elif operator == "or":
                term = words[i + 1]
                result = result | self.index.get(term, set())
                i += 2

            else:
                i += 1

        return sorted(result)


if __name__ == "__main__":

    indexer = BooleanRetrieval()

    documents = {
        1: "Python is a programming language",
        2: "Information retrieval deals with finding information",
        3: "Boolean models are used in information retrieval"
    }

    for doc_id, text in documents.items():
        indexer.index_document(doc_id, text)

    indexer.create_documents_matrix(documents)

    indexer.print_documents_matrix_table()
    indexer.print_all_terms()

    query = input("Enter your boolean query: ")

    results = indexer.boolean_search(query)

    if results:
        print("Results:", results)
    else:
        print("No results found.")