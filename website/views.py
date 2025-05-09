from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request, "home.html", {})


def about(request):
    return render(request, "about.html", {})


def contact(request):
    if request.method == "POST":
        name = request.POST.get("message-name")
        email = request.POST.get("message-email")
        message = request.POST.get("message")
        # send an email
        send_mail(
            "New message from " + name,  # subject
            message,  # message
            email,  # from email
            ["maxmarumbwa@gmail.com"],  # to email
            fail_silently=False,  # fail silently if there is an error
        )
        return render(request, "contact.html", {"message_name": name})
    else:
        return render(request, "contact.html", {})


def blog(request):
    return render(request, "blog.html", {})
