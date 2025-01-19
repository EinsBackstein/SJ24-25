"""
URL configuration for demo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from demoapp import views
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # Other URL patterns go here
    path('admin/', admin.site.urls),
    path('demo/', views.index_demo),
    path('people/', include('demoapp.urls')),
    path('', RedirectView.as_view(pattern_name='person_index_route', permanent=False)),
]



# urlpatterns = [
#     # 1.) people path routes to index
#     # 2.) people path followed by the id routes to the person details with this id
#     path('people/<int:person_id>/', views.person_details, name='person_details_route'),
#     # 3.) people followed by create routes to the person create page
#     path('people/create/', views.person_create, name='person_create_route'),
#     # 4.) people followed by store routes to the person store function
#     path('people/store/', views.person_store, name='person_store_route'),
#     # 5.) people followed by edit and the id routes to edit form
#     path('people/edit/<int:person_id>/', views.person_edit, name='person_edit_route'),
#     # 6.) people followed by update and the id routes to the update function
#     path('people/update/<int:person_id>/', views. person_update, name='person_update_route'),
#     # 7.) people followed by delete and the id routes to the delete function
#     path('people/delete/<int:person_id>/', views.person_delete, name='person_delete_route'),

# ]