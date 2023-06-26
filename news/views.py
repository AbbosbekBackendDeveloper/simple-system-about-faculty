# from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_list_or_404, HttpResponse, redirect
from .models import News, Category, Contact
from .forms import ContactForm
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.db.models import Q


# Create your views here.


def home(request):
    news = News.objects.all().order_by('-published_time')[:3]
    context = {
        "news": news,
    }
    return render(request, 'home.html', context)


def newslistview(request):
    category = request.GET.get('category')
    if category == None:
        newss = News.published.all()
    else:
        newss = News.objects.filter(category__name=category)
    paginator = Paginator(newss, 6)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('/')
    categories = Category.objects.all()
    context = {
        "newss": newss,
        "categories": categories,
        "newss": page,
    }
    return render(request, 'news-list.html', context)


def newsdetailview(request, news):
    news = get_list_or_404(News, slug=news, status=News.Status.Published)
    related = News.objects.filter(status=News.Status.Published)[:5]
    context = {
        "news": news,
        "related": related,
    }
    return render(request, 'news-detail.html', context)


def newssearchview(request):
    if request.method == 'POST':
        query = request.POST['query']
        search = News.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
        context = {
            "query": query,
            "search": search
        }
        return render(request, 'news-search.html', context)
    else:
        return render(request, 'news-search.html')


def contactview(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h3> Xabaringiz uchun tashakkur! </h3>")
    context = {
        "form": form,
    }

    return render(request, 'contact.html', context)
