from django.shortcuts import render

def index(request):
    # renders templates & returns HTTP response  w/ content
    return render(request, 'home/index.html')
    # request = HTTP request, home/index.html =  path to template file
    
# Same as index function, except different template file
def about(request):
    return render(request, 'home/about.html')