from django.urls import path
from.import views

urlpatterns = [
    path('Home',views.Home_page, name='Home'),
    path('sign_in', views.sign_in_page, name='sign-in'),
    path('sign_up', views.sign_up_page, name='sign-up'),
    path('Logout',views.logout_fun, name='Logout'),
    path('plan',views.plan, name='plan'),
    path('survey', views.survey_page, name='survey'),
    path("profile", views.profile, name='profile'),
    path('gender', views.gender_page, name='gender'),
    path('page1', views.page1_page, name='page1'),
]
