from django.urls import path
from django.contrib.auth import views as v
from . import views



urlpatterns = [
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('signup/',views.sign_view, name='signup'),
    path('passwordrest/',v.PasswordResetView.as_view(),name='reset_password'),
    path('passwordrest-sent/',v.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('passwordrest/<uidb64>/<token>/',v.PasswordResetView.as_view(),name='password_reset_confirm'),
    path('passwordrest_complete/',v.PasswordResetCompleteView.as_view(),name='password_reset_complete')

]
