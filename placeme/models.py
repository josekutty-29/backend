from django.db import models

class User(models.Model):
    email = models.CharField(unique=True,max_length=254, blank=True, null=True)
    password = models.CharField(max_length=254, blank=True, null=True)
    role = models.CharField(max_length=20,default='student')
    firstname = models.CharField(max_length=20, blank=True, null=True)
    lastname = models.CharField(max_length=20, blank=True, null=True)
    regno = models.CharField(max_length=20, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
 # Manually add the is_authenticated property
    @property
    def is_authenticated(self):
        # For this custom model, you might simply return True.
        # Note: This is only a workaround and does not check if the user is truly authenticated.
        return True
    class Meta:
        managed = True
        db_table = 'user'

    