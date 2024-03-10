# Load model directly
from transformers import BlipProcessor, BlipForConditionalGeneration

# this model gives image captioning in English still need to be translated to German to concat with the other features
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")