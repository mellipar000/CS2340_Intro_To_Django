from django.urls import path
from . import views
urlpatterns = [
  path('', views.index, name='home.index'),
  # '' = url path, views.index = HTTP handler function, home.index = url pattern id
  path('about', views.about, name='home.about'),
  # 'about' = url path, views.about = HTTP handler function, home.about = url pattern id
]