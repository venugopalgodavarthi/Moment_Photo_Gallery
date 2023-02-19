from django.db import models

# Create your models here.


class categoriesmodel(models.Model):
    ctname = models.CharField(max_length=50)

    def __str__(self):
        return self.ctname


class imagesmodel(models.Model):
    ctname = models.ForeignKey(categoriesmodel, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='pics')
    userid = models.CharField(max_length=50)
