from functools import reduce


# Function to take a list of items and return the
#       'power set' of that list including every
#       possible combination of items in that list
def get_power_set (lst):
    return [[
            item
            for bit, item
            in zip( ('{:0' + str(len(lst)) + 'b}').format(mask), lst )  # zip the binary string of mask integer, and the parameter list
            if int(bit)                                                 # include all entries in parameter list where a bit is set in mask bit string
        ]
        for mask
        in range(1, 2 ** len(lst))                                      # For every integer between [1, 2 ^ length of array), called mask
        if mask & (mask - 1) != 0                                       # Only keep bit strings with more than one bit set
    ]
    

def get_intersections (categorized, search_categories):
    
    power_set = get_power_set(search_categories)
    length    = len(power_set)

    ret = {}
    for combination in power_set:
        lst = list(reduce (
            lambda intersections_acc, cur_syns: (
                    intersections_acc.intersection (
                        set(categorized [ 
                            cur_syns
                        ] or [])
                    )
                ),
                combination[1:],
                # Starting point of reduction is the synonyms of the first category
                #       casted to a set
                set(categorized [ 
                    combination[0]
                ] or []
            )
        ))
        print(lst)
        if len(lst) > 0 or length < 50:
            ret[ ' / '.join(s.capitalize() for s in combination) ] = lst

    return ret


# print(cats)