from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')), 
]

<<<<<<< HEAD
#commit1 
#commit5


=======
>>>>>>> parent of fdd010a (commit1)
