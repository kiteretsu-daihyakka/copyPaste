from django.http import HttpResponse
from django.shortcuts import render
from .models import textData

def index(request):
    entrdTxt = None
    if request.method == 'GET':
        entrdTxt = request.GET['textHere']
        if textData.objects.filter().count() is 0:
            textData(txt=entrdTxt).save()
        else:
            textData.objects.filter().update(txt=entrdTxt)
        return render(request,'textFieldForm.html',context={'entrdTxt':entrdTxt})


    for td in textData.objects.filter():
        entrdTxt = td.txt

    print(entrdTxt)
    return render(request,'textFieldForm.html',context={'entrdTxt':entrdTxt})
        
    # return HttpResponse('<input>')