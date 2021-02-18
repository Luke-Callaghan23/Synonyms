

from ..models import Category, SaidSynonym

def create (cat_list):

    all = len(cat_list) == 0

    print(all)

    # Creating a dictionary for all Category objects and their 
    #       associated synonyms
    return {
        str(x) : list(map(
            lambda term: str(term),
            x.terms.all()
        ))
        for x in Category.objects.all()#[:2]
        if all or str(x) in cat_list
    }