from django.urls import path
from .views import status_page, check_status, add_website, delete_website

urlpatterns = [
    path('', status_page, name='status_page'),
    path('check_status/', check_status, name='check_status'),
    path('add_website/', add_website, name='add_website'),
    path('delete_website/<int:website_id>/', delete_website, name='delete_website'),
]