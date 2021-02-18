from django.shortcuts import render

@csrf_exempt
def main_view (request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, 'home.html', {})
