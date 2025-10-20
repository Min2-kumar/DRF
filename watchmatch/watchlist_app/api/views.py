from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.decorators import api_view

# from watchlist_app.models import Movie
# from watchlist_app.api.serializers import MovieSerializers

from watchlist_app.models import WatchList, StreamPlatform
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer


class StreamPlatformAPIView(APIView):

    def get(self, request):
        streamplatform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(streamplatform, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class StreamPlatformDetailAPIView(APIView):

    def get(self, request, pk):
        try:
            streamplatform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error':'Not found data'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatformSerializer(streamplatform)
        return Response(serializer.data)
    
    def put(self, request, pk):
        streamplatform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(streamplatform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        streamplatform = StreamPlatform.objects.get(pk=pk)
        streamplatform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAPIView(APIView):
    def get(self, request):
        watchlist = WatchList.objects.all()
        serializer = WatchListSerializer(watchlist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSerializer(watchlist)
        return Response(serializer.data)
    
    def put(self, request, pk):
        watchlsit = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(watchlsit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Watchlsit = WatchList.objects.get(pk=pk)
        Watchlsit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# --------------------------------------------------------------------------------------------------

# class WatchListAPIView(APIView):
#     def get(self, request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializers(movies, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = MovieSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# class MovieDetailAPIView(APIView):
#     def get(self, request, pk):
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error':'Not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = MovieSerializers(movie)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializers(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, pk):
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# -----------------------------------------------------------------------------------------------------------------
# ['GET', 'POST', 'PUT', 'DELETE']  -- > ye display button bhi show krate hai

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializers(movies, many=True)
#         return Response(serializer.data)     # 200 OK by default
    
#     if request.method == 'POST':
#         serializer = MovieSerializers(data=request.data)    # request.data --> jo data client post kr raha
#         if serializer.is_valid():
#             serializer.save()   # then runs to [def create(self, validated_data):] in serializers.py
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
    
#     if request.method == 'GET':

#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = MovieSerializers(movie)
#         return Response(serializer.data)
    

#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializers(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# # -----------------------------------------------------------------------------------------------------------------