from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('get-blogs', views.BlogReadOnlyView)

app_name = 'blog'

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt')),
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('delete-blog/<str:pk>/', views.DeleteBlogView.as_view(), name='delete-blog'),
]
