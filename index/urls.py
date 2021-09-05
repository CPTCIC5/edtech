from django.urls import path
from . import views

app_name='index'

urlpatterns = [
    path('',views.index,name='index'),
    path('learn/',views.learn,name='learn'),
    path('contact/',views.contact,name='contact'),
    path('communities/',views.communities,name='communities'),
    path('solution/',views.solution,name='solution'),
    path('solution/<str:slug>/',views.paginated_solution,name='paginated solution')
]
