from django.db import models

# Create your models here.




class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='Blog Image/', height_field=None, width_field=None, max_length=None)
    published_date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.title}. Published On: {self.published_date}"

