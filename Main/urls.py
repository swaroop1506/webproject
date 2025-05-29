from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('gallery/',views.gallery,name = 'gallery'),  #for Gallery
    path('contact/',views.contact,name = 'contact'),    # for Contact
    path('about-us/',views.about_us,name = 'about-us'),
    
    path("about_founder/",views.founder ,name = 'founder'),
    path('new-user/',views.new_user,name ='new_user'),
    path('register_user/',views.register_user,name ='register_user'),
    path('login/',views.sign_in,name = 'login'),
    path('logout/',views.sign_out,name = 'logout'),
    path('forgot-password/', auth_views.PasswordResetView.as_view(template_name="home/forgotpassword.html"), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="home/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="home/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="home/password_reset_complete.html"), name='password_reset_complete'),

    # path('logout/',auth_views.LogoutView.as_view(template_name='home/school_website.html'),name = 'logout'),
    # link after login
]