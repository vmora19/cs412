# marathon_analytics/urls.py
 
from django.urls import path
from . import views 
 
urlpatterns = [
    # map the URL (empty string) to the view
	path('', views.VotersListView.as_view(), name='voters'),
    path('voter/<int:pk>/', views.VoterDetailView.as_view(), name='voter'),
    path('graphs', views.GraphListView.as_view(), name='graphs'),
]