from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student, Marks

@receiver(post_save, sender=Student)
def create_initial_marks(sender, instance, created, **kwargs):
    """Create an initial Marks entry when a new Student is created."""
    if created:
        Marks.objects.create(reg_no=instance, sem=instance.semester, cgpa=0, backlog=0)  # Default values
