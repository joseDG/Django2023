
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #users app
    re_path('', include('applications.users.urls')),
    # urls producto app
    re_path('', include('applications.producto.urls')),
    # urls venta
    #re_path('', include('applications.venta.urls')),

    # routers
    #re_path('', include('applications.producto.routes')),
    #re_path('', include('applications.venta.routes')),
]
