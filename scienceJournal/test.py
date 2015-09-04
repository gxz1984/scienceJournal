__author__ = 'ibm'
import json

# Reading data back
with open('../data_utf8.json', 'r') as f:
    data = json.load(f)
    print(data['article_list'])