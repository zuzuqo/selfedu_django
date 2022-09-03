from django.urls import path
from women.views import index, about, add_article, contact, login, post_detail, show_category

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_article/', add_article, name='add_article'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', post_detail, name='post'),
    path('category/<slug:category_slug>/', show_category, name='category'),
]
