from django.urls import path 

from .views import IndexView, DetailView

app_name = "blog"
urlpatterns = [
    path('blog/', IndexView.as_view(), name="blog-list"),
    path('blog/<int:id>/', DetailView.as_view(), name="detail"),
]
