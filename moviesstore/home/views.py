from django.shortcuts import render

def index(request):
    template_data = {}
    template_data['title'] = 'Movies Store'
    # renders templates & returns HTTP response  w/ content
    return render(request, 'home/index.html', 
                  {'template_data': template_data}) # template_data = browser tab title
    # request = HTTP request, home/index.html = path to template file
    
# Same as index function, except different template file
def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'home/about.html', 
                  {'template_data': template_data})