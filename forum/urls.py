from django.urls import path

from .views import ForumView


urlpatterns = [
    path("", ForumView.as_view()),
]
