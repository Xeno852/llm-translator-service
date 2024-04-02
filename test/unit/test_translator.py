from mock import patch
from src.translator import translate_content


@patch('src.translator.get_language')
@patch('src.translator.get_translation')
def test_chinese(mock_get_translation, mock_get_language):
    mock_get_language.return_value = "Chinese"
    mock_get_translation.return_value = "This is a Chinese message"
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message"

@patch('src.translator.get_language')
@patch('src.translator.get_translation')
def test_french(mock_get_translation, mock_get_language):
    mock_get_language.return_value = "French"
    mock_get_translation.return_value = "This is a French message"
    is_english, translated_content = translate_content("Ceci est un message en français")
    assert is_english == False
    assert translated_content == "This is a French message"

@patch('src.translator.get_language')
@patch('src.translator.get_translation')
def test_english(mock_get_translation, mock_get_language):
    mock_get_language.return_value = "English"
    mock_get_translation.return_value = "This is an English message"
    is_english, translated_content = translate_content("This is an English message")
    assert is_english == True
    assert translated_content == "This is an English message"

@patch('src.translator.get_language')
@patch('src.translator.get_translation')
def test_spanish(mock_get_translation, mock_get_language):
    mock_get_language.return_value = "Spanish"
    mock_get_translation.return_value = "This is a Spanish message"
    is_english, translated_content = translate_content("Esta es un mensaje en español")
    assert is_english == False
    assert translated_content == "This is a Spanish message"

def test_llm_gibberish_response():
    pass

def test_llm_normal_response():
    pass

