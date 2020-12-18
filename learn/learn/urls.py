
from django.contrib import admin
from django.urls import path
from . import views

from blog import views as app


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('blog/', app.blog),
    path('home/', views.blog,name='home'),
    path('signup/', views.signup_view, name="signup")
]
 