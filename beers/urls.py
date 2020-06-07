from django.conf.urls import url

from beers.views import first_view

urlpatterns = [

    url('^$', first_view, name='first-view'),

]