from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(verbose_name='Image', upload_to='projects')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Update date')
    link = models.URLField(verbose_name='More information', null=True, blank=True)

    class Meta:
        verbose_name = 'proyect'
        verbose_name_plural = 'proyects'
        ordering = ['-created']

    def __str__(self):
        return self.title
