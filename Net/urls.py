from django.contrib import admin
from django.urls import path
from film.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloApi.as_view()),
    path('men_haqimda/', MenApi.as_view()),
    path('aktyorlar/', AkrtorlarApi.as_view()),
    path('aktyor/<int:son>/', AktyorAPI.as_view()),
]