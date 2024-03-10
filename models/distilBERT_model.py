from transformers import DistilBertTokenizer, DistilBertModel
import torch

class CustomDistilBertModel(DistilBertModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tokenizer = DistilBertTokenizer.from_pretrained("sentence-transformers/nq-distilbert-base-v1")

    def encode(self, sentence):
        # Tokenize the sentence
        inputs = self.tokenizer(sentence, return_tensors="pt", truncation=True, padding=True, max_length=512)

        # Get the embeddings
        with torch.no_grad():
            embeddings = self(**inputs).last_hidden_state

        # Average embeddings to get the sentence vector (simple pooling)
        sentence_vector = embeddings.mean(dim=1)

        return sentence_vector

# Instantiate the model
model = CustomDistilBertModel.from_pretrained("sentence-transformers/nq-distilbert-base-v1")



