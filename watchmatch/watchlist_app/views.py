from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse

#           BASIC API CONCEPT IN DJANGO

# RETURN ALL OBJECTS
def movie_list(request):
    movies = Movie.objects.all()
    print(movies)   # <QuerySet [<Blog: Beatles Blog>]> | that is not iterable, need to convert in iterable
    print(movies.values())   # dict inside list | now it will return dict that is iterable
    data ={
        'movie' : list(movies.values())
    }
    return JsonResponse(data)

# that is output
# {
#   "movie": [
#     {
#       "id": 1,
#       "name": "Python vs Java",
#       "description": "description1",
#       "active": true
#     },
#     {
#       "id": 2,
#       "name": "JavaScript the face",
#       "description": "description2",
#       "active": true
#     }
#   ]
# }

# ---------------------------------------------------------------------------------------------------------------------

# RETURN INDIVIDUAL ELEMENTS
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    print('this is movie: ',movie)      # movie → is an instance of the Movie model.
    print('this is movie.name :',movie.name)    # movie.name → is the value of the name field in that particular movie.
    data = {
        'name' :movie.name,
        'description' : movie.description,
        'active' : movie.active,
    }
    return JsonResponse(data)
# ---------------------------------
# that is output
# {
#   "name": "Python vs Java",
#   "description": "description1",
#   "active": true
# }

# | Expression   | Output                           |
# | ------------ | -------------------------------- |
# | `movie`      | The full object (Movie instance) |
# | `movie.name` | Only the `name` attribute value  |
# ------------------------------------------------------------------------------------------------------------------------


# WE ARE DOING HERE
# COMPLEX QUERYSET -------> PYTHON DICT ------> JSON RESPONSE
# (Movie.objects.all())     (iterable)