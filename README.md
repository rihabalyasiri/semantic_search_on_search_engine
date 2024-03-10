# Evaluating Semantic Search over an Index of Online Banner Ads

This thesis explores the application of semantic search within the domain of online advertising. By leveraging advanced natural language processing (NLP) techniques, we aim to enhance the precision and relevance of search results in this field.


## Technologies Used

We utilized a variety of technologies and models, including but not limited to:

- **NLP Models and Libraries**: DistilBERT, Sentence Transformers
- **Similarity Measures**: Cosine Similarity, FAISS Similarity, Euclidean Distance
- **Data Normalization and Preprocessing**: Custom normalization techniques for text data
- **Programming Languages and Tools**: Python, JSON for data handling

## Experiments Conducted

Our experiments were focused on comparing different algorithms and models to find the most effective approach for semantic search in our dataset. The main experiments included:

1. **Algorithm Comparison**: We compared the performance of cosine similarity, FAISS similarity, and Euclidean distance in identifying relevant ads.
2. **Model Effectiveness**: We evaluated the effectiveness of different NLP models, including a German Semantic Comparator, a Multi-Language Efficient Embedder, and DistilBERT, in capturing semantic similarities.
3. **Impact of Data Normalization**: We assessed the impact of data preprocessing and normalization on the quality of search results.

## Achievements

Our experiments led to several key findings:

- The German Semantic Comparator model, combined with cosine similarity, provided the most relevant search results for queries related to German-language ads.
- Data normalization did not improved the accuracy of semantic search by standardizing the input data.
- Cosine similarity offered a good accuracy for advertisment datasets.


## Conclusion

This thesis presents a comprehensive analysis of semantic search technologies in the context of online advertising. Through our experiments, we've demonstrated the potential of NLP and similarity algorithms in improving ad relevance and user experience. Our findings contribute valuable insights into the field of semantic search, offering a foundation for future research and development.

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
