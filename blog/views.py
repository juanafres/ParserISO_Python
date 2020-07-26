from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .parserISO import ParserIso
# Create your views here.

def post_list(request):
    miParser = ParserIso()
    if(request.GET.get('mybtn') and (not request.GET.get('isoTextBox') == "" )):
        posts = miParser.parsearIso(str(request.GET.get('isoTextBox')))
        return render(request,'blog/post_list.html', {'posts': posts})
    return render(request, 'blog/post_list.html', {'posts': []})

def request_page(request):
    if(request.GET.get('mybtn')):
        vector = parserISO.mypythonfunction( request.GET.get('mytextbox') )
    return render(request,'blog/post_list.html', {'campos': vector})