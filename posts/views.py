from django.shortcuts import render
from django.http import HttpResponse
from .get_posts import result


def search_form(request):
    return render(request, 'posts/search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        posts = result(q)
        return render(request, 'posts/search_results.html', {'posts': posts, 'query': q})

    else:
        return HttpResponse('You submitted an empty form.')


