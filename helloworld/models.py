from django.db import models

class Subscribers(models.Model):
    email = models.EmailField(blank=True)
    name = models.CharField(max_length=10, blank=True)
    image = models.FileField(upload_to='csv', blank=True)


    def __str__(self):
        return "%s %s %s" % (self.email, self.name, self.image)
