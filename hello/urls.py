from django.urls import path
#. == current file
from . import views
urlpatterns = [
    path("",views.index, name = "index"), 
    #DAJIJI is the path that user will type in the url to get to the brain function.
    path("DAJIJI",views.brain, name = "brain"),
    path("DAVID",views.david, name = "david"),
    #string name is the name passed to the function. the first str: name could be any other name
    #that greet message just telling us what the funtion do i think.
    path("<str:name>",views.greet, name = "greet")
]