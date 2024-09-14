from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),  # Home page with student list
    path('create', views.create_student, name='create_student'),  # Create new student
    path('edit/<int:student_id>', views.edit_student, name='edit_student'),  # Edit student
    path('delete/<int:student_id>', views.delete_student, name='delete_student'),  # Delete student
]
