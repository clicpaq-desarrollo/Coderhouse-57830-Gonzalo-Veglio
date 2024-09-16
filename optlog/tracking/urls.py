from django.urls import path
from .views import AddTrackingView

app_name = 'tracking'

urlpatterns = [ 
    path('admin-panel/tracking/create/', AddTrackingView.as_view(), name='tracking_create'),

 ]
 