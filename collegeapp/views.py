from django.shortcuts import render
from .models import Carousal, Notice, Quote, Information, PhotoGallery, Visitor
from django.core.paginator import Paginator
def homeview(request):
    visitor_count = Visitor.objects.count()
    info_query = Information.objects.last()
    carousal_query = Carousal.objects.all().order_by('-id')[:4]
    pg_query = PhotoGallery.objects.all().order_by('-id')[:3]
    notice_query = Notice.objects.all().order_by('-id')[:8]
    qoute_query = Quote.objects.last()
    return render(request, 'home.html', {'notices': notice_query, 'carousals': carousal_query, 'quote':qoute_query, 'info': info_query, 'photo_gallery': pg_query, 'visitor_count': visitor_count})

def allnotice(request):
    info_query = Information.objects.last()
    query = Notice.objects.all()
    return render(request, 'detail.html', {'notices': query, 'info': info_query})

def contactview(request):
    info_query = Information.objects.last()
    return render(request, 'contact.html', {'info': info_query})

def photogalleryview(request):
    info_query = Information.objects.last()
    pg = PhotoGallery.objects.all().order_by('-id')
    all_post = PhotoGallery.objects.all()
    paginator = Paginator(all_post, 25, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'photogallery.html', {'photo_gallery': pg, 'info': info_query, 'page_obj': page_obj})

def chairmanprincipalview(request, text):
    info_query = Information.objects.last()
    qoute_query = Quote.objects.last()
    if text == 'chairman':
        pic = qoute_query.chairman_image
        des = qoute_query.chairman_quote
        name = "সভাপতির বাণী"
    else:
        pic = qoute_query.principal_image
        des = qoute_query.principal_quote
        name = "অধ্যক্ষের বাণী"
    return render(request, 'chairmanprincipal.html', {'name':name, 'pic':pic, 'des':des, 'info': info_query})
