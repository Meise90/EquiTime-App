from datetime import date
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from EquiTimeProject import settings
from .models import PhoneModel
from .tokens import generate_token
import phonenumbers

# Create your views here.

def home_view(request):
    today = date.today()
    current_day = today.strftime("%A")


    return render(
        request,
        'homepageapp/home.html',
        context={
            'today': today,
            'current_day': current_day,
        }
    )


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=username) and User.is_active:
            messages.error(request, 'Username already exists. Please try some other username.')
            return redirect('homepageapp:register-view')

        # if User.objects.filter(email=email):
        #     messages.error(request, 'Email already registered. Please use another email address.')
        #     return redirect('homepageapp:register-view')

        if len(username) > 10:
            messages.error(request, 'Username must be under 10 characters.')
            return redirect('homepageapp:register-view')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match.")
            return redirect('homepageapp:register-view')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric.")
            return redirect('homepageapp:register-view')

        my_user = User.objects.create_user(username, email, pass1)
        my_user.first_name = fname
        my_user.last_name = lname
        my_user.is_active = False
        my_user.save()

        phone_number = request.POST.get('phone_number')

        phone_number = PhoneModel(phone_number=phone_number, user=my_user)
        if phonenumbers.is_valid_number(phone_number.phone_number):
            phone_number.save()
        else:
            messages.error(request, "This is not a valid phone number. Please give your number with country code "
                                    "and without any spaces, e.g. +48111222333")
            my_user.delete()
            return redirect('homepageapp:register-view')

        messages.success(request, "Your account has been successfully created. "
                                  "We have sent you welcome and address confirmation emails!")

        # Welcome Email

        subject = "Welcome to EquiTime Application!"
        message = 'Hello ' + my_user.first_name + "! \n" + "Thank you for visiting our website. \n" \
                                                           "Your login: " + my_user.username
        from_email = settings.EMAIL_HOST_USER
        to_list = [my_user.email]
        # fail_silently=True / if our email fails to send it still won't crash our app
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email with confirmation link

        current_site = get_current_site(request)
        email_title = "Confirm your email address."
        message_2 = render_to_string('email_confirmation.html', {
            'name': my_user.first_name,
            'username': my_user.username,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(my_user.pk)),
            'token': generate_token.make_token(my_user),
        })
        email = EmailMessage(
            email_title,
            message_2,
            settings.EMAIL_HOST_USER,
            [my_user.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('homepageapp:index-view')

    if request.method == "GET":
        return render(
            request,
            'registration/register.html',
        )


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        my_user = User.objects.get(pk=uid)

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        my_user = None

    if my_user is not None and generate_token.check_token(my_user, token):
        my_user.is_active = True
        my_user.save()
        login(request, my_user)
        return render(
            request,
            'email_confirmed.html',
        )
    else:
        return render(
            request,
            'activation_failed.html'
        )


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        my_user = authenticate(request, username=username, password=pass1)

        if my_user is not None:
            login(request, my_user)
            fname = my_user.first_name
            return render(
                request,
                'homepageapp/home.html',
                context={
                    'fname': fname
                }
            )

        else:
            messages.error(request, "Bad credentials! Please make sure that you confirmed your email address.")

            return redirect('homepageapp:index-view')

    if request.method == "GET":
        return render(
            request,
            'registration/signin.html'
        )


def index_view(request):
    return render(
        request,
        'registration/index.html',
    )


def logout_view(request):
    logout(request)
    messages.success(request, "You are logged out!")
    # return redirect('homepageapp:home-view')

    return render(
        request,
        'registration/logout.html',
    )
