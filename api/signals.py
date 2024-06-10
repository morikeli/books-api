from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Book
import uuid


@receiver(pre_save, sender=Book)
def generate_bookID(sender, instance, **kwargs):
    if instance.id is None:
        instance.id = uuid.uuid4()
