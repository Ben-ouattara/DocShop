from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from store.views import index, details_produit
from shop import  settings
urlpatterns = [
   path('',index , name= 'index') ,
    path('admin/', admin.site.urls),
    path('produit/slug<str:slug/>', details_produit, name = 'details_produit'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
