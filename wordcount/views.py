from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,"homepage.html")

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split(" ")
    count = len(wordlist)

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase the COUNT
            worddictionary[word] += 1
        else:
            #add the word to worddictionary
            worddictionary[word] = 1

    sortedlist = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse = True)
    return render(request,"count.html",{'fulltext':fulltext, 'count':count, 'sortedlist':sortedlist})

def about(request):
    return render(request, "about.html")
