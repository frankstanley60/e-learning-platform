"""
URL configuration for e_learning_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
   path('', RedirectView.as_view(url='core/dashboard')),
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),  # Include core URLs
    path('users/', include('users.urls')),  # Include users app URLs
    path('content/', include('content_management.urls')),  # Include your content management app's URLs
    path('learning/', include('adaptive_learning.urls')),
    path('interaction/', include('user_interaction.urls')),
      # assuming your app is named 'learning'
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
