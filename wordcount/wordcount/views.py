from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    text = fulltext.split()
    countdict = {}
    for word in text:
        if (word in countdict):
            countdict[word]+=1
        else:
            countdict[word]=1
    sortedwords = sorted(countdict.items(), key=operator.itemgetter(1),reverse=True)
   
    return render(request,'count.html',{'texts':fulltext,'sortedwords':sortedwords})

def about(request):
    return render(request,'about.html')