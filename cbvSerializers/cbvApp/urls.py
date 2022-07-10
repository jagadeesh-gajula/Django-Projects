from django.urls import path
from .views import StudentDetail, StudentList, mixin_student_list, mixin_student_detail ,generic_student_list,generic_student_details

urlpatterns = [
    path('cbv',StudentList.as_view()),

    path('cbv/<int:pk>/',StudentDetail.as_view()),

    path('mixin',mixin_student_list.as_view()),

    path('mixin/<int:pk>',mixin_student_detail.as_view()),

    path('generics',generic_student_list.as_view()),

    path('generics/<int:pk>',generic_student_details.as_view())
]