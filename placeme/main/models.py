from django.db import models
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model





from django.contrib.auth.models import AbstractUser



from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Additional custom fields
    regno = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=20, default='student')
    
    # Explicitly define the username field with a default value
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=True,
        default=""
    )

    def save(self, *args, **kwargs):
        # If username is empty, set it to the email
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email






class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'



class Tutor(models.Model):
    """Tutor Table"""

    tutor_id = models.AutoField(primary_key=True)
    tutor_name = models.CharField(max_length=255)
    department = models.CharField(max_length=100) # Tutor's department
    semester = models.PositiveIntegerField()       # Semester they tutor for
    division = models.CharField(max_length=50)       # Division they handle

    def __str__(self):
        return self.tutor_name

User = get_user_model()

class Student(models.Model):
    """Student Table"""

    reg_no = models.CharField(max_length=20, primary_key=True)  # Student Registration Number as PK
    # Change this field from ForeignKey to OneToOneField
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    department = models.CharField(max_length=100)
    semester = models.PositiveIntegerField()
    date_of_birth = models.DateField(blank=True, null=True)
    batch = models.CharField(max_length=20)
    division = models.CharField(max_length=20, null=True)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    tutor = models.ForeignKey('Tutor', on_delete=models.SET_NULL, blank=True, null=True, related_name="students")

    def __str__(self):
        return self.reg_no

class Marks(models.Model):
    """Marks Table"""

    reg_no = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks') # FK to student table
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)  # Adjust max_digits and decimal_places as needed
    backlog = models.PositiveIntegerField(default=0) #Default Value provided
    sem = models.PositiveIntegerField()

    class Meta:
        # Add composite primary key to prevent duplicate marks entries
        unique_together = ('reg_no', 'sem')


    def __str__(self):
        return f"{self.reg_no} - Semester {self.sem}"



class PlacementOffer(models.Model):
    """Placement Offer Table"""

    offer_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    cgpa_required = models.DecimalField(max_digits=4, decimal_places=2)
    no_of_backpapers = models.PositiveIntegerField(default=0) # Default backpapers
    salary = models.DecimalField(max_digits=12, decimal_places=2)  # Adjust digits as required
    description = models.TextField(blank=True, null=True) # Can be empty
    skillset = models.TextField(blank=True, null=True) # Can be empty
    contact_email = models.EmailField()
    posted_date = models.DateField()
    final_date = models.DateField()

    def __str__(self):
        return self.company_name

class Application(models.Model):
    """Application Table"""

    appli_id = models.AutoField(primary_key=True) # Auto Increamenting Primary key field
    reg_no = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="applications") #Relation with student
    offer_id = models.ForeignKey(PlacementOffer, on_delete=models.CASCADE, related_name="applications")  # Relation with PlacementOffer table
    status = models.CharField(max_length=50)  # e.g., "Applied", "Shortlisted", "Rejected"
    applied_date = models.DateField()

    def __str__(self):
        return f"Application {self.appli_id} - {self.reg_no}"  # More informative string representation



