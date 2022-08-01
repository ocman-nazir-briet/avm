from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from shop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('index', views.index, name="index"),
    path('about',views.about, name="about"),
    path('agents', views.agent, name="about"),
    path('properties', views.properties, name="properties"),
    path('contact', views.contact, name="contact"),
    path('contact2', views.contact2, name="contact2"),
    path('blog', views.blog, name="blog"),
    path('login', views.loginUser, name="login"),
    path('signup', views.signupUser, name="signup"),
    path('logout', views.logoutUser, name="logout"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('plotAdd', views.plotAdd, name='plotAdd'),
    path('agentAdd', views.agentAdd, name='agentAdd'),
    path('clientAdd', views.clientAdd, name='clientAdd'),
    path('blogAdd', views.blogAdd, name='blogAdd'),
    path('sales', views.saleAdd, name='sales'),
    path('apps-chat', views.appChat, name='appchat'),
    path('deleteBlog/<str:pk>/', views.deleteBlog, name="deleteBlog"),
    path('<int:obj_id>', views.blogSingle, name='blogSingle'),
    path('search', views.search, name="search")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

