from django.urls import path
# from watchlist_app.api.views import movie_list, movie_details
# from watchlist_app.api.views import WatchListAPIView, MovieDetailAPIView
from watchlist_app.api.views import WatchListAPIView, WatchDetailAPIView, StreamPlatformAPIView, StreamPlatformDetailAPIView

urlpatterns = [
    # movie/
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>/', movie_details, name='movie-details'),

    # Class Based APIView
    path('list/', WatchListAPIView.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAPIView.as_view(), name='movie-details'),
    
    path('stream/', StreamPlatformAPIView.as_view(), name='stream-platform'),
    path('stream/<int:pk>/', StreamPlatformDetailAPIView.as_view(), name='stream-list'),
]
