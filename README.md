### EX5 Information Retrieval Using Boolean Model in Python
### DATE: 17 - 08 - 2026
### AIM: To implement Information Retrieval Using Boolean Model in Python.
### Description:
<div align = "justify">
The Boolean model in Information Retrieval (IR) is a fundamental model used for searching and retrieving information from a collection of documents. It operates on the principles of set theory and logic, where documents are represented as sets of terms or words, and queries are expressed as Boolean expressions using logical operators such as AND, OR, and NOT.
  
### Procedure:
1. ***Initialize the BooleanRetrieval class:*** The BooleanRetrieval class is defined to manage the indexing and searching of documents.
2. ***Constructor and Index Initialization:*** The class constructor initializes an empty index to store the inverted index mapping terms to documents.
3. ***Indexing Documents:***
    <p> a) The index_document method is responsible for indexing documents.
    <p> b) Tokenize the text content of documents, converting them into lowercase terms.
    <p> c) For each term in the document, it adds an entry in the index, associating the term with the document ID. </p>
4. ***Fetch Web Page Text:***
    <p>a) The fetch_webpage_text method uses the requests library to fetch content from a given URL.
    <p>b) Extract text content from the fetched HTML using BeautifulSoup.
    <p>c) The extracted text is returned for further processing.
5. ***Boolean Search:***
    <p>a) The boolean_search method performs Boolean searches on the indexed documents.
    <p>b) Tokenize the input query and iterates through its terms.
    <p>c) For each term in the query, it retrieves documents containing that term and performs Boolean operations (AND, OR, NOT) based on the query's structure.

### Program:

```python
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
```

### Output:

### AND:
<img width="886" height="170" alt="{FB49B8A3-EB8D-401C-8CE9-11CA7C3C681A}" src="https://github.com/user-attachments/assets/e8a59ea1-ae3f-4177-9fdc-36beb92ef0f0" />


### OR:
<img width="882" height="166" alt="{EEB448DD-88CC-49F7-BA01-7D0EC084F6AB}" src="https://github.com/user-attachments/assets/822b1e9d-cea1-4c1f-aa80-985062b6772d" />

### NOT:
<img width="888" height="168" alt="{3932146A-AA2E-411E-B6D6-3E3BBBFC5C98}" src="https://github.com/user-attachments/assets/6a98c44a-36e0-40b1-9a19-65a87e543487" />


### Result:
Thus, the Information Retrieval system using the Boolean Model was successfully implemented in Python. The program successfully created an inverted index and document-term matrix and retrieved the relevant documents based on AND, OR, and NOT Boolean operations.
