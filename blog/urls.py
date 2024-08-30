from django.urls import path
from .views import PostListView, RatingListCreateView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/create', PostListView.create_post, name='set-post'),
    path('ratings/', RatingListCreateView.as_view(), name='rating-list-create'),
    path('submit_rating/', RatingListCreateView.submit_rating, name='submit_rating'),
]
