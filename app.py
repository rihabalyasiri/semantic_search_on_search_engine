import similarities.cosine_similarity as cosine_similarity
import similarities.faiss_similarity as faiss_similarity
import similarities.euclidean_distance as euclidean_distance
from normalizing import normalizing
import json
from models.German_Semantic_Comparator import model_nli as German_Semantic_Comparator
from models.MultiLang_Efficient_Embedder import model_nli as MultiLang_Efficient_Embedder
from models.distilBERT_model import model as DestilBERT_model


filename = 'data/ground_truth.json'

with open(filename, 'r') as file:
    ground_truth = json.load(file)
    

def search_similar_entries(query, data, top_k, data_cleaning, algorithem, model, features, reverse):

    # Store similarities and corresponding entries
    similarities = []
    
    # checking the data cleaning (normalizing) if applied or not
    if data_cleaning:
        query_normalized = normalizing(query)
        query_vector = model.encode(query_normalized)
    else:
        query_vector = model.encode(query)


    # loop through all the data in Ground Truth
    for ad in data:
        sentence = extract_features_text(features, ad)

        # checking the data cleaning (normalizing) if applied or not
        if data_cleaning:
            sentence_normalizing = normalizing(sentence)
            sentence_vector = model.encode(sentence_normalizing)
        else:
            sentence_vector = model.encode(sentence)


        similarity = algorithem.calculate_similarity(sentence_vector, query_vector)
        similarities.append((similarity, ad))
    
    
    # Sort the entries based on similarity and return the top k entries
    sorted_entries = sorted(similarities, key=lambda x: x[0], reverse=reverse)[:top_k]       
         
    
    return [{'similarity': similarity, **ad} for similarity, ad in sorted_entries]


def extract_features_text(features, ad):
    sentence = "" 

    for feature in features:
        if feature == "body_text":
            sentence = ad[feature]
        elif feature == "frame_hrefs_parsed":
            if feature in ad and isinstance(ad[feature], list):
                concatenated_domains = ' '.join(item['advertiser.domain_name'] for item in ad[feature] if 'advertiser.domain_name' in item)
                sentence= sentence + " " + concatenated_domains
        elif feature == "image_caption_de":
            sentence= sentence + " " + ad[feature]
        elif feature == "predicted_text":
            sentence= sentence + " " + ad[feature]
        
        elif feature == "combined_description":
            sentence = sentence + " " + ad[feature]
        else:
            concatenated_keywords = ' '.join(item for item in ad[feature])
            sentence= sentence + " " + concatenated_keywords
    return sentence





# Testing Queries:
# 1. Wein kaufen
# 2. günstiger Mobilfunktarif
# 3. Kredit mit niedrigen Zinsen
# 4. Schnäppchen Flüge

# Folders of Queries:
# 1. wein_kaufen
# 2. schnaeppchen_fluege
# 3. guenstiger_mobilfunktarif
"""
    :param query -> it is string as a sentence for searching
    :param data -> list of dictonieres that contains all the needed features of Ad (Ground Truth)
    :param top_k -> number of the top results (10, 25)
    :param data_cleaning -> True = mit normalizing, False = ohne normalizing
    :param algorithem = cosine_similarity or faiss_similarity or euclidean_distance
    :param model =  German_Semantic_Comparator , MultiLang_Efficient_Embedder , DestilBERT_model
    :param features -> list of strings of all the keys of features = ["body_text","frame_hrefs_parsed", "image_caption_de", 
                                                                        "keywords", "combined_description" ]
    :param reverse=True means sort from highest to lowest
        # Cosine Algorithm -> reverse = True (because the highest values toward 1 the more similar)
        # Faiss Algorithm -> reverse = False (beacuse the lowest values in distance the more similar)
        # Euclidean Distance Algorithm -> reverse = False (beacuse the lowest values in distance the more similar)
"""
query = "Wein kaufen"
query_folder = "wein_kaufen"

#TODO: here they should be changed every experiment
experiment_number = "Experiment_37"
data_cleaning=False
model=German_Semantic_Comparator
algorithem=cosine_similarity
reverse=True
features =["body_text","frame_hrefs_parsed", "image_caption_de", "keywords", "combined_description"]
k = 25


top_results = search_similar_entries(query=query,data=ground_truth, top_k=k, data_cleaning=data_cleaning,
                                    algorithem=algorithem, model=model,
                                    features =features, reverse=reverse)

with open(f"results/{query_folder}/top_{k}/{experiment_number}.json", 'w') as file:
    json.dump(top_results, file, indent=4)

