"""
This Python File
"""

import re

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
                 "after you check out and we will find the savings for you."

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


print("Base:", SAMPLE_TXT_ONE)
SAMPLE_TXT_ONE = strip_document(SAMPLE_TXT_ONE)
SAMPLE_TXT_ONE = lower_case(SAMPLE_TXT_ONE)
SAMPLE_TXT_ONE = replace_contraction(SAMPLE_TXT_ONE)
SAMPLE_TXT_ONE = keep_alphanum(SAMPLE_TXT_ONE)
SAMPLE_TXT_ONE = remove_stop_words(SAMPLE_TXT_ONE)
print(SAMPLE_TXT_ONE)
SAMPLE_TXT_ONE_COUNT = word_count(SAMPLE_TXT_ONE)

print("Base:", SAMPLE_TXT_TWO)
SAMPLE_TXT_TWO = strip_document(SAMPLE_TXT_TWO)
SAMPLE_TXT_TWO = lower_case(SAMPLE_TXT_TWO)
SAMPLE_TXT_TWO = replace_contraction(SAMPLE_TXT_TWO)
SAMPLE_TXT_TWO = keep_alphanum(SAMPLE_TXT_TWO)
SAMPLE_TXT_TWO = remove_stop_words(SAMPLE_TXT_TWO)
print(SAMPLE_TXT_TWO)
SAMPLE_TXT_TWO_COUNT = word_count(SAMPLE_TXT_TWO)

SAMPLE_TXT_UNION = create_txt_union(SAMPLE_TXT_ONE, SAMPLE_TXT_TWO)

print("Words txt 1:", len(SAMPLE_TXT_ONE))
print("Words txt 2:", len(SAMPLE_TXT_TWO))
print("Union:", SAMPLE_TXT_UNION)
print("Length of Union", len(SAMPLE_TXT_UNION))

SAMPLE_VEC_ONE, SAMPLE_VEC_TWO = create_vectors(SAMPLE_TXT_ONE_COUNT, SAMPLE_TXT_TWO_COUNT, SAMPLE_TXT_UNION)

print("Vector One", SAMPLE_VEC_ONE)
print("Vector Two", SAMPLE_VEC_TWO)

'''


import math
import re
from collections import Counter

WORD = re.compile(r"\w+")


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    print(intersection)
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    print(numerator)

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


text1 = "This is a foo bar sentence ."
text2 = "This sentence is similar to a foo bar sentence ."

vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)
#print(vector1)
#print(vector2)

cosine = get_cosine(vector1, vector2)

#print("Cosine:", cosine)




from collections import Counter

def build_vector(iterable1, iterable2):
    counter1 = Counter(iterable1)
    counter2 = Counter(iterable2)
    print(counter1)
    print(counter1.keys())
    print(counter2.keys())
    all_items = set(counter1.keys()).union(set(counter2.keys()))
    print(all_items)
    vector1 = [counter1[k] for k in all_items]
    vector2 = [counter2[k] for k in all_items]
    return vector1, vector2

l1 = "Julie loves me more than Linda loves me".split()
l2 = "Jane likes me more than Julie loves me or".split()


v1, v2 = build_vector(l1, l2)

print(v1, v2)

'''