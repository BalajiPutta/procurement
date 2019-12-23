"""Procurement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView, ListView

from Procurement import settings
from Procurement_app.models import *
from Procurement_app.views import *

from Procurement.procurement_app.models import Product_details
from views import home, admin_login, adding_Product, sign_in, user_Sign_Up, user_logout, admin_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='main_page'),
    path('admin_home/',TemplateView.as_view(template_name='admin_home.html'),name='admin_home'),
    path('admin_sign_in/',admin_login,name='admin_sign_in'),
    path('product_add/',TemplateView.as_view(template_name='product_add.html'),name='product_add'),
    path('adding_product/',adding_Product,name='adding_product'),
    path('product_all/',ListView.as_view(template_name='product_all.html',model=Product_details),name='product_all'),







    path('user_home/',TemplateView.as_view(template_name='user_home.html'),name='user_home'),
    path('user_signup/',TemplateView.as_view(template_name='user_signup.html'),name='user_signup'),
    path('sign_in/',sign_in,name='sign_in'),
    path('user_sign_up/',user_Sign_Up,name='user_sign_up'),
    path('user_logout/',user_logout,name='user_logout'),
    path('user_raise_req/',TemplateView.as_view(template_name='user_raise_req.html'),name='user_raise_req'),
    path('admin_logout/',admin_logout,name='admin_logout')
]

urlpatterns += (
    static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT))