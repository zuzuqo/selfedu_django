from django.urls import path
from women.views import index, categories, archive

urlpatterns = [
    path('', index, name='home'),
    path('categories/<int:cat_id>/', categories),
    path('archive/<int:year>/', archive),
]
