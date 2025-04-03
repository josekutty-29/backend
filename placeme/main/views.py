from django.shortcuts import render, redirect,get_object_or_404
from .models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StudentRegistrationForm, TutorForm, PlacementOfferForm, UserForm
from django.contrib.auth import logout
import csv
from .models import Tutor, Student, PlacementOffer, Marks, PlacementOfficer,Notification,TutorApproval,PlacementApproval
from django.db.models import Q
from django.utils import timezone

def signup(request):
    if request.method == "POST":
        print("Form submitted!")  # Debug print
        print("POST data:", request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('firstname')  # assuming your form uses 'firstname'
        last_name = request.POST.get('lastname')
        reg_no = request.POST.get('reg_no')
        # Create the new user instance.
        new_user = User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            regno=reg_no
        )
        new_user.set_password(password)  # Hash the password
        try:
            new_user.save()
            print("User saved successfully.")
            print("Total users now:", User.objects.count())
            # Set the backend manually
            new_user.backend = 'django.contrib.auth.backends.ModelBackend'
            # Log the user in
            login(request, new_user)
            messages.success(request, "Signup successful!")
            # Redirect to student_register view after successful signup
            return redirect('student_register',1)
        except Exception as e:
            print("Error saving user:", e)
            messages.error(request, "Error during signup: " + str(e))
            return redirect('signup')
    return render(request, 'signup.html')




def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('username')  # The form field for email
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            role = user.role.lower() if hasattr(user, 'role') and user.role else ""
            print(role)
            if role == "student":
                return redirect('student_dashboard')  
            elif role == "tutor":
                return redirect('tutor')   
            elif role == "admin":
                return redirect('admin_dashboard')
            elif role == 'placement_officer':
                return redirect('placement_officer')
            else:
                messages.get_messages(request).used = True  # Clear any existing messages
                messages.error(request, "Role not assigned. Please contact administrator.")
                return redirect('login')
        else:
            messages.get_messages(request).used = True  # Clear any existing messages
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    
    # For GET requests, render the login template with any messages
    messages.get_messages(request).used = True  # Clear any existing messages
    return render(request, 'index copy.html')

def forgot_password(request):
    return render()

@login_required
def student_dashboard(request):
    placement_approval = None
    try:
        profile = Student.objects.get(user=request.user)
        placement_approval= PlacementApproval.objects.filter(student = profile)
    except Student.DoesNotExist:
        profile = None
    try:
        mark = Marks.objects.filter(reg_no=profile.reg_no).first()
    except Marks.DoesNotExist:
        mark = None
    print(mark)
    if not mark:
        messages.warning(request,"Your tutor didnt update your mark...")
    if mark:
       placements = PlacementOffer.objects.filter(cgpa_required__lte=mark.cgpa,sem = profile.semester,department = profile.department,final_date__gte=timezone.now().date())
    else:   
        placements = None
    context = {
        'user': request.user,
        'profile': profile,
        'placements': placements,
        'notifications':placement_approval
    }
    return render(request, 'student.html', context)

@csrf_exempt
@login_required
def toggle_like(request, offer_id):
    if request.method == "POST":
        user = request.user
        placement = get_object_or_404(PlacementOffer, offer_id=offer_id)

        if user in placement.liked_by.all():
            placement.liked_by.remove(user)
            liked = False
        else:
            placement.liked_by.add(user)
            liked = True

        return JsonResponse({"liked": liked})
    
    return JsonResponse({"error": "Invalid request"}, status=400)

@login_required
@csrf_exempt
def toggle_apply(request, offer_id):
    if request.method == "POST":
        user = request.user
        placement = get_object_or_404(PlacementOffer, offer_id=offer_id)

        if user in placement.applied_by.all():
            placement.applied_by.remove(user)
            applied = False
        else:
            placement.applied_by.add(user)
            applied = True
        return JsonResponse({"applied": applied})
    return JsonResponse({"error": "Invalid request"}, status=400)


@login_required
def tutor_dashboard(request):
    if request.method == "POST" and request.FILES.get("csv_file"):
        csv_file = request.FILES["csv_file"]

        if not csv_file.name.endswith(".csv"):
            messages.error(request, "File is not a CSV format")
            return redirect("tutor_dashboard")

        decoded_file = csv_file.read().decode("utf-8").splitlines()
        reader = csv.DictReader(decoded_file)

        for row in reader:
            try:
                student = Student.objects.get(reg_no=row["reg_no"])
                mark, created = Marks.objects.update_or_create(
                    reg_no=student,
                    sem=row["sem"],
                    defaults={
                        "cgpa": row["cgpa"],
                        "backlog": row["backlog"]
                    }
                )
                messages.success(request, f"{student.user.first_name} {student.user.last_name}'s mark updated successfully")
            except Student.DoesNotExist:
                messages.error(request, f"Student with register number {row['reg_no']} not found.")
        return redirect("tutor_dashboard")

    tutor_instance = get_object_or_404(Tutor, user=request.user)
    students = Student.objects.filter(tutor=tutor_instance).exclude(reg_no__isnull=True)

    # Filtering logic
    sem_filter = request.GET.get("sem")
    backlog_filter = request.GET.get("backlog")
    student_filter = request.GET.get("student_filter")  # New filter for student name or reg_no
    student_sort = request.GET.get("student_sort")  # New sorting parameter

    if sem_filter and int(sem_filter) > 0:
        students = students.filter(semester=sem_filter)
    if backlog_filter:
        students = students.filter(marks__backlog=backlog_filter)
    if student_filter:
        students = students.filter(user__first_name__icontains=student_filter) | students.filter(reg_no__icontains=student_filter)
    else:
        student_filter=''

    # Sorting logic
    if student_sort == "name":
        students = students.order_by("user__first_name")
    elif student_sort == "-name":
        students = students.order_by("-user__first_name")
    elif student_sort == "regno":
        students = students.order_by("reg_no")
    elif student_sort == "-regno":
        students = students.order_by("-reg_no")

    placements = PlacementOffer.objects.all()
    marks_dict = {student.reg_no: [] for student in students}
    notification = Notification.objects.filter(receiver = request.user)
    tutor_approvals = [TutorApproval.objects.filter(nid = x) for x in notification]
    for mark in Marks.objects.filter(reg_no__in=students):
        marks_dict[mark.reg_no.reg_no].append(mark)

    context = {
        'user': request.user,
        'tutor': tutor_instance,
        'students': students,
        'placements': placements,
        'marks_dict': marks_dict,
        'student_filter': student_filter,
        'student_sort': student_sort,
        'tutor_approvals':tutor_approvals
    }
    return render(request, 'tutor.html', context)




@login_required
def export_marks_csv(request):
    # Create the HttpResponse object with CSV header
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="student_marks.csv"'

    writer = csv.writer(response)
    # Write the header row
    writer.writerow(["Register Number", "Semester", "CGPA", "Backlogs"])

    # Query all marks and write them into the CSV file
    for mark in Marks.objects.all():
        writer.writerow([mark.reg_no.reg_no, mark.cgpa, mark.backlog, mark.sem])
    return response


@login_required
def export_applied_students_marks(request,offer_id):
    print(offer_id)
    """Exports marks of all students who applied for the Placement Officer's offers."""
    placement_officer = get_object_or_404(PlacementOfficer, user=request.user)
    placement_offers = PlacementOffer.objects.filter(created_by=placement_officer,offer_id = offer_id)
    applied_users = placement_offers.values_list("applied_by", flat=True).distinct()

    # Get corresponding student profiles
    applied_students = Student.objects.filter(user__in=applied_users)

    # Prepare CSV response
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename=\"applied_students_marks.csv\"'

    writer = csv.writer(response)
    writer.writerow(["Reg No", "Name", "Semester", "CGPA", "Backlogs"])

    # Write student data
    for student in applied_students:
        marks = Marks.objects.filter(reg_no=student).order_by("-sem")  # Get marks sorted by semester
        if marks.exists():
            for mark in marks:
                writer.writerow([
                    student.reg_no,
                    f"{student.user.first_name} {student.user.last_name}",
                    mark.sem,
                    mark.cgpa,
                    mark.backlog
                ])
        else:
            # If no marks exist, write default values
            writer.writerow([
                student.reg_no,
                f"{student.user.first_name} {student.user.last_name}",
                "N/A",
                "N/A",
                "N/A"
            ])

    return response




@login_required
def placement_officer_dashboard(request):
    try:
        profile = PlacementOfficer.objects.get(user=request.user)
    except PlacementOfficer.DoesNotExist:
        profile = None
    
    placement_officer = get_object_or_404(PlacementOfficer, user=request.user,)
    placements = PlacementOffer.objects.filter(created_by=placement_officer)
    
    # Get filter and sort parameters from request
    liked_filter = request.GET.get('liked_filter', '')
    liked_sort = request.GET.get('liked_sort', '')
    applied_filter = request.GET.get('applied_filter', '')
    applied_sort = request.GET.get('applied_sort', '')
    
    # Initialize dictionaries for liked and applied users
    liked = {}
    applied = {}
    accepted = {}

    # Gather all users who liked or applied
    for placement in placements:
        # Get users who liked this placement
        for user in placement.liked_by.all():
            if user not in liked:
                liked[user] = []
            liked[user].append(placement)
        
        # Get users who applied to this placement
        for user in placement.applied_by.all():
            if user not in applied:
                applied[user] = []
            applied[user].append(placement)
        
        for user in placement.accepted.all():
            if user not in accepted:
                accepted[user] = []
            accepted[user].append(placement)
            
    print(applied)
    
    # Filter liked users if a filter is provided
    if liked_filter:
        filtered_liked = {}
        for user, user_placements in liked.items():
            # Check various user attributes for the filter text
            if (liked_filter.lower() in user.username.lower() or
                liked_filter.lower() in user.first_name.lower() or
                liked_filter.lower() in user.last_name.lower() or
                liked_filter.lower() in user.email.lower() or
                (hasattr(user, 'regno') and user.regno and liked_filter.lower() in user.regno.lower())):
                filtered_liked[user] = user_placements
        liked = filtered_liked
    
    # Filter applied users if a filter is provided
    if applied_filter:
        filtered_applied = {}
        for user, user_placements in applied.items():
            # Check various user attributes for the filter text
            if (applied_filter.lower() in user.username.lower() or
                applied_filter.lower() in user.first_name.lower() or
                applied_filter.lower() in user.last_name.lower() or
                applied_filter.lower() in user.email.lower() or
                (hasattr(user, 'regno') and user.regno and applied_filter.lower() in user.regno.lower())):
                filtered_applied[user] = user_placements
        applied = filtered_applied
    
    # Sort the dictionaries
    if liked_sort:
        # Convert to list for sorting
        liked_items = list(liked.items())
        
        # Apply sorting based on criteria
        if liked_sort == 'name':
            liked_items.sort(key=lambda x: (x[0].first_name.lower(), x[0].last_name.lower()))
        elif liked_sort == '-name':
            liked_items.sort(key=lambda x: (x[0].first_name.lower(), x[0].last_name.lower()), reverse=True)
        elif liked_sort == 'email':
            liked_items.sort(key=lambda x: x[0].email.lower())
        elif liked_sort == '-email':
            liked_items.sort(key=lambda x: x[0].email.lower(), reverse=True)
        elif liked_sort == 'regno':
            liked_items.sort(key=lambda x: x[0].regno if x[0].regno else '')
        elif liked_sort == '-regno':
            liked_items.sort(key=lambda x: x[0].regno if x[0].regno else '', reverse=True)
        
        # Convert back to dictionary
        liked = dict(liked_items)
    
    # Same sorting logic for applied users
    if applied_sort:
        # Convert to list for sorting
        applied_items = list(applied.items())
        
        # Apply sorting based on criteria
        if applied_sort == 'name':
            applied_items.sort(key=lambda x: (x[0].first_name.lower(), x[0].last_name.lower()))
        elif applied_sort == '-name':
            applied_items.sort(key=lambda x: (x[0].first_name.lower(), x[0].last_name.lower()), reverse=True)
        elif applied_sort == 'email':
            applied_items.sort(key=lambda x: x[0].email.lower())
        elif applied_sort == '-email':
            applied_items.sort(key=lambda x: x[0].email.lower(), reverse=True)
        elif applied_sort == 'regno':
            applied_items.sort(key=lambda x: x[0].regno if x[0].regno else '')
        elif applied_sort == '-regno':
            applied_items.sort(key=lambda x: x[0].regno if x[0].regno else '', reverse=True)
        
        # Convert back to dictionary
        applied = dict(applied_items)
    
    context = {
        'profile': profile,
        'placements': placements,
        'liked': liked,
        'applied': applied,
        'liked_filter': liked_filter,
        'liked_sort': liked_sort,
        'applied_filter': applied_filter,
        'applied_sort': applied_sort,
    }
    
    return render(request, 'placement_officer.html', context)


@login_required
def accept_applied(request,offer_id,user_id):
    placement = PlacementOffer.objects.get(offer_id=offer_id)
    user = User.objects.get(id = user_id)
    placement.accepted.add(user)
    notification = Notification(sender = request.user,
                                receiver = user,
                                message = "You have been placed")
    notification.save()
    student = Student.objects.get(user = user)
    placement_approval = PlacementApproval(
        nid = notification,
        placement = placement,
        student =student
    )
    placement_approval.save()
    return redirect('placement_officer')

@login_required
def placement_offer_create(request):
    if request.method == "POST":
        form = PlacementOfferForm(request.POST)
        if form.is_valid():
            placement_offer = form.save(commit=False)
            placement_offer.created_by = request.user.placementofficer  # Assign current placement officer
            placement_offer.save()
            return redirect("placement_officer")  # Redirect to placement officer dashboard
    else:
        form = PlacementOfferForm()

    return render(request, "placement_offer_form.html", {"form": form})


@login_required
def placement_offer_update(request, offer_id):
    placement_offer = get_object_or_404(PlacementOffer, offer_id=offer_id)
    if request.user != placement_offer.created_by.user:
        messages.error(request,"Not Authorized")
        return redirect("placement_officer")  # Redirect if not authorized
    if request.method == "POST":
        form = PlacementOfferForm(request.POST, instance=placement_offer)
        if form.is_valid():
            form.save()
            return redirect("placement_officer")
    else:
        form = PlacementOfferForm(instance=placement_offer)
    return render(request, "tutor_form.html", {"form": form, "edit": True})

@login_required
def placement_offer_delete(request,offer_id):
    placement_offer = get_object_or_404(PlacementOffer, offer_id=offer_id)
    print("Delete process started...",placement_offer.created_by.user,"   ",request.user)
    if request.user != placement_offer.created_by.user:
        messages.error(request,"Not authorized")
        print("not authorized...")
        return redirect("placement_officer")  # Redirect if not authorized
    d = placement_offer.delete()
    if d:
        print("Delete successfull...")
        messages.success(request,"Deleted successfully")
    return redirect('placement_officer')



@login_required
def student_detail(request, student_id):
    # Get the student object for the current tutor, or 404 if not found
    print("Requesting student details...",student_id,request.user)
    student = get_object_or_404(Student, reg_no=student_id)
    form = StudentRegistrationForm(instance=student)
    context = {
        'form': form,
        'details':True
    }
    return render(request, 'student_form.html', context)




@login_required
def tutor_form(request):
    tutor = get_object_or_404(Tutor,user=request.user)
    if request.method == "POST":    
        form = TutorForm(request.POST, instance=tutor)
        if form.is_valid():
            form.save()
            return redirect("tutor_dashboard")  # Redirect after saving
    else:
        form = TutorForm(instance=tutor)  # Prefill the form for editing
    return render(request, "tutor_form.html", {"form": form, "tutor": tutor})




@login_required
def admin_dashboard(request):
    # Prepare any context data needed for the tutor dashboard
    context = {
        'user': request.user,
        # Add other context variables if needed
    }
    return render(request, 'admin.html', context)    



def logout_view(request):
    print("Session before flush:", request.session.items())
    request.session.flush()
    print("Session after flush:", request.session.items())
    logout(request)
    return redirect('login')


@login_required
def student_register(request,flag):
    print(request.user.regno)
    try:
        # Try to get the student profile for the logged-in user
        profile = Student.objects.get(reg_no=request.user.regno)
    except Student.DoesNotExist:
        profile = None  # No profile exists yet
    print(profile,request.method)
    copy = profile

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, instance=profile)  # Preload data
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user  # Ensure it's linked to the logged-in user
            profile.reg_no = request.user.regno  # Ensure reg_no remains correct
            tutor = profile.tutor
            if flag == 1:
                profile.tutor = None
            if not copy:
                notification = Notification(
                    sender = request.user,
                    receiver = tutor.user,
                    message = "New Student registeration "
                )
                notification.save()
                TutorApproval(nid = notification).save()
            profile.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('student_dashboard')
        else:
            print(form.errors)
            messages.error(request, form.errors)
    else:
        print("get...")
        if profile:
            form = StudentRegistrationForm(instance=profile)  # Load existing data into form
        else:
            print("else...")
            form = StudentRegistrationForm(initial = {'reg_no':request.user.regno})

    return render(request, 'student_form.html', {'form': form,'flag':flag})



@login_required
def student_apply_register(request,pid):
    print(request.user.regno)
    placement = PlacementOffer.objects.get(offer_id = pid)
    print(placement.offer_id)
    try:
        # Try to get the student profile for the logged-in user
        profile = Student.objects.get(reg_no=request.user.regno)
    except Student.DoesNotExist:
        profile = None  # No profile exists yet
    print(profile,request.method)

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, instance=profile)  # Preload data
        if form.is_valid():
            cleaned_data = form.cleaned_data  # Get all form data as a dictionary
            reg_no = cleaned_data.get('reg_no')
            department = cleaned_data.get('department')
            semester = cleaned_data.get('semester')
            division = cleaned_data.get('division')
            date_of_birth = cleaned_data.get('date_of_birth')
            batch = cleaned_data.get('batch')
            phone_no = cleaned_data.get('phone_no')
            tutor = cleaned_data.get('tutor')
            print(reg_no,department,semester,division,date_of_birth,batch,phone_no,tutor)
            profile = form.save(commit=False)
            profile.user = request.user  # Ensure it's linked to the logged-in user
            profile.reg_no = request.user.regno  # Ensure reg_no remains correct
            profile.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('student_dashboard')
        else:
            print("Invalid form")
            messages.error(request, form.errors)
    else:
        print("get...")
        if profile:
            form = StudentRegistrationForm(instance=profile)  # Load existing data into form
        else:
            print("else...")
            form = StudentRegistrationForm(initial = {'reg_no':request.user.regno})

    return render(request, 'student_form.html', {'form': form, 'placement':placement})




@login_required
def student_update(request, reg_no):
    student = Student.objects.filter(reg_no=reg_no).first()

    if not student:
        messages.error(request, "No profile found. Please register first.")
        return redirect('student_register', reg_no=reg_no)

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('tutor_dashboard')
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = StudentRegistrationForm(instance=student)

    return render(request, 'student_update.html', {'form': form, 'reg_no': reg_no})



@login_required
def remove_applied(request, offer_id, user_id):
    """Remove a user's application for a placement offer."""
    placement = get_object_or_404(PlacementOffer, offer_id=offer_id)
    user = get_object_or_404(User, id=user_id)

    if user in placement.applied_by.all():
        placement.applied_by.remove(user)

    return redirect(request.META.get("HTTP_REFERER", "placement_officer_dashboard"))



@login_required
def student_profile(request, user_id):
    """Display the profile of a student."""
    student = get_object_or_404(User, id=user_id)
    return render(request, "student_profile.html", {"student": student})



@login_required
def user_profile(request):
    """Display and update the user's profile on the same page."""
    user = request.user

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("user_profile")  # Redirect after successful update
    else:
        form = UserForm(instance=user)

    return render(request, "user_profile.html", {"form": form, "user": user})

@login_required
def confirm_approval(request,id):
    tutor = Tutor.objects.get(user = request.user)
    tutor_approval = TutorApproval.objects.get(tid = id)
    notification = tutor_approval.nid
    student = Student.objects.get(user = notification.sender)
    student.tutor = tutor
    student.save()
    tutor_approval.confirm=True
    tutor_approval.save()
    return redirect('tutor_dashboard')