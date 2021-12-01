from django.shortcuts import render, redirect, get_list_or_404
from django.urls import reverse_lazy
from django.shortcuts import HttpResponse
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib.auth.models import User
from UserProfile.models import UserProfile
import random

# accont_sid = "ACda4df1442a11a89a0dc2ece25a1e3212"
# auth_tocken = "c0fc6f59f66522d83231ac3cf74b1423"

# def send_otp(accont_sid, auth_tocken, body, from_, to_):
#     from twilio.rest import Client
#     client = Client(accont_sid, auth_tocken)
#     message = client.messages \
#                 .create(
#                      body=body,
#                      from_=from_,
#                      to=to_,
#                  )
#     print(message.sid)


def index(request):
    title = {'title': "Home"}
    return render(request, 'index.html', title)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        valid_user = authenticate(
            request, username=username, password=password)
        if valid_user is not None:
            auth_login(request, valid_user)
            return redirect(reverse_lazy('UserProfile:index'))
        else:
            return HttpResponse("wrong informations")

    return render(request, 'UserProfile/login.html')


def registrations(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        Password = request.POST.get('password')
        Password2 = request.POST.get('password2')
        DateOfBirth = request.POST.get('DateOfBirth')
        profession = request.POST.get('profession')
        bloodGroup = request.POST.get('bloodGroup')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        thana = request.POST.get('thana')
        union = request.POST.get('union')
        postCode = request.POST.get('postCode')

        check_user = User.objects.filter(email=email).first()
        check_profile = UserProfile.objects.filter(phone=phone).first()

        if Password != Password2:
            context1 = {"message1": "Password mismatch", "class1": "danger"}
            return render(request, 'UserProfile/registration.html', context1)

        if check_user or check_profile:
            context = {"message": "User already exist", "class": "danger"}
            return render(request, 'UserProfile/registration.html', context)

        user = User.objects.create_user(
            first_name=fname, last_name=lname, username=username, email=email, password=Password)
        user.save()

        # otp = str(random.randint(1000, 9999))
        profile= UserProfile(user=user,
                              phone=phone, DateOfBirth=DateOfBirth,
                              profession=profession,
                              bloodGroup=bloodGroup,
                              gender=gender,
                              city=city,
                              thana=thana,
                              union=union,
                              postCode=postCode,
        )
        profile.save()

        context = {"message": "Successfully registrations Complate",
                    "class2":"alert1 success ",
                   }
        return render(request, 'UserProfile/login.html', context)

        # message_body = f'''Your otp code- {otp}'''
        # send_otp(accont_sid, auth_tocken, message_body, '+8801765044544', phone)
        # return redirect(reverse_lazy('UserProfile:gootp'))

        # send_otp(phone, otp)
        # request.session['phone'] = phone
        # return redirect('gootp')

    return render(request, 'UserProfile/registration.html')


def user_profile(request,username):
    user_information=get_list_or_404(User, username=username)
    context={"title":"Profile", "user_information":user_information}
    return render(request, 'UserProfile/Profile.html', context)
    # return render(request, 'UserProfile/test.html', context)

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('UserProfile:index'))


# def gootp(request):
#     return render(request, 'UserProfile/otp.html')
