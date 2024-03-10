import requests
from PIL import Image, UnidentifiedImageError
from io import BytesIO
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException, ErrorCode

DetectorFactory.seed = 0 # To enforce consistent results

def is_single_pixel(image_url):
    try:
        response = requests.get(image_url)

        # Check if the request was successful and the content is an image
        if response.status_code == 200 and 'image' in response.headers.get('Content-Type', ''):
            img = Image.open(BytesIO(response.content))
            width, height = img.size
            return width == 1 and height == 1
        else:
            print(f"Error fetching image or non-image content at {image_url}")
            return False
    except UnidentifiedImageError:
        print(f"Cannot identify image file from {image_url}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def has_non_zero_entropy(ad):
    return ad.get('screenshot_entropy', 0) > 0



def generate_ad_url(ad):
    
    url_prefix = "http://ads3-d.adbl.io/static/img/" #TODO: ich kein Zugriff mehr an Bildern

    url_repo = ad.get("repository", "").split("adsdata/")[1] + "/"
    url_creative_name = ad.get("screenshot", "")
    ad_creative_url = url_prefix + url_repo + url_creative_name
    
    return ad_creative_url


def has_screenshot(entry):
    return bool(entry.get("screenshot"))

def remove_newlines(text):
    return text.replace('\n', ' ')


def german_text_detection(text):
   
    try:
        newText = remove_newlines(text)
        language = detect(newText)
        if(language == "de"):
            return True
    except LangDetectException as e:
        if e.code == ErrorCode.CantDetectError:
            print("Unable to detect language. Text might be too short or doesn't have recognizable features.\n")
            return False
        else:
            print(f"An error occurred: {e}\n")
            return False
    return False   

def is_text_making_sense(text):
    return True


def remove_duplicates(ads):
    unique_ads = set()
    return [unique_ads.add(ad['body_text']) or ad for ad in ads if ad.get('body_text', '') not in unique_ads]


