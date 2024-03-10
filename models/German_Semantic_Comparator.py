from sentence_transformers import SentenceTransformer, models




word_embedding_model = models.Transformer("aari1995/German_Semantic_STS_V2")
pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())
model_nli = SentenceTransformer(modules=[word_embedding_model, pooling_model])



