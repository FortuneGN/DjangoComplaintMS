from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('signin/', auth_views.LoginView.as_view(template_name='ComplaintMS/signin.html'), name='signin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='ComplaintMS/logout.html'), name='logout'),
    path('password/', views.change_password, name='change_password'),
    path('passwords/', views.change_password_g, name='change_password_g'),
    path('counter/', views.counter, name='counter'),
    path('solved/', views.solved, name='solved'),

    path('login/', views.login, name='login'),
    path('list/', views.list, name='list'),
    path('pdf/', views.pdf_view, name='view'),
    path('pdf_g/', views.pdf_viewer, name='view'),
    path('aboutus/', views.aboutus, name='aboutus'),

    path('login_redirect/', views.login_redirect, name='login_redirect'),
    path('slist/', views.slist, name='slist'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('complaints/', views.complaints, name='complaints'),
    path('allcomplaints/', views.allcomplaints, name='allcomplaints'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='ComplaintMS/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset-done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='ComplaintMS/password_reset_done.html'
         ),
         name='password_reset_done'),
    re_path(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='ComplaintMS/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='ComplaintMS/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
