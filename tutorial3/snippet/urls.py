from django.urls import path
from .views import GetSnippet
urlpatterns = [
    path('', GetSnippet.as_view())
]
