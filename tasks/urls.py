from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import index, by_label, TaskCreateView, attachment, TaskDetaiView, TaskUpdateView

urlpatterns = [
    path('', index, name='index'),
    path('accounts/login/', LoginView.as_view(next_page='index'), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/password_change/', PasswordChangeView.as_view(template_name='registration/change_password.html'),
         name='password_change'),
    path('accounts/password_change/done/', PasswordChangeDoneView.as_view(template_name='registration/password_changed.html'),
         name='password_change_done'),
    path('accounts/password_reset/', PasswordResetView.as_view(template_name='registration/reset_password.html',
                                                               subject_template_name='registration/reset_subject.txt',
                                                               email_template_name='registration/reset_email.txt'),
         name='password_reset'),
    path('accounts/password_reset/done', PasswordResetDoneView.as_view(template_name='registration/email_sent.html'),
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='registration/confirm_password.html'),
         name='password_reset_confirm'),
    path('accounts/reset/done/', PasswordResetCompleteView.as_view(template_name='registration/password_confirmed.html'),
         name='password_reset_complete'),
    path('attachment/', attachment, name='attachment'),
    path('add/', TaskCreateView.as_view(), name='add'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='edit'),
    path('task/<int:pk>/', TaskDetaiView.as_view(), name='detail'),
    path('<int:label_id>/', by_label, name='by_label'),
]