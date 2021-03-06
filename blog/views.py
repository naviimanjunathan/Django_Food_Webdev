from django.shortcuts import render, get_object_or_404
from .models import BlogPost


# Create your views here.
#def home_view(request):
 #   return render(request,template_name='home.html')

def blog_view(request):
    qs = BlogPost.objects.all()
    for i in qs:
        print(i.image)
    template_name = "blog.html"
    context = {'object_list': qs}
    return render(request, template_name, context)

def read_article(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "read_article.html"
    context = {'object': obj}
    return render(request, template_name, context)
