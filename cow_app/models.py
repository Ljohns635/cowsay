from django.db import models

class CowText(models.Model):
    speak = models.CharField(max_length=150)

    def __str__(self):
        return self.speak
