from django.contrib import admin
from django.urls import path,include
from . import views
from .views import ManageAppointmentTemplateView
from .views import ManageBatchAppointmentTemplateView
from .views import Feedback

# from .views import underweight_page, normal_weight_page, overweight_page

urlpatterns = [

    path('',views.Signup,name="signup"),

    path('login',views.Login,name="login"),

    path('logout',views.Logout,name="logout"),

    path('home',views.Home,name="home"),

    path('contact',views.contact,name="contact"),

    path('about',views.About,name="about"),

    path('services',views.Services,name="services"),

    path('diet' ,views.Diet,name='diet'),

    path('underweight/', views.underweight_page, name='underweight_page'),

    path('normalweight/', views.normal_weight_page, name='normal_weight_page'),

    path('overweight/', views.overweight_page, name='overweight_page'),

    path('obesity1/', views.obesity1_page, name='obesity1_page'),

    path('obesity2/', views.obesity2_page, name='obesity2_page'),

    path('extreme/', views.extreme_page, name='extreme_page'),

    path('workout' ,views.Workout,name='workout'),

    path('under-weight/', views.Underweight_page, name='underweight_pageW'),

    path('normal-weight/', views.Normal_weight_page, name='normal_weight_pageW'),

    path('over-weight/', views.Overweight_page, name='overweight_pageW'),

    path('obesity-1/', views.Obesity1_page, name='obesity1_pageW'),

    path('obesity-2/', views.Obesity2_page, name='obesity2_pageW'),

    path('extreme-weight/', views.Extreme_page, name='extreme_pageW'),

    path('book/' ,views.appointment,name='book'),

    path('success',views.Success, name='success'),

    path('apply',views.Apply,name='apply'),

    # path('PAppointment',views.PAppointment,name='PAppointment'),
    # path('PAppointment',views.PAppointment,name='PAppointment'),
    path("PAppointment", ManageAppointmentTemplateView.as_view(), name="manage"),

    path("managebatch", ManageBatchAppointmentTemplateView.as_view(), name="bmanage"),

    path('admin-si',views.AdminSite,name='admin-si'),

    path('feedback',views.Feedback1,name='feedback'),

    path('fees',views.Fees,name='fees'),

]