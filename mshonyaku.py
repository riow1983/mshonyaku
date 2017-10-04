from xml.etree import ElementTree
from auth import AzureAuthClient
import requests
import urllib.request

api_url = "https://api.microsofttranslator.com/V2/Http.svc/"
client_secret1 = "319660f0d6164c5fb8f91e2cb54101f5"
client_secret2 = "489da5a7b84a40cba92c75fdeaf3af01"
user = "riow1983"
rating = 10

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