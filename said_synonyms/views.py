import json
from django.shortcuts import render
from .scripts.create_categories import create
from .scripts.view_syns import get_intersections

from .forms import SearchForm, AddForm
from .models import Category, SaidSynonym

# 'view/'
def view_syns_view (request, *args, **kwargs):
    print(request)
    print(request.user)

    # When the page is first loaded in, we get all categories
    categories = create([])
    return render(request, 'view/view_synonyms.html', {
        'main_search_form': SearchForm(None),
        'categories': categories,
        'singles': True
    })


# 'view/search/singles/'
def search_singles_view (request, body=None, *args, **kwargs):
    print(request)

    print('Body: ')    
    print(request.body)

    if not body:
        jsonBody = json.loads(request.body)
        cat_list = jsonBody['categories']
        add      = jsonBody['add']
    else:
        cat_list = []
        add      = True


    categories = create(cat_list)

    return render(request, 'category_list.html', {
        'categories': categories,
        'singles': True,
        'add': add
    })

# 'view/search/combinations/'
def search_combinations_view (request, *args, **kwargs):
    print(request)

    print('Body: ')    
    print(request.body)

    cat_list = json.loads(request.body)[ 'categories' ]
    categories = create(cat_list)

    intersections = get_intersections(categories, categories.keys())

    print(intersections)

    return render(request, 'category_list.html', {
        'categories': intersections,
        'singles'   : False,
    })




# 'add/'
def add_syns_view (request, *args, **kwargs):
    print(request)
    print(request.user)


    categories = create([])
    return render(request, 'add/add_synonyms.html', {
        'main_search_form': AddForm(None),
        'categories'      : categories,
        'singles'         : True
    })


# 'add/add/'
def add_view (request, *args, **kwargs):
    print(request)
    print(request.user)
    
    
    print('Body: ')    
    print(request.body)

    body = json.loads(request.body)
    
    # Getting the string term and list of categories to add that
    #       term to
    term       = body[ 'term' ]
    categories = body[ 'categories' ]

    try: 
        term_model = SaidSynonym.objects.get(term=term)
    except:
        # Creating a new model for the term being added
        term_model = SaidSynonym(term=term)
        term_model.save()

    for category in categories:
        try:
            # Try to recieve the model from the database
            category_model = Category.objects.get(name=category)
        except:
            # If the model doesn't exist, an error will be raised,
            #       so we need to create and save that category
            category_model = Category(name=category)
            category_model.save()
        
        try: 
            category_model.terms.get(term=term)
        except:
            # If the term is not already found in that category, add it
            category_model.terms.add(term_model)

    return search_singles_view(request, body=True)

# 'add/remove/'
def remove_view (request, *args, **kwargs):
    print(request)
    print(request.user)
    
    
    print('Body: ')    
    print(request.body)

    body = json.loads(request.body)
    
    # Getting the string term
    term = body[ 'term' ]

    print(term)

    try: 
        term_model = SaidSynonym.objects.get(term=term)
        term_model.delete()
    except:
        pass

    return search_singles_view(request, body=True)