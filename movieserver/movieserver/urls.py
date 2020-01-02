from django.conf.urls import url, include
from django.contrib import admin
from movieserver.resources import MovieResource
movie_resource = MovieResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(movie_resource.urls)),
]
