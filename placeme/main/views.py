
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StudentRegistrationForm
# Assuming you have defined your User model for the existing MySQL table as discussed



# def signup(request):
#     if request.method == "POST":
#         print("Form submitted!")  # Debug print
#         print("POST data:", request.POST)
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         firstname = request.POST.get('firstname')
#         lastname = request.POST.get('lastname')
#         regno = request.POST.get('regno')
        
#         # Create and save the new user
#         new_user = User(
#             email=email,
#             password=password,  # In production, use set_password() to hash the password!
#             firstname=firstname,
#             lastname=lastname,
#             regno=regno
#             # role will default to 'student' from your model
#         )
#         try:
#             new_user.save()
        
#             print("User saved successfully.")
#             print("Total users now:", User.objects.count())
#             # Redirect to student_register view after successful signup
            
#             return redirect('student_register')
#         except Exception as e:
#             print("Error saving user:", e)
#             messages.error(request, "Error during signup: " + str(e))
#             return redirect('signup')
            
#     return render(request, 'signup.html')


def signup(request):
    if request.method == "POST":
        print("Form submitted!")  # Debug print
        print("POST data:", request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('firstname')  # assuming your form uses 'firstname'
        last_name = request.POST.get('lastname')
        regno = request.POST.get('regno')
        
        # Create the new user instance.
        new_user = User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            regno=regno  # custom field on your user model
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
            return redirect('student_register')
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
            messages.success(request, "Logged in successfully!")
            role = user.role.lower() if hasattr(user, 'role') and user.role else ""
            
            if role == "student":
                return redirect('student_dashboard')  # URL name for student dashboard.
            elif role == "tutor":
                return redirect('tutor_dashboard')   
            elif role == "admin":
                return redirect('admin_dashboard')        # URL name for tutor page.
            else:
                
                return redirect('login')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    
    # For GET requests, render the login template.
    return render(request, 'index copy.html')

# @login_required
# def student_dashboard(request):
#     # Prepare any context data needed for the student dashboard
#     context = {
#         'user': request.user,
#         # Add other context variables if needed
#     }
#     return render(request, 'student.html', context)

from .models import Student  # Import your Student model
@login_required
def student_dashboard(request):
    try:
        profile = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        profile = None
    context = {
        'user': request.user,
        'profile': profile,
    }
    return render(request, 'student.html', context)



@login_required
def tutor_dashboard(request):
    # Prepare any context data needed for the tutor dashboard
    context = {
        'user': request.user,
        # Add other context variables if needed
    }
    return render(request, 'tutor.html', context)

@login_required
def admin_dashboard(request):
    # Prepare any context data needed for the tutor dashboard
    context = {
        'user': request.user,
        # Add other context variables if needed
    }
    return render(request, 'admin.html', context)    


def logout_view(request):
    logout(request)
    return redirect('login')    


""" 
def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            # Assume the profile model has a OneToOneField linking to the user:
            profile.user = request.user
            profile.save()
            messages.success(request, "Profile updated successfully!")
            # Redirect to the student dashboard after registration
            return redirect('student_dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_form.html', {'form': form}) """
@login_required
def student_register(request):
    # Check if the student already has a profile. If yes, redirect them.
    try:
        profile = Student.objects.get(user=request.user)
        return redirect('student_dashboard')
    except Student.DoesNotExist:
        pass

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            # Link this student profile to the logged-in user
            profile.user = request.user
            # Optionally, if you want to enforce consistency, update reg_no from the user
            profile.reg_no = request.user.regno
            profile.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('student_dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        # Pre-populate the form with the registration number from the user
        initial_data = {'reg_no': request.user.regno}
        form = StudentRegistrationForm(initial=initial_data)
        
    return render(request, 'student_form.html', {'form': form})




""" 
def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            # Assume the profile model has a OneToOneField linking to the user:
            profile.user = request.user
            profile.save()
            messages.success(request, "Profile updated successfully!")
            # Redirect to the student dashboard after registration
            return redirect('student_dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_form.html', {'form': form}) """
