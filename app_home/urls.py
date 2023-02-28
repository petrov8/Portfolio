from django.urls import path
import app_home.views as resource


urlpatterns = [
    path("", resource.home_view, name="home"),
    path("projects/", resource.MyProjectsView.as_view(), name="projects"),
    path("about/", resource.AboutMeView.as_view(), name="about"),
    path("contact/", resource.ContactView.as_view(), name="contact"),
]
