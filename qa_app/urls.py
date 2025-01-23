
from django.contrib import admin
from django.urls import path
from questions.views import home , upload , ask_question

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('' , home , name="home"),
    path('upload/' , upload , name="upload"),
    path('ask/' , ask_question , name = "ask")
]