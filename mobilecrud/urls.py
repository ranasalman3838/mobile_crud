from django.urls import path
from . import views


urlpatterns = [
    (path('',views.mobile_list)),
    (path("mobile/data/<int:id>",views.mobile))
    
]