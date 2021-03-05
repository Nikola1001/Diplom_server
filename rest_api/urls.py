from django.urls import path, include
from .views import ProcessView, CustomAuthToken
app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ProcessView.as_view()),
    path('articles/<int:pk>', ProcessView.as_view()),
    path('auth/', CustomAuthToken.as_view()),
]