from django.urls import include, path
from . import views as school_views
from django.views.generic import TemplateView

urlpatterns = [
	path('school/<code>/',school_views.school_view, name='school_view'),
	path('district/', school_views.districts, name='districts'),
	path('district/<int:district>/',school_views.sub_districts, name='sub_districts'),
	path('search/',school_views.search, name='search'),
]