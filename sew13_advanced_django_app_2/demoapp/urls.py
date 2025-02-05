from django.urls import path
from demoapp import views

urlpatterns = [
    path('', views.person_index, name='person_index_route'),
    path('<int:person_id>/', views.person_details, name='person_details_route'),
    # 3.) people followed by create routes to the person create page
    path('create/', views.person_create, name='person_create_route'),
    # 4.) people followed by store routes to the person store function 
    path('store/', views.person_store, name='person_store_route'),
    # 5.) people followed by edit and the id routes to edit form
    path('edit/<int:person_id>/', views.person_edit, name='person_edit_route'),
    # 6.) people followed by update and the id routes to the update function
    path('update/<int:person_id>/', views.person_update, name='person_update_route'),
    # 7.) people followed by delete and the id routes to the delete function
    path('delete/<int:person_id>/', views.person_delete, name='person_delete_route'),
]