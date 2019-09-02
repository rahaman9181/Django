from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from users import views as user_views

urlpatterns=[
path('',views.home,name="home"),
path('home',views.home,name="home"),
path('login',views.login,name="login"),
path('register',views.register,name="register"),
path('logout',views.logout,name="logout"),
path('password',views.password,name="password"),
path('password_change',views.password_change,name="password_change"),
path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
path('posts',views.post_list,name="post_list"),
path('upload',views.upload_post,name="upload_post"),
path('delete_post/<int:pk>',views.delete_post,name="delete_post"),

]
