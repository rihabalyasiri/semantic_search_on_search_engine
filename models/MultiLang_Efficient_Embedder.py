from sentence_transformers import SentenceTransformer, models




word_embedding_model = models.Transformer('sentence-transformers/paraphrase-multilingual-mpnet-base-v2')
pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())
model_nli = SentenceTransformer(modules=[word_embedding_model, pooling_model])


