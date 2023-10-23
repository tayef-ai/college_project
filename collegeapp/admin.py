from django.contrib import admin
from .models import Carousal, Notice, Quote, Information, PhotoGallery, Visitor

@admin.register(Visitor)
class VisitorModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp')

@admin.register(Carousal)
class CarousalModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'date')

@admin.register(PhotoGallery)
class PhotoGalleryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'date')

@admin.register(Notice)
class NoticeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'document', 'date')
    search_fields = ('title',)

@admin.register(Quote)
class QuoteModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'principal_image', 'principal_quote', 'chairman_image', 'chairman_quote')

@admin.register(Information)
class InformationModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'protisthan_porichiti', 'pathdan_songkranto', 'mpo_info', 'teacher_staff', 'managing_committee', 'eleven_class', 'tweleve_class', 'degree_class')

    