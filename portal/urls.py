from django.urls import path
from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('fish_list/', views.fishList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)