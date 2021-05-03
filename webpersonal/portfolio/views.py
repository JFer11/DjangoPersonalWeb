from django.shortcuts import render
from .models import Project


def portfolio(request):
    """ All projects created through the Admin Page will be dynamically loaded into the response template. """
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio.html", {"projects": projects})
