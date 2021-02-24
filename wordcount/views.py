from django.http import HttpResponse 
from django.shortcuts import render



def home_view(request):
	return render(request,'home.html')

def count_view(request):
	fulltext = request.GET['fulltext']
	wordsList = fulltext.split()
	print(fulltext)
	return render(request,'count.html', {'fulltext': fulltext, 'count': len(wordsList)})

def about_view(request):
	return render(request,'about.html')