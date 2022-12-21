from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Name'
    )
    email = models.CharField(
        max_length=100,
        verbose_name='Email'
    )
    content = models.TextField(
        verbose_name='Content'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Send date'
    )

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        ordering = ['-created']

    def __str__(self):
        return self.name
