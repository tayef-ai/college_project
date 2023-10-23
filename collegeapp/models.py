from django.db import models

class Visitor(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Carousal(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to='carousal')
    date = models.DateTimeField(auto_now=True)

class PhotoGallery(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to='photo_gallery')
    date = models.DateTimeField(auto_now=True)

class Notice(models.Model):
    title = models.CharField(max_length=255)
    document = models.FileField(upload_to='notice')
    date = models.DateTimeField(auto_now=True)

class Quote(models.Model):
    principal_image = models.ImageField(upload_to='principal')
    principal_quote = models.TextField()
    chairman_image = models.ImageField(upload_to='chairman')
    chairman_quote = models.TextField()
    date = models.DateTimeField(auto_now=True)

class Information(models.Model):
    protisthan_porichiti = models.FileField(upload_to="information")
    pathdan_songkranto = models.FileField(upload_to="information")
    mpo_info = models.FileField(upload_to="information")
    teacher_staff = models.FileField(upload_to="information")
    managing_committee = models.FileField(upload_to="information")
    eleven_class = models.FileField(upload_to="information")
    tweleve_class = models.FileField(upload_to="information")
    degree_class = models.FileField(upload_to="information")