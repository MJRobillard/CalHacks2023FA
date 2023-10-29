import cv2
from skimage import metrics
import pytesseract
import requests


# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'




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



def ocrPlease(file):
   return ocr_space_file(filename=file, api_key= "K87442248088957")

# Use examples:
