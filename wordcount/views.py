from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')
def count(request):
    fulltext=request.GET['text']
    wordlist=fulltext.split()
    cmbne=""
    for i in wordlist:
        cmbne+=i
    totalchar=len(cmbne)
    countdict={}
    for word in wordlist:
        if word in countdict:
            countdict[word]+=1
        else:
            countdict[word]=1
    noofoccurence=sorted(countdict.items(),key=operator.itemgetter(1),reverse=True)
    top5=[]
    try:
        for i in range(5):
            top5.append(noofoccurence[i])
    except:
        pass

    return render(request,'count.html',{'text':fulltext,'count':len(wordlist),'totchar':totalchar,'wordcount':top5})
def about(request):
    return render(request,'about.html')
