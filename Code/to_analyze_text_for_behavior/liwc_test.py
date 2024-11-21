# https://youtu.be/fqQvZvyBoJk?si=qyix38an9fP24HiA


# AFTER: https://youtu.be/MAiHS-rpUuE?si=DN1VBtMXtDS4LtPs

from collections import Counter
import liwc
import re

parse, category_names = liwc.load_token_parser(
    '../LIWC2007_English100131.dic')


def tokenize(text):
    for match in re.finditer(r'\w+', text, re.UNICODE):
        yield match.group(0)


file = open("Elizabeth_Preprocessed.txt", 'r')
elizabeth = file.readline().lower()
elizabeth_tokens = tokenize(elizabeth)
print(elizabeth_tokens)

elizabeth_counts = Counter(
    category for token in elizabeth_tokens for category in parse(token))
print(elizabeth_counts)


Counter({'cogmech': 840, 'relativ': 767, 'verb': 681, 'present': 668, 'social': 502, 'affect': 444, 'funct': 395, 
         'time': 390, 'assent': 368, 'posemo': 311, 'insight': 306, 'bio': 285, 'motion': 228, 'percept': 201, 
         'space': 195, 'work': 187, 'health': 186, 'negemo': 133, 'negate': 132, 'excl': 131, 'tentat': 122, 
         'achieve': 116, 'home': 98, 'feel': 83, 'quant': 83, 'filler': 81, 'humans': 78,
        'adverb': 77, 'discrep': 75, 'hear': 74, 'leisure': 63, 'certain': 62, 'incl': 61, 'family': 59, 
        'body': 58, 'relig': 57, 'pronoun': 57, 'ipron': 57, 'death': 47, 'anx': 37, 'cause': 36, 'inhib': 35, 
        'see': 35, 'preps': 33, 'ingest': 30, 'anger': 28, 'money': 24, 'friend': 24, 'sad': 18, 'auxverb': 13, 
        'sexual': 13, 'number': 11, 'nonfl': 4, 'past': 4, 'conj': 2, 'swear': 2, 'future': 1})
