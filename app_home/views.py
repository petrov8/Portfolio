from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, DetailView, TemplateView

from app_home.SEND_IN_BLUE_client import send_email
from app_home.forms import ContactForm
# Create your views here.


# No login or auth / no CSRF required
@csrf_exempt
def home_view(request):
    form = ContactForm(request.POST or None)
    email_sent = False
    form_errors = False

    if request.method == "POST":
        form_errors = True if form.errors else False
        email_sent = True if send_email(request) else False

    return render(request, "base.html", {
        "form": form,
        "email_sent": email_sent,
        "form_errors": form_errors
    })


class AboutMeView(TemplateView):
    pass


class MyProjectsView(DetailView):
    pass


class ContactView(CreateView):
    pass




