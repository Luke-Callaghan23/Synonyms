from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import Form1, Form2, SimpleSearchForm

@csrf_exempt
def test_2_forms_view (request, *args, **kwargs):
    print(request)
    print(request.POST)
    if not request.POST:
        form1 = Form1(None)
        form2 = Form2(None)
        return render(request, 'two_forms.html', {
            'form1': form1,
            'form2': form2
        })
    elif 'id' in request.POST:
        id = int(request.POST[ 'id' ])
        if id == 1:
            return JsonResponse({
                'Form': '1'
            })
        elif id == 2:
            return JsonResponse({
                'Form': '2'
            })

@csrf_exempt
def test_multi_forms_view (request, *args, **kwargs):
    print(request)
    print(request.POST)
    return render(request, 'multi_forms/base.html', {
        'search_form': SimpleSearchForm(None),
    })

@csrf_exempt
def test_multi_forms_search_view (request, *args, **kwargs):
    print('SEARCH')


    import random

    num_syns = random.randrange(1, 30)
    num_syns = 35

    from functools import reduce
    syns = list(map(lambda x: (
        reduce (
            lambda acc, item: '{}{}'.format(acc, 'abcdefghijklmnopqrstuvwxyz'[ random.randrange(26) ]),
            range(random.randrange(3, 12)),
            ''
        )
    ), range(num_syns)))

    print(syns)

    return render(request, 'multi_forms/form.html', {
        'search_form': SimpleSearchForm(request.POST),
        'other_stuff': syns
    })
    

@csrf_exempt
def test_multi_forms_add_view (request, *args, **kwargs):
    print('ADD')
    return render(request, 'multi_forms/form.html', {
        'search_form': SimpleSearchForm(None)
    })


    