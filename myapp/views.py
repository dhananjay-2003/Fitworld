from django.shortcuts import render,redirect
# from .forms import signupform
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Contact
from .models import Appointment
from .models import Batch_Appointment
from .models import Feedback

from django.utils import timezone
timezone.now()

from django.template import Context
from django.template.loader import render_to_string, get_template
from django.views.generic import ListView
import datetime
import re

# Create your views here.


#Superuser Credentials
#username = FitworldAdmin
#gmail = nalawadedhananjaycode@gmail.com
#Password = Fitworld@20




def Signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        # Validate username
        if not re.match(r'^(?=.*[a-zA-Z]{5,})(?=.*\d{3,})(?=.*[!@#$%^&*()_+])[a-zA-Z\d!@#$%^&*()_+]+$', username):
            messages.error(request, "Invalid username format. It should contain at least 5 letters, 1 symbol, and 3 numbers.")

        # Validate password
        if len(password1) < 8:
            messages.error(request, "Password should contain at least 8 characters.")
        elif not any(char.isdigit() for char in password1):
            messages.error(request, "Password should contain at least 1 number.")

        # Check if the passwords match
        elif password1 != password2:
            messages.error(request, "Passwords do not match.")
        else:
            # Create a new user
            user = User.objects.create_user(username=username, password=password1, email=email)

            # Log in the user
            login(request, user)

            # Send email
            email = EmailMessage(
                subject=f"Registering on The Fitworld",
                body="Thank you for registering on the Fitworld. You are now a member of the Fitworld Family.",
                from_email=settings.EMAIL_HOST_USER,
                to=[email],
                reply_to=[settings.EMAIL_HOST_USER]
            )
            email.send()

            # Redirect to the login page or any other desired page
            return redirect('login')

    # If the request method is not POST, render the signup page
    return render(request, 'signup.html')



def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)
       
        if user is not None:
            login(request, user)

            if request.user.is_superuser:
                # return redirect('admin1')
                return redirect('admin:index')


            # return redirect('home')
            return render(request,'home.html')
        else:
            

            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
            

    return render(request, 'login.html')


def admin(request):
    return render(request, 'admin.html')


def Logout(request):

    return redirect("/login")



def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Services(request):
    return render(request, 'Services.html')

def contact(request):
    if request.method=="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        problem = request.POST['problem']

        contact = Contact(firstname =firstname, lastname = lastname, email =email, problem =problem)
        contact.save()

    return render(request, 'Contact_us.html')


def Diet(request):
    return render(request,'BMI.html')


def underweight_page(request):
    return render(request, 'underweight_page.html')

def normal_weight_page(request):
    return render(request, 'normal_weight_page.html')

def overweight_page(request):
    return render(request, 'overweight_page.html')

def obesity1_page(request):
    return render(request, 'obesity1_page.html')

def obesity2_page(request):
    return render(request, 'obesity2_page.html')

def extreme_page(request):
    return render(request, 'extreme_page.html')

def Workout(request):
    return render(request,'BMI1.html')

def Underweight_page(request):
    return render(request, 'underweight_pageW.html')

def Normal_weight_page(request):
    return render(request, 'normal_weight_pageW.html')

def Overweight_page(request):
    return render(request, 'overweight_pageW.html')

def Obesity1_page(request):
    return render(request, 'obesity1_pageW.html')

def Obesity2_page(request):
    return render(request, 'obesity2_pageW.html')

def Extreme_page(request):
    return render(request, 'extreme_pageW.html')




def appointment(request):
    
    if request.method=="POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("message")
        date = request.POST.get("date")
        course = request.POST.get("course")
        time = request.POST.get("time")

        appointment = Appointment.objects.create(first_name = fname,last_name = lname,email = email,phone = mobile,request = message, request_date = date,course=course,event_time = time, sent_date=timezone.now() )
        appointment.save()

        messages.add_message(request, messages.SUCCESS, f"{message}")
        return redirect('success')

    return render(request, 'book_appointment.html')


def Success(request):
    return render(request, 'Success.html')


def Apply(request):
    if request.method=="POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        course = request.POST.get("course")
        event = request.POST.get("event")
        date = request.POST.get("date")

        batch_appointment = Batch_Appointment(first_name = fname,last_name = lname,email = email,phone = mobile,event_time = event,course =course,request_date =date, sent_date=timezone.now() )
        batch_appointment.save()
        return redirect('success')

    return render(request,'applyappointment.html')

    

class ManageAppointmentTemplateView(ListView):
    template_name = "PAppointment.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3


    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        data = {
            "fname":appointment.first_name,
            "date":date,
        }

        message = get_template('email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name}")
        # return HttpResponseRedirect(request.path)
        return redirect('manage')


   

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({   
            "title":"Manage Appointments"
        })
        return context










class ManageBatchAppointmentTemplateView(ListView):
    template_name = "BAppointment.html"
    model = Batch_Appointment
    context_object_name = "batch_appointments"
    login_required = True
    paginate_by = 3


    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Batch_Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        data = {
            "fname":appointment.first_name,
            "date":date,
        }

        message = get_template('email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name}")
        # return HttpResponseRedirect(request.path)
        return redirect('bmanage')


   

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Batch_Appointment.objects.all()
        context.update({   
            "title":"Batch Appointments"
        })
        return context




def AdminSite(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)
       
        if user is not None:
            login(request, user)

            if request.user.is_superuser:
                # return redirect('admin1')
                return redirect('manage')


            # return redirect('home')
            return render(request,'home.html')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'adminsitelogin.html')



def Feedback1(request):
    if request.method == 'POST':
        rating = int(request.POST.get('rating', 0))
        comment = request.POST.get('comment', '')

        feedback = Feedback(rating=rating,comment=comment)
        feedback.save()

    return render(request, 'home.html')


def Fees(request):
    return render(request, 'Fees.html')
    


