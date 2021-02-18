from collections import defaultdict

# Default categories can be shortened by typing just the first letter of the categoriy,
#       those categories can be found in this default dict
default_cats = defaultdict(lambda: None, { 
    'A': 'Argumentative',
    'D': 'Downcast',
    'C': 'Cruel',
    'E': 'Excited',
    'H': 'Happy',
    'I': 'Irritated',
    'P': 'Playful',
    'R': 'Reassuring',
    'S': 'Surprised',
    'M': 'Mad',
    'N': 'Neutral'
})