from django.urls import path
from .views import userView

urlpatterns = [
    path('', userView, name='index'),
    path('res', userView, name='res'),

]
