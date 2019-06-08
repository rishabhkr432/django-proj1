import operator

from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html', {'Creator': "Unknown Asura"})


def count(request):
    user_text = request.GET['textdata']
    spacelist = user_text.split()
    checkword = {}
    for word in spacelist:
        if word in checkword:
            checkword[word] += 1
        else:
            checkword[word] = 1

    sorted_words = sorted(checkword.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',
                  {'userdata': user_text, 'count': len(spacelist), 'wordkey': sorted_words, 'Creator': "Unknown Asura"})


def about(request):
    return render(request, 'about.html', {'Creator': "Unknown Asura"})
