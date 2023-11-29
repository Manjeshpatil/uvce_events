from django.urls import path
from . import views
# from .views import club_profile
urlpatterns = [
   path('', views.homePage, name ="home"),
#    path('students/', views.students, name ="students"),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('create_event/', views.Create_event, name="create_event"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('studentRegister/', views.studentRegister, name='student_Register'),
    # path('profile/<int:user_id>/', club_profile, name='club_profile'),
    
]
