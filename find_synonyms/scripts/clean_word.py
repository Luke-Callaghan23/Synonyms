from functools import reduce
def clean_word (word):
    word = word.strip().lower()  # step 1: remove excess spaces and turn to lower case
    word = reduce (             # step 2: split the word on all spaces and only keep the longest one
        lambda acc, word: (     #       (sometimes the api will return words like 'blahblah (of)'
            acc                 #       and we'll want to strip the '(of)' )
            if len(acc) > len(word)
            else word
        ),
        word.split(),
        ''
    )
    print(word)
    return word