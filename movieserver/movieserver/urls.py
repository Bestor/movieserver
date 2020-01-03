from django.conf.urls import url, include
from django.contrib import admin
from models import Movies
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movies
        fields = ['title', 'format', 'length', 'year', 'rating']

# ViewSets define the view behavior.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
