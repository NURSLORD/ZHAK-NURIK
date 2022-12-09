from django.shortcuts import render
from main.models import *


# Create your views here.
def main_page(request):
    latest = LatestWork.objects.all()
    context = {
        'latests': latest,
        'h': 'active',
        'title': 'main'
    }
    return render(request, "index.html", context)


def blog_page(request):
    con = {
        'title': 'blog'
    }
    return render(request, "blog.html",context = con)


def blog_post_page(request):
    return render(request, "blog-post.html")


def contact_page(request):
    return render(request, "contact.html")


def portfolio_page(request):
    con = {
        'p': 'active',
        'title': 'Nurs'
    }
    return render(request, "portfolio.html", con)


def portfolio_item_page(request):
    latest = LatestWork.objects.all()
    context = {
        'latests': latest}
    return render(request, "portfolio-item.html", context=context)


def ui_elements_page(request):
    return render(request, "ui-elements.html")
