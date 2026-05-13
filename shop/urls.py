from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from shop import  settings
from store.views import index, details_produit

urlpatterns = [
   path('',index , name= 'index') ,
    path('admin/', admin.site.urls),
    path('produit/<str:slug>/',details_produit , name= 'produit'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)