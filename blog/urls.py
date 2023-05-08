from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.home_view, name='home'),
    path('<slug:blog_slug>/', views.single_post, name='single_post'),
    path('category/<slug:category_slug>/', views.category_view, name='category_url'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)