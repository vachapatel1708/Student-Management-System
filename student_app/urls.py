from django.urls import path,include
from.import views

urlpatterns = [
    path('',views.home),
    path('showlist/',views.showlist,name='showlist'),
    path('addstudent/',views.addstudent),
    path('studentdetail/<int:id>',views.studentdetail),
    path('delete/<int:id>',views.delete),
    path('update/<int:id>',views.update),
    path('showpayment/',views.showpayment),
    path('addpayment/',views.addpayment),
    path('attendance/',views.attendance),
    path('mark_attendance/',views.mark_attendance),
    path('exam/',views.exam),
    path('about/',views.about),
    path('login/',views.login),
    path('register/',views.register),
    path('logout/',views.user_logout, name="logout")
]