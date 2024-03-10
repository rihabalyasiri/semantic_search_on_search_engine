import preprocessing 
from models.extract_text_from_image_model import generate_text_from_image 


# preprocessing the data
# 1. German Language Detection
# 2. Higher screenshot_entropy values
# 3. Generate image URL for each element
# 4. interpretate the meaning of images (predicted text)
# 5. correct the words of the predicted text that comes from the model
# 6. keeps just the sentence that make sense from the predicted text
# 7. delete all duplicate data that has same text

#TODO: filtern nach die dataframe (call_to_action == 1) bedeutet 
# enthalten call_to_action wörter müssen auch entfernt (weiß nicht was von wörter muss vorher analysieren)


def filtering(ads):
    filtered_data = []
    unique_ads = preprocessing.remove_duplicates(ads)
 

    for ad in unique_ads:

        isGerman_body_text = preprocessing.german_text_detection(ad["body_text"])
        hasNonZeroEntropy = preprocessing.has_non_zero_entropy(ad)
        generated_url = preprocessing.generate_ad_url(ad)
        ad["ad_creative_url"] = generated_url # change the data and add on it ad_creative_url
        #isSinglePixel = preprocessing.is_single_pixel(generated_url)

        #if isGerman_body_text and hasNonZeroEntropy and isSinglePixel != True:
           
            #predicted_text = generate_text_from_image(generated_url)
            #entry["predicted_text"] = predicted_text # change the data add on ot predicted_text
            #isGerman_predicted_text = preprocessing.german_text_detection(entry.get("predicted_text", ""))
            #print(f"{i}: {predicted_text}")

        
        hasScreenshot = preprocessing.has_screenshot(ad)
       
        if (isGerman_body_text == True) and hasScreenshot and hasNonZeroEntropy:
            filtered_data.append(ad)
    
    return filtered_data