
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.utils.timezone import now
import uuid
import hashlib


class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "student", "Student"
        ADMIN = "admin", "Admin"
        PLACEMENT_OFFICER = "placement_officer", "Placement Officer"
        TUTOR = "tutor", "Tutor"

    regno = models.CharField(max_length=20, unique=True, blank=True, null=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT
    )

    username = models.CharField(
        max_length=150,
        unique=True,
        blank=True,
        default=""
    )

    def save(self, *args, **kwargs):
        if not self.regno:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # YYYYMMDDHHMMSS
            unique_id = str(uuid.uuid4().hex[:6]).upper()  
            raw_regno = f"REG{timestamp}{unique_id}"  
            self.regno = hashlib.sha256(raw_regno.encode()).hexdigest()[:20]

        if not self.username:
            self.username = self.email

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.email} ({self.regno})"

    class Meta:
        db_table = "main_user"


class Department(models.Model):
    """Department Table"""
    name = models.CharField(max_length=100, unique=True)  # Department name
    code = models.CharField(max_length=10, unique=True)  # Short code like 'CSE', 'ECE'
    head = models.CharField(max_length=100, blank=True, null=True)  # Head of the department
    contact_email = models.EmailField(blank=True, null=True)  # Department email
    description = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return self.name


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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    tutor_id = models.AutoField(primary_key=True)
    tutor_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,default=1) # Tutor's department
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
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='students_dept',default=1)
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

class PlacementOfficer(models.Model):
    """Placement Officer Model"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # One officer per user

    def __str__(self):
        return f"Placement Officer: {self.user.username}"


class PlacementOffer(models.Model):
    """Placement Offer Model"""
    offer_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    cgpa_required = models.DecimalField(max_digits=4, decimal_places=2)
    no_of_backpapers = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    skillset = models.TextField(blank=True, null=True)
    contact_email = models.EmailField()
    posted_date = models.DateField()
    final_date = models.DateField()
    sem = models.IntegerField(default=6,blank=False)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,default=1)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_placements", blank=True)
    applied_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="applied_placements", blank=True)
    created_by = models.ForeignKey(PlacementOfficer, on_delete=models.CASCADE, related_name="offers_created")
    accepted = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='accepted_students',blank=True)

    def __str__(self):
        return f"{self.company_name} (Managed by {self.created_by.user.username})"


    # Method to check if a PlacementOfficer is authorized to modify this offer
    def is_managed_by(self, officer):
        return self.created_by == officer


    # Remove Like (Only if Officer Owns This Offer)
    def remove_like(self, officer, student):
        if not self.is_managed_by(officer):
            return "You are not authorized to manage this offer!"
        
        if student in self.liked_by.all():
            self.liked_by.remove(student)
            self.save()
            return f"{student.username}'s like removed from {self.company_name}"
        return f"{student.username} has not liked {self.company_name}"


    # Add Applicant (Only if Officer Owns This Offer)
    def add_applicant(self, officer, student):
        if not self.is_managed_by(officer):
            return "You are not authorized to manage this offer!"
        
        if student not in self.applied_by.all():
            self.applied_by.add(student)
            self.save()
            return f"{student.username} applied for {self.company_name}"
        return f"{student.username} has already applied for {self.company_name}"


    # Remove Applicant (Only if Officer Owns This Offer)
    def remove_applicant(self, officer, student):
        if not self.is_managed_by(officer):
            return "You are not authorized to manage this offer!"
        
        if student in self.applied_by.all():
            self.applied_by.remove(student)
            self.save()
            return f"{student.username} removed from {self.company_name} applications"
        return f"{student.username} has not applied for {self.company_name}"



class Application(models.Model):
    """Application Table"""

    appli_id = models.AutoField(primary_key=True) # Auto Increamenting Primary key field
    reg_no = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="applications") #Relation with student
    offer_id = models.ForeignKey(PlacementOffer, on_delete=models.CASCADE, related_name="applications")  # Relation with PlacementOffer table
    status = models.CharField(max_length=50)  # e.g., "Applied", "Shortlisted", "Rejected"
    applied_date = models.DateField()

    def __str__(self):
        return f"Application {self.appli_id} - {self.reg_no}"  # More informative string representation



class Notification(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_notifications", blank=False)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_notifications", blank=False)
    message = models.TextField()
    status = models.BooleanField(default=False)
    date = models.DateField(default=now)
    
class TutorApproval(models.Model):
    tid = models.AutoField(primary_key=True)
    nid = models.ForeignKey(Notification, on_delete=models.CASCADE)
    confirm = models.BooleanField(default=False)
    
class PlacementApproval(models.Model):
    pid = models.AutoField(primary_key=True)
    nid = models.ForeignKey(Notification, on_delete=models.CASCADE,related_name="placement_notification")
    placement = models.ForeignKey(PlacementOffer,on_delete=models.CASCADE,related_name="placement_details")
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="placement_student_notification",default=1)