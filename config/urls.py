from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path("main/", include("main.urls",namespace="main")),
    path("chat/", include("chat.urls",namespace="chat")),
    path('admin/', admin.site.urls),
]

