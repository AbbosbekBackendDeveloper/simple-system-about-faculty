from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.views.generic import ListView
from .models import KafedraTeacher, KafedraCategory, \
    KafedraGrant, KafedraCultural, \
    KafedraInternational, KafedraLife, \
    KafedraSince, KafedraTeachersUpdate


def kafedrateachersview(request):
    category = request.GET.get('category')
    if category == None:
        teacher = KafedraTeacher.published.all()
    else:
        teacher = KafedraTeacher.objects.filter(category__name=category)
    # page = request.GET.get('page', 1)
    # paginator = Paginator(teacher, 2)
    # try:
    #     teachers = paginator.page(page)
    # except PageNotAnInteger:
    #     teachers = paginator.page(1)
    # except EmptyPage:
    #     teachers = paginator.page(paginator.num_pages)
    # page = paginator.get_page(page_num)
    categories = KafedraCategory.objects.all()
    context = {
        "teacher": teacher,
        "categories": categories,
        # "teachers": teachers,
    }
    return render(request, 'kafedra/teachers.html', context)


def teachersdetailview(request, teacher):
    teacher = get_list_or_404(KafedraTeacher, slug=teacher, status=KafedraTeacher.Status.Published)
    related = KafedraTeacher.objects.filter(status=KafedraTeacher.Status.Published)[:5]
    context = {
        "teacher": teacher,
        "related": related,
    }
    return render(request, 'kafedra/teachers-detail.html', context)


def teacherssearchview(request):
    if request.method == 'POST':
        query = request.POST['query']
        search = KafedraTeacher.objects.filter(
            Q(fish__icontains=query) | Q(description__icontains=query)
        )
        context = {
            "query": query,
            "search": search
        }
        return render(request, 'kafedra/teachers-search.html', context)
    else:
        return render(request, 'kafedra/teachers-search.html')


def kafedragrantview(request):
    category = request.GET.get('category')
    if category == None:
        teacher = KafedraGrant.published.all()
    else:
        teacher = KafedraGrant.objects.filter(category__name=category)
    # page = request.GET.get('page', 1)
    # paginator = Paginator(teacher, 2)
    # try:
    #     teachers = paginator.page(page)
    # except PageNotAnInteger:
    #     teachers = paginator.page(1)
    # except EmptyPage:
    #     teachers = paginator.page(paginator.num_pages)
    # page = paginator.get_page(page_num)
    categories = KafedraCategory.objects.all()
    context = {
        "teacher": teacher,
        "categories": categories,
        # "teachers": teachers,
    }
    return render(request, 'kafedra/grants.html', context)


def grantdetailview(request, grant):
    teacher = get_list_or_404(KafedraGrant, slug=grant, status=KafedraGrant.Status.Published)
    related = KafedraGrant.objects.filter(status=KafedraGrant.Status.Published)[:5]
    context = {
        "teacher": teacher,
        "related": related,
    }
    return render(request, 'kafedra/grant-detail.html', context)


def kafedrasinceview(request):
    category = request.GET.get('category')
    if category == None:
        teacher = KafedraSince.published.all()
    else:
        teacher = KafedraSince.objects.filter(category__name=category)
    # page = request.GET.get('page', 1)
    # paginator = Paginator(teacher, 2)
    # try:
    #     teachers = paginator.page(page)
    # except PageNotAnInteger:
    #     teachers = paginator.page(1)
    # except EmptyPage:
    #     teachers = paginator.page(paginator.num_pages)
    # # page = paginator.get_page(page_num)
    categories = KafedraCategory.objects.all()
    context = {        "teacher": teacher,
        "categories": categories,
        # "teachers": teachers,
    }
    return render(request, 'kafedra/since.html', context)


def sincedetailview(request, since):
    teacher = get_list_or_404(KafedraSince, slug=since, status=KafedraSince.Status.Published)
    related = KafedraSince.objects.filter(status=KafedraSince.Status.Published)[:5]
    context = {
        "teacher": teacher,
        "related": related,
    }
    return render(request, 'kafedra/ilmiy-detail.html', context)


def kafedralifesview(request):
    category = request.GET.get('category')
    if category == None:
        teacher = KafedraLife.published.all()
    else:
        teacher = KafedraLife.objects.filter(category__name=category)
    # page = request.GET.get('page', 1)
    # paginator = Paginator(teacher, 2)
    # try:
    #     teachers = paginator.page(page)
    # except PageNotAnInteger:
    #     teachers = paginator.page(1)
    # except EmptyPage:
    #     teachers = paginator.page(paginator.num_pages)
    # page = paginator.get_page(page_num)
    categories = KafedraCategory.objects.all()
    context = {
        "teacher": teacher,
        "categories": categories,
        # "teachers": teachers,
    }
    return render(request, 'kafedra/lifes.html', context)


def lifedetailview(request, life):
    teacher = get_list_or_404(KafedraLife, slug=life, status=KafedraLife.Status.Published)
    related = KafedraLife.objects.filter(status=KafedraLife.Status.Published)[:5]
    context = {
        "teacher": teacher,
        "related": related,
    }
    return render(request, 'kafedra/hayoti-detail.html', context)


def kafedraculturalview(request):
    category = request.GET.get('category')
    if category == None:
        teacher = KafedraCultural.published.all()
    else:
        teacher = KafedraCultural.objects.filter(category__name=category)
    # page = request.GET.get('page', 1)
    # paginator = Paginator(teacher, 2)
    # try:
    #     teachers = paginator.page(page)
    # except PageNotAnInteger:
    #     teachers = paginator.page(1)
    # except EmptyPage:
    #     teachers = paginator.page(paginator.num_pages)
    # page = paginator.get_page(page_num)
    categories = KafedraCategory.objects.all()
    context = {
        "teacher": teacher,
        "categories": categories,
        # "teachers": teachers,
    }
    return render(request, 'kafedra/culturals.html', context)


def culturaldetailview(request, cultural):
    teacher = get_list_or_404(KafedraCultural, slug=cultural, status=KafedraCultural.Status.Published)
    related = KafedraCultural.objects.filter(status=KafedraCultural.Status.Published)[:5]
    context = {
        "teacher": teacher,
        "related": related,
    }
    return render(request, 'kafedra/manaviy-detail.html', context)


def kafedrinternatinalsview(request):
    category = request.GET.get('category')
    if category == None:
        teacher = KafedraInternational.published.all()
    else:
        teacher = KafedraInternational.objects.filter(category__name=category)
    # page = request.GET.get('page', 1)
    # paginator = Paginator(teacher, 1)
    # try:
    #     teachers = paginator.page(page)
    # except PageNotAnInteger:
    #     teachers = paginator.page(1)
    # except EmptyPage:
    #     teachers = paginator.page(paginator.num_pages)
    # page = paginator.get_page(page_num)
    categories = KafedraCategory.objects.all()
    context = {
        "teacher": teacher,
        "categories": categories,
        # "teachers": teachers,
    }
    return render(request, 'kafedra/international.html', context)


def internationaldetailview(request, international):
    teacher = get_list_or_404(KafedraInternational, slug=international, status=KafedraInternational.Status.Published)
    related = KafedraInternational.objects.filter(status=KafedraInternational.Status.Published)[:5]
    context = {
        "teacher": teacher,
        "related": related,
    }
    return render(request, 'kafedra/hamkorlik-detail.html', context)


def kafedrupdatesview(request):
    category = request.GET.get('category')
    if category == None:
        teacher = KafedraTeachersUpdate.published.all()
    else:
        teacher = KafedraTeachersUpdate.objects.filter(category__name=category)
    # page = request.GET.get('page', 1)
    # paginator = Paginator(teacher, 2)
    # try:
    #     teachers = paginator.page(page)
    # except PageNotAnInteger:
    #     teachers = paginator.page(1)
    # except EmptyPage:
    #     teachers = paginator.page(paginator.num_pages)
    # page = paginator.get_page(page_num)
    categories = KafedraCategory.objects.all()
    context = {
        "teacher": teacher,
        "categories": categories,
        # "teachers": teachers,
    }
    return render(request, 'kafedra/updates.html', context)


def teachersupdatedetailview(request, teacher_update):
    teacher = get_list_or_404(KafedraTeachersUpdate, slug=teacher_update, status=KafedraTeachersUpdate.Status.Published)
    related = KafedraTeachersUpdate.objects.filter(status=KafedraTeachersUpdate.Status.Published)[:5]
    context = {
        "teacher": teacher,
        "related": related,
    }
    return render(request, 'kafedra/malaka-detail.html', context)


def lifesearchview(request):
    if request.method == 'POST':
        query = request.POST['query']
        search = KafedraLife.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
        context = {
            "query": query,
            "search": search
        }
        return render(request, 'kafedra/life-search.html', context)
    else:
        return render(request, 'kafedra/life-search.html')


def sincesearchview(request):
    if request.method == 'POST':
        query = request.POST['query']
        search = KafedraSince.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        context = {
            "query": query,
            "search": search
        }
        return render(request, 'kafedra/since-search.html', context)
    else:
        return render(request, 'kafedra/since-search.html')


def grantsearchview(request):
    if request.method == 'POST':
        query = request.POST['query']
        search = KafedraGrant.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        context = {
            "query": query,
            "search": search
        }
        return render(request, 'kafedra/grant-search.html', context)
    else:
        return render(request, 'kafedra/grant-search.html')


def culturalsearchview(request):
    if request.method == 'POST':
        query = request.POST['query']
        search = KafedraCultural.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        context = {
            "query": query,
            "search": search
        }
        return render(request, 'kafedra/cultural-search.html', context)
    else:
        return render(request, 'kafedra/cultural-search.html')


def internationalsearchview(request):
    if request.method == 'POST':
        query = request.POST['query']
        search = KafedraInternational.objects.filter(
            Q(name__icontains=query) | Q(district__icontains=query)
        )
        context = {
            "query": query,
            "search": search
        }
        return render(request, 'kafedra/international-search.html', context)
    else:
        return render(request, 'kafedra/international-search.html')


def teacherupdatesearchview(request):
    if request.method == 'POST':
        query = request.POST['query']
        search = KafedraTeachersUpdate.objects.filter(
            Q(teacher_updated_time__icontains=query)
        )
        context = {
            "query": query,
            "search": search
        }
        return render(request, 'kafedra/teacher-update-search.html', context)
    else:
        return render(request, 'kafedra/teacher-update-search.html')