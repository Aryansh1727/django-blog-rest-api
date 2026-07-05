from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # USERS FIRST
    path('api/', include('users.urls')),

    # POSTS SECOND
    path('', include('helloworld.urls')),
]