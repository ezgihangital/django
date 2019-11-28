from django.db import models
from django.urls import reverse
# Create your models here.

class uygulama(models.Model):
    title = models.CharField(max_length=120, verbose_name='Kişi Adı')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('uygulama:detail', kwargs={'id': self.id})
    def get_create_url(self):
        return reverse('uygulama:create')
    def get_update_url(self):
        return reverse('uygulama:update', kwargs={'id': self.id})
    def get_delete_url(self):
        return reverse('uygulama:delete', kwargs={'id': self.id})