from django.db import models

class SearchBox(models.Model):
    Text_box = models.TextField(max_length=255)



class ValueSearch(models.Model):
    title = models.TextField(max_length=255)
    titles = models.TextField(max_length=255)
    urls = models.TextField(max_length=2550)
    price = models.TextField(max_length=255)


