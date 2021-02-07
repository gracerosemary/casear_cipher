import nltk # natural language toolkit (poetry add nltk)
nltk.download('words', quiet=True)
from nltk.corpus import words
import string
word_list = words.words()
lower_alpha = string.ascii_lowercase
upper_alpha = string.ascii_uppercase

def encrypt(plain_text, key):
    """Takes in a plain text phrase and a numeric shift. The phrase will then be shifted that many letters. 

    Args:
        plain_text (str): text (word, phrase, sentence, etc)
        key (int): integer representing number of shifts needed

    Returns:
        str: returns new text after shifting 
    """
    encrypted_text = ''
    for char in plain_text:
        if char in lower_alpha:
            letter = lower_alpha[(lower_alpha.index(char) + key) % len(lower_alpha)]
            encrypted_text += letter
        elif char in upper_alpha:
            letter = upper_alpha[(upper_alpha.index(char) + key) % len(upper_alpha)]
            encrypted_text += letter
        else:
            encrypted_text += char 
    return encrypted_text

def decrypt(encoded, key):
    """Takes in encrypted text and numeric shift and restores the encrypted text back to original form. 

    Args:
        encoded (str): encoded text
        key (int): number of shifts needed

    Returns:
        str: original text (decoded)
    """
    return encrypt(encoded, -key)

def word_check(text):
    """Checks the text for English words and returns true if at least 80% of the words are found in the English language.

    Args:
        text (str): text

    Returns:
        bool: returns True if at least 80% words found are English 
    """
    count = 0
    words = text.split()
    for word in words:
        if word.lower() in word_list:
            count += 1
        # else:
        #     print("Word not found: ", word)
    percentage = (count / len(words)) * 100
    # print(percentage, "% English words found")
    # print("Number of words: ", count)
    if percentage > 80:
        return True
    else:
        return False

def crack(encoded):
    """Decodes the cipher so that an encrypted message can be transformed into its original state with no key access.

    Args:
        encoded (str): encoded string/text
    """

    for key in range(26):
        decoded = decrypt(encoded, key)
        check = word_check(decoded)
        if check is True:
            print("Key is", key)
            return decoded        

if __name__ == "__main__":
    # key = 2
    # plain = 'MoM'
    # encrypted = encrypt(plain, key)
    # decrypted = decrypt(plain, key)
    # print(encrypted)
    # print(decrypted)

    # check_word = 'kv ycu vjg dguv qh vkogu, kv ycu vjg yqtuv qh vkogu.'
    # print(crack(check_word))
    pass