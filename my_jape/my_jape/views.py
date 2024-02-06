from django.http import HttpResponse
from django.shortcuts import render

def template_view(request):
    return render(request, 'template_site.html')
    # return HttpResponse("<h3>JAPE WEBSITE</h3>")