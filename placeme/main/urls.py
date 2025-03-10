from django.urls import path
from .views import signup ,login_view # We'll create this view next

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
]
