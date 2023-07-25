from django.urls import path
from blog.views import BlogListView, BlogCreatView, BlogDetailView, BlogUpdateView, BlogDeleteView, published_func, \
    FullListView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='start_list'),
    path('create/', BlogCreatView.as_view(), name='create'),
    path('view/<int:pk>', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
    path('full_list/', FullListView.as_view(), name='full_list'),
    path('publishing/<int:pk>', published_func, name='published_func')
]
