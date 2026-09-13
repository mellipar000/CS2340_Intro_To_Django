from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='movies.index'),
    # If movies path matched, execute the views.index() function
    path('<int:id>/', views.show, name='movies.show'),
    # <ind:id> = expects integer to be passed from the URL for the movie id
    path('<int:id>/review/create/', views.create_review, name='movies.create_review'),
    path('<int:id>/review/<int:review_id>/edit/', views.edit_review, name='movies.edit_review'),
    path('<int:id>/review/<int:review_id>/delete/', views.delete_review, name='movies.delete_review'),
    path('<int:id>/review/<int:review_id>/report', views.report_review, name='movies.report_review'),
]