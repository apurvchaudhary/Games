from django.db import models

# Create your models here.
class ModelBase(models.Model):
    """
    Model to save created at and updated at time and date
    """
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)


class Game(ModelBase):
    """
    Model to save Games
    """
    title= models.CharField(max_length=255, blank=False)
    platform = models.CharField(max_length=255, blank=False)
    score = models.DecimalField(max_digits=4, decimal_places=2, blank=False)
    genre = models.CharField(max_length=250, blank=False)
    editors_choice = models.BooleanField(default=False)

    def __str__(self):
        return self.title