# pip install --quiet google-cloud-aiplatform
from vertexai.language_models import ChatModel, InputOutputTextPair




from typing import Callable
# def translate_content(content: str) -> tuple[bool, str]:
#     if content == "这是一条中文消息":
#         return False, "This is a Chinese message"
#     if content == "Ceci est un message en français":
#         return False, "This is a French message"
#     if content == "Esta es un mensaje en español":
#         return False, "This is a Spanish message"
#     if content == "Esta é uma mensagem em português":
#         return False, "This is a Portuguese message"
#     if content  == "これは日本語のメッセージです":
#         return False, "This is a Japanese message"
#     if content == "이것은 한국어 메시지입니다":
#         return False, "This is a Korean message"
#     if content == "Dies ist eine Nachricht auf Deutsch":
#         return False, "This is a German message"
#     if content == "Questo è un messaggio in italiano":
#         return False, "This is an Italian message"
#     if content == "Это сообщение на русском":
#         return False, "This is a Russian message"
#     if content == "هذه رسالة باللغة العربية":
#         return False, "This is an Arabic message"
#     if content == "यह हिंदी में संदेश है":
#         return False, "This is a Hindi message"
#     if content == "นี่คือข้อความภาษาไทย":
#         return False, "This is a Thai message"
#     if content == "Bu bir Türkçe mesajdır":
#         return False, "This is a Turkish message"
#     if content == "Đây là một tin nhắn bằng tiếng Việt":
#         return False, "This is a Vietnamese message"
#     if content == "Esto es un mensaje en catalán":
#         return False, "This is a Catalan message"
#     if content == "This is an English message":
#         return True, "This is an English message"
#     return True, content


# Below is unnessary for this current checkpoint (CP2), however should be used for the final checkpoint (CP3):
"""
# from vertexai.language_models import ChatModel, InputOutputTextPair

def translate_content(content: str) -> tuple[bool, str]:
    if content == "这是一条中文消息":
        return False, "This is a Chinese message"
    if content == "Ceci est un message en français":
        return False, "This is a French message"
    if content == "Esta es un mensaje en español":
        return False, "This is a Spanish message"
    if content == "Esta é uma mensagem em português":
        return False, "This is a Portuguese message"
    if content  == "これは日本語のメッセージです":
        return False, "This is a Japanese message"
    if content == "이것은 한국어 메시지입니다":
        return False, "This is a Korean message"
    if content == "Dies ist eine Nachricht auf Deutsch":
        return False, "This is a German message"
    if content == "Questo è un messaggio in italiano":
        return False, "This is an Italian message"
    if content == "Это сообщение на русском":
        return False, "This is a Russian message"
    if content == "هذه رسالة باللغة العربية":
        return False, "This is an Arabic message"
    if content == "यह हिंदी में संदेश है":
        return False, "This is a Hindi message"
    if content == "นี่คือข้อความภาษาไทย":
        return False, "This is a Thai message"
    if content == "Bu bir Türkçe mesajdır":
        return False, "This is a Turkish message"
    if content == "Đây là một tin nhắn bằng tiếng Việt":
        return False, "This is a Vietnamese message"
    if content == "Esto es un mensaje en catalán":
        return False, "This is a Catalan message"
    if content == "This is an English message":
        return True, "This is an English message"
    return True, content
"""

# Below is unnessary for this current checkpoint (CP2), however should be used for the final checkpoint (CP3):
# """
def get_translation(post: str) -> str:
    # Initialize the ChatModel with the specific model identifier
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    # Define a context or prompt modification to guide the model towards translation.
    # This might need to be adjusted based on the model's training and expected input format.
    trans_context = "Translate the following text to English with the highest semantic meaning. The response you give following this should ONLY include the traslated text.:"
    """
    Translates non-English posts into English using the Vertex AI 'chat-bison' model.

    Args:
        post (str): The text to be translated.

    Returns:
        str: The translated text.
    """
    # Parameters for controlling the model's behavior
    parameters = {
        "temperature": 0.7,
        "max_output_tokens": 256,
    }

    # Initialize a chat session with the provided context
    # chat = chat_model.start_chat(context=trans_context)

    # Send the post to the model for translation
    # response = chat.send_message(post, **parameters)
    response = "MOCK"
    # print("CALLED")
    # print(f"RESPONSE HERE IS {response.text}")

    # Return the model's response text, which should be the translation
    return response.text

def get_language(post: str) -> str:
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    language_ident_context = "Identify the language of the following text. Answer only in the language. Say the languages in their English version. For example say \"Spanish\", not \"This is Spanish\". For examples such as brazilian portuguese vs european portuguese, just flatten it to only be Portuguese. Also include no punctionation, only the language name in english:"
    """
    Identifies the language of the given text using the Vertex AI 'chat-bison' model.

    Args:
        post (str): The text whose language is to be identified.

    Returns:
        str: The identified language.
    """
    # Parameters for controlling the model's behavior
    parameters = {
        "temperature": 0.7,
        "max_output_tokens": 256,
    }

    # Initialize a chat session with the provided context
    chat = chat_model.start_chat(context=language_ident_context)

    # Send the post to the model for language identification
    response = chat.send_message(post, **parameters)
    # response = "MOCK"

    # Return the model's response text, which should be the language identification
    return response.text


def query_llm(post: str) -> tuple[bool, str]:
    """
    Simulates querying a language model (LLM) to determine if a post is in English and,
    if not, to translate it into English.

    Args:
        post (str): The post to be analyzed and potentially translated.

    Returns:
        tuple[bool, str]: A tuple containing a boolean indicating whether the post is in English
                          and the original post or its English translation.
    """
    # Placeholder for LLM's language detection (simulated)
    if (get_language(post).lower == "english"):
        return (True, post)
        # return (True, post)
    else:

      translation = get_translation(post) 

      # return (False, translation)
      return (False, translation)
    return "Translation not avalible"

def translate_content(content: str) -> tuple[bool, str]:
    return query_llm(content)

# """
