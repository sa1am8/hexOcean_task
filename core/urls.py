from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('api/media', views.ImagesApi.as_view()),
    path('api/media/<str:link>', views.ImageResizeApi.as_view())
]
