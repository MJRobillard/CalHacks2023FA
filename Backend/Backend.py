import cv2
from skimage import metrics
import pytesseract
import requests
import os
import json



# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

API_URL = "https://api-inference.huggingface.co/models/microsoft/trocr-base-handwritten"
API_TOKEN = "HIDDEN"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

optionsImage = [] ##
optionsValue = []
actualOptions = []
dictionaryFileToValue = []

def sim(image1,image2) :
  image1 = cv2.imread("cropped_image2.jpg")
  image2 = cv2.imread("cropped_image4.jpg")
  image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]), interpolation = cv2.INTER_AREA)
  print(image1.shape, image2.shape)
  # Convert images to grayscale
  image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
  image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
  # Calculate SSIM
  ssim_score = metrics.structural_similarity(image1_gray, image2_gray, full=True)
  print(f"SSIM Score: ", round(ssim_score[0], 2))
  # SSIM Score: 0.38
  return ssim_score;

def is_string_convertible_to_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def extract_integer_from_json(json_response):
    temp = []
    for s in json_response: 
        if is_string_convertible_to_int(s):
            temp.append(s)
        
    return temp[-1]


def ocr_space_file(filename, overlay=False, api_key='helloworld', language='eng'):


    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def ocr_space_url(url, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with remote file.
        Python3.5 - not tested on 2.7
    :param url: Image url.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()



def ocr(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    print(str(response.text))
    return(extract_integer_from_json(str(response.text)))
        
ocr("cropped_image8.jpg")
  

current_directory = os.getcwd()

# Use examples:
options = []
for filename in os.listdir(current_directory):
    if "cropped" in filename:
        # If "cropped" is in the filename, add it to the options list
        options.append(filename)
    
        
split_point = len(options) // 2
options2 = options[split_point:]

options1= options[:split_point]


for file in options2:
  actualOptions.append(ocr(file))
  
  

print(actualOptions)
print(options2, "values")
dictionaryFileToValue = dict(zip(options2,actualOptions))
print(int(dictionaryFileToValue['cropped_image5.jpg']) + int(dictionaryFileToValue['cropped_image6.jpg'] ))
print(dictionaryFileToValue)