# Evaluating Semantic Search over an Index of Online Banner Ads

The goal of this thesis is to evaluate the influence of semantic search technology on search engine, specifically focusing on online banner ads, and comparing its effectiveness to traditional keyword-based searches using Elasticsearch. Semantic search technology aims to understand the semantics, or meaning of queries and advertisement documents, allowing for searches based on the context and meaning of the queries.

## Technologies Used

We utilized a variety of technologies and models, including but not limited to:

- **NLP**: Sentence Transformers, Tokenization, Embedding, SpaCy, HuggingFace
- **Similarity Measures**: Cosine Similarity, FAISS Similarity, Euclidean Distance
- **Data Normalization and Preprocessing**: Custom normalization techniques for text data
- **Programming Languages and Tools**: Python, JSON for data handling

## Experiments Conducted

Our experiments were focused on comparing different algorithms and models to find the most effective approach for semantic search in our dataset. The main experiments included:

1. **Algorithm Comparison**: We compared the performance of cosine similarity, FAISS similarity, and Euclidean distance in identifying relevant ads.
2. **Model Effectiveness**: We evaluated the effectiveness of different NLP models, including a German Semantic Comparator, a Multi-Language Efficient Embedder in capturing semantic similarities.
3. **Impact of Data Normalization**: We assessed the impact of data preprocessing and normalization on the quality of search results.

## Achievements

Our experiments led to several key findings:

- German Semantic Comparator model significantly surpasses the performance of the MultiLang Efficient Embedder model.
- Data preprocessing techniques, such as stemming, removing stop words, and tok- enization, may contribute to the loss of semantic meaning.
- Cosine similarity offered a good accuracy for advertisment datasets.

## Conclusion

Our initial aim was to apply evaluation method based on semantic search over an index of online banner ads and evaluate it against various experiments to examine the impact of different criteria, such as data preprocessing, various SBERT models, different similarity metrics, and various features. The main idea was to use an SBERT model, trained on datasets for semantic similarity and clustering tasks, to feed it with features (inputs) to generate a vector (embedding). This embedding is then compared with the embedding of the query using a similarity algorithm to return the ads with the highest similarities.
Throughout this thesis, we observed how different experiments affected semantic search. We noted that data preprocessing techniques (such as tokenization, stemming, etc.) reduced the relevance of ads compared to experiments where no data preprocessing was applied. This suggests that data preprocessing can sometimes result in the loss of sentence meaning. Moreover, the choice of model was crucial, as it significantly impacted the ability to capture semantics. In some cases, the MultiLang Efficient Embedder struggled to process the semantics of the ads compared to the German Semantic Comparator, which was trained specifically on the German language and tasks like semantic search and clustering. It generates a more dimensional embedding with 1024 dimensions, whereas the MultiLang Efficient Embedder produces only a 768-dimensional embedding, which may not capture the full semantic meaning of the sentences as effectively.
Semantic search has enhanced the traditional keyword-matching search engine by retrieving more relevant ads, increasing accuracy by up to 10%, 90% depending on the threshold and query complexity.

## Reference to the Experiments used in this thesis

[Experiments List](./experiments/README.md)

## Getting Started

## Setting Up a Virtual Environment

Before installing the project dependencies, it's recommended to set up a virtual environment. This helps in avoiding conflicts with other Python projects by creating an isolated environment for this project's dependencies.

### Creating a Virtual Environment

Run the following command to create a virtual environment named `venv` within the project directory. You can replace `venv` with any name you prefer for your virtual environment.

- On macOS and Linux:

  ```
  python3 -m venv venv
  ```

- On Windows:

  ```
  python -m venv venv
  ```

### Activating the Virtual Environment

Once the virtual environment has been created, you need to activate it and switch to it.

- On macOS and Linux:

  ```
  source venv/bin/activate
  ```

- On Windows:

  ```
  .\venv\Scripts\activate
  ```

To get started with this project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt` in your terminal. This will set up your environment with the necessary libraries.

## Running the Project

To run a semantic search query using app.py, use the following command template in Python:

```python

query = "search query"
top_k = Number of top results
data_cleaning = True or False (based on whether to preprocess the data)
algorithm = cosine_similarity (or other algorithm to use)
model = chosen model (e.g., German_Semantic_Comparator)
features = List of features to consider in the search
reverse = True or False (based on the algorithm's sorting requirement)

```

Replace the placeholders with your specific details to perform a search. For a detailed explanation of each parameter and how to customize your search, refer to the source code documentation.

## Thesis as PDF
If you like to go through all the process in more details, here is the link [Evaluating Semantic over an Index of Online Banner Ads](https://github.com/rihabalyasiri/semantic_search_on_search_engine/blob/main/ba.pdf)
