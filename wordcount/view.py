from django.http import HttpResponse
from django.shortcuts import render
import operator
def home_page(request):
    # return HttpResponse('<h1>This is homepage</h1>')
    return render(request,'home.html',{'Name':'Ankit here!!'})

def about(request):
    return render(request,'about.html')

# def contact(request):
    # return HttpResponse('<h1>Contact Page</h1><br>This is contact page')

def count(request):
    data = request.GET['data']
    word_list=data.split()
    list_length =len(word_list)
    word_dict ={}
    for word in word_list:
        if word not in word_dict:
            word_dict[word]=1
        else:
            word_dict[word]+=1
    sorted_list=sorted(word_dict.items(),key=operator.itemgetter(1),reverse=True)
    # sorted_list=word_dict.item.sort(reverse=True)

    # print(data)
    return render(request,'count.html',{'fulltext':data,'words':list_length,'worddict':sorted_list})
