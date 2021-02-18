from said_synonyms.models import Category, SaidSynonym

from sys import argv


def categorize (category):
    def term (synonym):
        resp = input(f'{str(synonym)} ? ')
        if resp.lower().startswith('y'):
            category.terms.add(synonym)
    return term

category = argv[1]
cat_obj = Category.objects.get(name=category)
syns = SaidSynonym.objects.all()


list(map(categorize(cat_obj), syns))