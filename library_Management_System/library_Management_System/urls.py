from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/books/', permanent=True)), 
    path('authors/', include('Authors.urls')),
    path('books/', include('Books.urls')),
    path('members/', include('Members.urls')),
    path('borrowing/', include('Borrowing.urls')),
]