from django.urls import path
from .views import SubmissionView

urlpatterns = [
    path('advanced-guidance', SubmissionView.as_view() , name='API_Submission_URL'),
    
]