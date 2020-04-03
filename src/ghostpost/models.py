from django.db import models
from django.utils import timezone
import random

class Post(models.Model):
    u_id = models.IntegerField(default=random.randint(0, 999999), blank=False)
    post_type = models.CharField(choices=[('B', 'boast'), ('R', 'roast')], blank=False, max_length=1)
    text = models.CharField(blank=False, max_length=280)
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.text