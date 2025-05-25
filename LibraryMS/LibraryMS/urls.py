from django.conf import settings 
from django.conf.urls import url
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('', include('homepage.urls')), 
    path('admin/', admin.site.urls),
    path('useraccounts/', include('useraccounts.urls')), 
    re_path(r'feedback/', include('feedback.urls')), 
    path('book/', include('book.urls')), 
    path('bookorders/', include('bookorders.urls')),

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
