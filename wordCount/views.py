from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def count(request):
    fullText = request.GET['fullText']
    wordList = fullText.split()
    wordDict = {}
    for eachWord in wordList:
        if eachWord in wordDict:
            #increase
            wordDict[eachWord] = wordDict[eachWord] + 1
        else:
            #add word to dictionary
            wordDict[eachWord] = 1
    sortedWordDict = sorted(wordDict.items(), key = operator.itemgetter(1), reverse=True)
    return render(request,'count.html', {'fullTextKey':fullText, 'CountKey':len(wordList), 'sortedWordDictionaryKey':sortedWordDict})

def about(request):
    return render(request,'about.html')
