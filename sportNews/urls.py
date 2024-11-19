from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path("", views.home, name="home"),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('sportNews/<int:id>/', views.article_detail, name='article_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)