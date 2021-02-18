import json

# data = json.loads('[]')


# parse_list = lambda lst: ([
#     term
#     if   type(term) != type([])
#     else [ inner_term for inner_term in parse_list(term) ]
#     for term in 
#     lst
# ])

# def parse_list (lst):
#     ret = []
#     for term in lst:
#         if type(term) == list:
#             new_lst = parse_list(term)
#             for item in new_lst:
#                 ret.append(item)
#         else:
#             ret.append(term)
#     return ret



# lst = list (
#     map (
#         lambda definition: ({
#             'synonyms'    :  parse_list(definition[ 'meta' ][ 'syns' ]),
#             'antonyms'    :  parse_list(definition[ 'meta' ][ 'ants' ]),
#             'part'        :  definition[ 'fl' ],
#             'definition'  :  parse_list(definition[ 'shortdef' ])
#         }),
#         data
#     )
# )

# print(json.dumps(lst))


# import requests

# print(json.dumps(requests.get('https://dictionaryapi.com/api/v3/references/thesaurus/json/test?key=29029b50-e0f1-4be6-ac00-77ab8233e66b').json()))
