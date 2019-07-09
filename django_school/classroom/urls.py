from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
	path('', TemplateView.as_view(template_name="classroom/timetable.html"), name='timetable'),
]