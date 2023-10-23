from django.contrib import admin
from django.urls import path
from collegeapp import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "সৈয়দা সেলিমা কাদের চৌধুরী ডিগ্রি কলেজ"
admin.site.site_title = "সৈয়দা সেলিমা কাদের চৌধুরী ডিগ্রি কলেজ"
admin.site.index_title = "সৈয়দা সেলিমা কাদের চৌধুরী ডিগ্রি কলেজ"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homeview, name='home'),
    path('notice/', views.allnotice, name='allnotice'),
    path('contact/', views.contactview, name='contact'),
    path('photogallery/', views.photogalleryview, name='photogallery'),
    path('cp/<str:text>', views.chairmanprincipalview, name='cp'),
    # path('info/', views.informationview, name='info'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)