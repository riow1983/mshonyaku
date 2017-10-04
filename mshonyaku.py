from xml.etree import ElementTree
from auth import AzureAuthClient
import requests
import urllib.request

api_url = "https://api.microsofttranslator.com/V2/Http.svc/"
client_secret1 = "YOUR_SECRET_KEY1"
client_secret2 = "YOUR_SECRET_KEY2" # you can choose whichever you like
user = "YOUR_USER_NAME" # whatever you like
rating = 10 # You can choose between -10 to 10

def translate(textToTranslate=None, fromLangCode=None, toLangCode=None):
    auth_client = AzureAuthClient(client_secret1)
    bearer_token = 'Bearer ' + auth_client.get_access_token().decode('utf-8')
    finalToken = bearer_token
    headers = {"Authorization": finalToken}
    
    textToTranslate = urllib.request.quote(textToTranslate)
    translateUrl = api_url + "Translate?text={}&from={}&to={}".format(textToTranslate, fromLangCode, toLangCode)
    translationData = requests.get(translateUrl, headers=headers)
    translation = ElementTree.fromstring(translationData.text.encode('utf-8'))
    
    return translation.text


def add_translate(originalText=None, translatedText=None, fromLangCode=None, toLangCode=None, user=user, rating=rating):
    auth_client = AzureAuthClient(client_secret1)
    bearer_token = 'Bearer ' + auth_client.get_access_token().decode('utf-8')
    finalToken = bearer_token
    headers = {"Authorization": finalToken}
    
    originalText = urllib.request.quote(originalText)
    translatedText = urllib.request.quote(translatedText)
    addtranslateUrl = api_url + "AddTranslation?originalText={}&translatedText={}&from={}&to={}&user={}&rating={}".format(originalText, translatedText, fromLangCode, toLangCode, user, rating)
    
    addtranslationData = requests.get(addtranslateUrl, headers = headers)
    
    return addtranslationData