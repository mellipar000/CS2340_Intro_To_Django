from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='movies.index'),
    # If movies path matched, execute the views.index() function
    path('<int:id>/', views.show, name='movies.show'),
    # <ind:id> = expects integer to be passed from the URL for the movie id
]