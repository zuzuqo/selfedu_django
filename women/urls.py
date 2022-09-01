from django.urls import path
from women.views import index, about, add_article, contact, login, post_detail

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_article/', add_article, name='add_article'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', post_detail, name='post')
]
