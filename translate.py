from langchain_helper import get_qa_chain  
from googletrans import Translator
from format import format_paragraph

translator = Translator()
chain = get_qa_chain()

def translate(user_message):
    query = user_message
    result = translator.detect(query)
    lang = result.lang
    if(lang != 'en'):
        translatedlang = translator.translate(query)
        user_message = translatedlang.text
    bot_response = chain(user_message) 
    response = bot_response['result']
    response = format_paragraph(response)
    if(lang != 'en'):
        translation = translator.translate(response, dest=result.lang)
        response = translation.text
    return response