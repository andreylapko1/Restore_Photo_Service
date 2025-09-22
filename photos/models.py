from django.contrib.auth.models import User
from django.db import models
from django.db.models import ImageField, CharField, ForeignKey, CASCADE


class Photos(models.Model):
    PHOTOS_STATUS_CHOICES = [
        ('Pending', 'pending'),
        ('Complete', 'complete')
    ]
    original_photo = ImageField(upload_to='uploads/')
    restored_photo = ImageField(null=True)
    status = CharField(choices=PHOTOS_STATUS_CHOICES, default='pending')
    user = ForeignKey(User, on_delete=CASCADE)






