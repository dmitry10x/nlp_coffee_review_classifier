# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import re
import pymorphy2
import math


m1 = pymorphy2.MorphAnalyzer()


#Читаем .csv с отзывами
data = pd.read_csv('data.csv', sep=';', names=['review','label'])
data.head()


with open('dictionary.csv', newline='') as f:
    reader = csv.reader(f)
    dictionary = list(reader)[0]

def transform_input(review, dictionary):
    raw_tokens = review.split(' ')
    for i in range(len(raw_tokens)):
        raw_tokens[i] = raw_tokens[i].lower()
        raw_tokens[i] = re.sub('[!@#$]', '', raw_tokens[i])
        raw_tokens[i] = re.sub('[.@#$]', '', raw_tokens[i])
        raw_tokens[i] = re.sub('[,@#$]', '', raw_tokens[i])
        raw_tokens[i] = re.sub('[?@#$]', '', raw_tokens[i])
        raw_tokens[i] = re.sub('[)@#$]', '', raw_tokens[i])
        raw_tokens[i] = re.sub('[:@#$]', '', raw_tokens[i])
        raw_tokens[i] = re.sub('[(@#$]', '', raw_tokens[i])
        try:
#             raw_tokens[i] = m2.analyze(raw_tokens[i])[0]['analysis'][0]['lex']
            raw_tokens[i] =  m1.normal_forms(raw_tokens[i])[0]
        except:
            raw_tokens[i] = ''

        x = np.array([], dtype='int64')
#         print(raw_tokens)
        for feature in dictionary:
            if feature in raw_tokens:
                x = np.append(x, [1])
            else:
                x = np.append(x, [0])

    return x


def predict_cosine_dist_1(review, X_pos=X_pos, X_neg=X_neg):
    if type(review) == str:
        x = transform_input(str(review), cv)
    else:
        x = review
    #tran
#     x = x.reshape(-1,1)
    dist_pos = distance.cosine(x,X_pos)
    dist_neg = distance.cosine(x,X_neg)
    print(dist_pos, dist_neg)
    if dist_pos < dist_neg:
        return 1
    else:
        return 2
