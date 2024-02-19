from django.urls import path
from . import views 
urlpatterns = [
    path('login/',views.StudentLoginView.as_view()),
    path('signup/',views.StudentSignupView.as_view()),
    # path('test_token/',views.test_token),
]
