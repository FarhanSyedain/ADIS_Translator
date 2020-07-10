from django.urls import path
from .views import home,translate
urlpatterns = [
    path('',home,name='home'),
    path('trans/',translate,name='t'),
]