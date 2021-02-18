from django.shortcuts import render
from .forms import SubSearchForm, MainSearchForm
from .scripts.query_api import query_and_translate
from .scripts.clean_word import clean_word

# The main view of this app
def main_search_view (request, *args, **kwargs):
    print(request)
    print(request.POST)

    # The user can make a search in the mainview with querystring like
    #       ?searchterm={term}.  This block will get that querystring
    #       and, if it exists, create a subsearch for that string and
    #       query that string.  Results are stored in get_request_search 
    getsearchterm = request.GET.get('searchterm', None)
    get_request_search = None if not getsearchterm else {
        'search_form': SubSearchForm({ 'search_bar': clean_word(getsearchterm) }),
        'definitions': query_and_translate(clean_word(getsearchterm))
    }

    return render(request, 'container.html', {
        'main_search_form': MainSearchForm(None),
        'get_request_search': get_request_search
    })


# View that will recieve a POST search request for a word's synonyms
#       found in request.POST[ 'search_bar' ], and will return rendered
#       HTML for a subsearch_form
# This POST is called when the user searches in a subsearch
def search_term_view (request, *args, **kwargs):
    print('SEARCH')
    print(request)
    print(request.POST)
    word = clean_word(request.POST[ 'search_bar' ])

    # Query the api and translate the messy json to something more readable
    #       for the subsearch_form.html template
    definitions = query_and_translate(word)

    return render(request, 'subsearch_form.html', {
        'search_form': SubSearchForm({ 'search_bar': word }),
        'definitions': definitions
    })
        
# View that returns rendered HTML for a blank subsearch form
# This POST is called when the user hits the '+' on a subsearch
def add_view (request, *args, **kwargs):
    print('ADD')
    print(request)
    print(request.POST)
    return render(request, 'subsearch_form.html', {
        'search_form': SubSearchForm(None)
    })


    