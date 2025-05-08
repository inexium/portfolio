"""
handling "main" app urls
"""

from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt", content_type="text/plain"
        ),
    ),
    path(
        "sitemap.xml",
        TemplateView.as_view(
            template_name="sitemap.xml", content_type="application/xml"
        ),
    ),
]
