def query_and_translate (term):
    

    '''
    format of recieved JSON -- (the data that we want, at least):
        [
            {
                'meta': {
                    ants: [
                        'ant1', 'ant2', ..., 'antsn'
                    ]
                    syns: [
                        'syn1', 'syn2', ..., 'synsn'
                    ]
                },
                'fl': 'string part of speech',
                'shortdef': [
                    'shortdef1',
                    'shortdef2',
                    ...
                    'shortdefn'
                ]
            },
        ]
    '''
    import json
    import requests

    data = requests.get (
            f'https://dictionaryapi.com/api/v3/references/thesaurus/json/{term}?key=29029b50-e0f1-4be6-ac00-77ab8233e66b'
        ).json()

    def translate_json (data):
        '''
        Function to translate above formatted JSON to this format:
        [
            {
                'defintion': [
                    'definition1',
                    'definition2',
                    ...
                    'definitionn',
                ],
                'part': 'string part of speech',
                'synonyms': [
                    'synonym1',
                    'synonym2',
                    ...
                    'synonymn',
                ]
                'antonyms': [
                    'antonym1',
                    'antonym2',
                    ...
                    'antonymn',
                ]
            }
        ]
        '''
        def parse_list (lst):
            ret = []
            for term in lst:
                if type(term) == list:
                    new_lst = parse_list(term)
                    for item in new_lst:
                        ret.append(item)
                else:
                    ret.append(term)
            return ret

        return list (
            map (
                lambda definition: ({
                    'definitions' :  parse_list(definition[ 'shortdef' ]),
                    'part'        :  definition[ 'fl' ],
                    'synonyms'    :  parse_list(definition[ 'meta' ][ 'syns' ]),
                    'antonyms'    :  parse_list(definition[ 'meta' ][ 'ants' ]),
                }),
                data
            )
        )

    return translate_json(data)
