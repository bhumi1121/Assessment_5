from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('fpswd',views.fpswd,name='fpswd'),
    path('verify_otp',views.verify_otp,name='verify_otp'),
    path('set_pswd',views.set_pswd,name='set_pswd'),

    path('add_member',views.add_member,name='add_member'),
    path('member',views.member,name='member'),
    path('delete_member/<int:pk>',views.delete_member,name='delete_member'),

    path('add_chairman',views.add_chairman,name='add_chairman'),
    path('chairman',views.chairman,name='chairman'),
    path('delete_chairman/<int:pk>',views.delete_chairman,name='delete_chairman'),

    path('add_visitor',views.add_visitor,name='add_visitor'),
    path('visitor',views.visitor,name='visitor'),
    path('delete_visitor/<int:pk>',views.delete_visitor,name='delete_visitor'),

    path('add_watchman',views.add_watchman,name='add_watchman'),
    path('watchman',views.watchman,name='watchman'),
    path('delete_watchman/<int:pk>',views.delete_watchman,name='delete_watchman'),

    path('add_event',views.add_event,name='add_event'),
    path('event',views.event,name='event'),
    path('delete_event/<int:pk>',views.delete_event,name='delete_event'),

    path('add_notice',views.add_notice,name='add_notice'),
    path('notice',views.notice,name='notice'),
    path('delete_notice/<int:pk>',views.delete_notice,name='delete_notice'),

    path('ajax/e_verify/',views.e_verify,name='e_verify'),

]
