from django.urls import path
from .views import ProcessView
app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ProcessView.as_view()),
    path('articles/<int:pk>', ProcessView.as_view())
]