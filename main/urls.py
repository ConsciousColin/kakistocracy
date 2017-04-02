from django.conf.urls import url

#from . import views
from main.views import IndexView, PostView, AboutView, NetworkJSON, NetworkView, RidesharingMap

urlpatterns = [
    url(r'^$', IndexView.as_view(), name ='index_view'),
    url(r'^about', AboutView.as_view(), name = 'about_view'),
    url(r'^(?P<slug>[\w\-]+)$',PostView.as_view(), name = 'post_view'),
    url(r'^graphs/network_json', NetworkJSON.as_view(), name ='json_view'),
    url(r'^graphs/network', NetworkView.as_view(), name ='network_view'),
    url(r'^graphs/ridesharing', RidesharingMap.as_view(), name ='rideshare_view'),
]