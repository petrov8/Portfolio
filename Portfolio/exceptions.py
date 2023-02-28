
from django.shortcuts import render


def handle_404(request, exception):
    return render(request, "exceptions/404.html", status=404)


