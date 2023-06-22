from django.urls import path
from . import views


urlpatterns = [path('',views.upload,name='upload'),
               path('combine',views.combine,name='combine')
        ]

