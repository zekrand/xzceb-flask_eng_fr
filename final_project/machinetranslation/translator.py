"""
IBM Watson Translator Final project
Using python for calling watson translator API, perform unit tests
and flask server for servring translator functions.
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
#Define variables for use with watson translatior
apikey = os.environ['apikey']
url = os.environ['url']

"""
Construct instance of watson translator as language_translator
Set service url for us-east
"""
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url(url)

def english_to_french(english_text):
    ''' Input: English text into the function as string
        Output: Translated text from english to french
                Using watson translator.
    '''
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()
    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    ''' Input: French text into the function as string
        Output: Translated text from french to english
                Using watson translator.
    '''
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()
    return english_text['translations'][0]['translation']
