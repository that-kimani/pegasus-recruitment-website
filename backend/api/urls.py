from django.urls import path
from .views import SubmissionView , ChatAssistancView

urlpatterns = [
    path('advanced-guidance', SubmissionView.as_view() , name='API_Submission_URL'),
    path('guidance-bot', ChatAssistancView.as_view() , name='Chat_Assistant_URL')
    
]