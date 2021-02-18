"""
This Python File
"""

import re
import math

STOP_WORDS = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you",
              "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself",
              "she", "her", "hers", "herself", "it", "its", "itself", "they", "them",
              "their", "theirs", "themselves", "what", "which", "who", "whom", "this",
              "that", "these", "those", "am", "is", "are", "was", "were", "be", "been",
              "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a",
              "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "through", "during", "before", "after",
              "above", "below", "to", "from", "up", "down", "in", "out", "on", "off",
              "over", "under", "again", "further", "then", "once", "here", "there",
              "when", "where", "why", "how", "all", "any", "both", "each", "few",
              "more", "most", "other", "some", "such", "no", "nor", "not", "only",
              "own", "same", "so", "than", "too", "very", "can", "will"]

CONTRACTION_MAPPING = {"you'll": "you will", "don't": "do not", "we'll": "we will"}

SAMPLE_TXT_ONE = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already " \
                 "love. If you have any participating brands on your receipt, you'll get points based on the cost of " \
                 "the products. You don't need to clip any coupons or scan individual barcodes. Just scan each " \
                 "grocery receipt after you shop and we'll find the savings for you. "

SAMPLE_TXT_TWO = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If " \
                 "you have any eligible brands on your receipt, you will get points based on the total cost of the " \
                 "products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt " \
                 "after you check out and we will find the savings for you. "

SAMPLE_TXT_THREE = "We are always looking for opportunities for you to earn more points, which is why we also give " \
                   "you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on " \
                   "top of the regular points you earn every time you purchase a participating brand. No need to " \
                   "pre-select these offers, we'll give you the points whether or not you knew about the offer. We " \
                   "just think it is easier that way. "


# The first step is to clean the text

# Remove all leading and trailing whitespaces - when people copy and past white spaces can happen
def strip_document(txt):
    """Returns string after removing leading and trailing spaces
    :param txt: String to clean
    :return: String
    """
    txt = txt.strip()
    return txt


# Convert all the text to lowercase
def lower_case(txt):
    txt = txt.lower()
    return txt


# Replace all the Contractions in the Document
def replace_contraction(txt):
    for contraction, full in CONTRACTION_MAPPING.items():
        txt = txt.replace(contraction, full)
    return txt


# Only Keep alphanumeric characters - we are going to use regular expressions to do this
def keep_alphanum(txt):
    """
    Removes all non alphanumeric characters will return the txt as a list
    :param txt: string
    :return: list
    """
    pattern = re.compile("\w+")
    list_txt = pattern.findall(txt)
    return list_txt


# Remove all Stop words - they don't have significance for us
def remove_stop_words(list_words):
    result = [word for word in list_words if word not in STOP_WORDS]
    return result


# Count duplicate words and create dictionary
def word_count(list_words):
    dict_word_count = {}
    for word in list_words:
        if word in dict_word_count:
            dict_word_count[word] += 1
        else:
            dict_word_count[word] = 1
    return dict_word_count


# We need to get the Union of these two dictionaries
def create_txt_union(txt_one, txt_two):
    txt_one_set = set(txt_one)
    txt_two_set = set(txt_two)
    txt_union = txt_one_set.union(txt_two_set)
    return txt_union


# Creating the vectors for these two dictionaries
def create_vectors(txt_one_dict, txt_two_dict, union):
    # Creating vector for first txt
    vector_one = []
    for word in union:
        try:
            vector_one.append(txt_one_dict[word])
        except KeyError:
            vector_one.append(0)

    # Creating vector for second txt
    vector_two = []
    for word in union:
        try:
            vector_two.append(txt_two_dict[word])
        except KeyError:
            vector_two.append(0)
    return vector_one, vector_two


def create_dot_product(vec_one, vec_two):
    dot_product = sum(v1_element * v2_element for v1_element, v2_element in zip(vec_one, vec_two))
    return dot_product


def create_divisor(vec_one, vec_two):
    vec_one_divisor = sum((item ** 2 for item in vec_one))
    vec_one_divisor = math.sqrt(vec_one_divisor)
    vec_two_divisor = sum((item ** 2 for item in vec_two))
    vec_two_divisor = math.sqrt(vec_two_divisor)
    return vec_one_divisor, vec_two_divisor


def determine_txt_similarity(txt_one, txt_two):
    """"""
    # Txt One Preparation (Cleaning and then getting the dict of word count)
    txt_one_clean = strip_document(txt_one)
    txt_one_clean = lower_case(txt_one_clean)
    txt_one_clean = replace_contraction(txt_one_clean)
    txt_one_clean = keep_alphanum(txt_one_clean)
    txt_one_clean = remove_stop_words(txt_one_clean)
    txt_one_count = word_count(txt_one_clean)

    # Txt Two Preparation (Cleaning and then getting the dict of word count)
    txt_two_clean = strip_document(txt_two)
    txt_two_clean = lower_case(txt_two_clean)
    txt_two_clean = replace_contraction(txt_two_clean)
    txt_two_clean = keep_alphanum(txt_two_clean)
    txt_two_clean = remove_stop_words(txt_two_clean)
    txt_two_count = word_count(txt_two_clean)

    # Getting the Union of the two texts (words)
    txt_union = create_txt_union(txt_one_clean, txt_two_clean)

    # Creating the vectors for our calculation
    vec_one, vec_two = create_vectors(txt_one_count, txt_two_count, txt_union)

    # Getting the Dot Product
    dot_product = create_dot_product(vec_one, vec_two)

    # Creating the two divisors
    txt_one_divisor, txt_two_divisor = create_divisor(vec_one, vec_two)

    # Calculating the result
    result = dot_product/(txt_one_divisor * txt_two_divisor)

    return result

similarity_score = determine_txt_similarity(SAMPLE_TXT_ONE, SAMPLE_TXT_TWO)

print(round(similarity_score, 2))
