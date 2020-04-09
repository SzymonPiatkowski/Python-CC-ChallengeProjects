# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
import re

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


def censor_phrase(email, word_or_phrase):
    email = re.sub(r'\b' + word_or_phrase + r'\b',
                    "█" * len(word_or_phrase), email)
    email = re.sub(r'\b' + word_or_phrase.capitalize() +
                    r'\b', "█" * len(word_or_phrase), email)
    email = re.sub(r'\b' + word_or_phrase.title() + r'\b',
                    "█" * len(word_or_phrase), email)
    email = re.sub(r'\b' + word_or_phrase.upper() + r'\b',
                    "█" * len(word_or_phrase), email)
    email = re.sub(r'\b' + word_or_phrase.lower() + r'\b',
                    "█" * len(word_or_phrase), email)
    return email

# print(censor_phrase(email_one, "learning algorithms"))


def censor_proprietary_terms(email):
    proprietary_terms = ["she", "personality matrix", "sense of self",
                        "self-preservation", "learning algorithm", "her", "herself"]
    for term in proprietary_terms:
        email = censor_phrase(email, term)
    return email

# print(censor_proprietary_terms(email_two))


def censor_negative_words(email):
    negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset",
                        "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
    if sum(email.count(word) for word in negative_words) > 1:
        for word in negative_words:
            email = censor_phrase(email, word)
    email = censor_proprietary_terms(email)
    return email

# print(censor_negative_words(email_three))


def censor_all(email):
    email = censor_negative_words(email)
    email_list = email.split("\n")
    new_email_list = []
    for paragraph in email_list:
        paragraph_list = paragraph.split()
        new_paragraph_list = []
        for index, word in enumerate(paragraph_list):
            # If there is already a value in the new list, which is a censored one, we skip it:
            try:
                if new_paragraph_list[index]:
                    continue
            except:
                new_paragraph_list.append(word)
            # We check if the word is censored or not:
            if "█" in word and index < len(paragraph_list):
                if index == len(paragraph_list) - 1:
                    pass
                # We check if the next word ends wiht or without punctuation, and censor it accordingly.
                elif paragraph_list[index + 1][-1].isalnum():
                    new_paragraph_list.append(len(paragraph_list[index + 1]) * "█")
                else:
                    new_paragraph_list.append(((len(paragraph_list[index + 1]) - 1) * "█") + paragraph_list[index + 1][-1])
                # We check if the previous word ends wiht or without punctuation, and censor it accordingly.
                print(index)
                if index == 0:
                    continue
                elif paragraph_list[index - 1][-1].isalnum():
                    new_paragraph_list[index - 1] = (len(paragraph_list[index - 1]) * "█")
                else: 
                    new_paragraph_list[index - 1] = ((len(paragraph_list[index - 1]) - 1) * "█") + paragraph_list[index - 1][-1]
        new_paragraph = " ".join(new_paragraph_list)         
        new_email_list.append(new_paragraph)
    return "\n".join(new_email_list)
    
print(censor_all(email_four))
