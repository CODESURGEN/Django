from django.shortcuts import render , HttpResponse

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is homepage")

def about(request):
    return HttpResponse("This is about page")
   
def contact(request):
    return HttpResponse("This is contact page")
   
