from django.http import HttpResponse
from django.http import HttpRequest,request
from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def count(request):
    text=request.GET['fulltext']
    text_list=text.split()
    wordcount={}
    for word in text_list:
        if word in wordcount:
            wordcount[word]+=1
        else:
            wordcount[word]=1

    return render(request,'count.html', {'textis':text, 'length':len(text_list),'wordcount':wordcount.items()})
