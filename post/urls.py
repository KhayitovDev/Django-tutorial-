from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r"posts", views.PostViewSet)



urlpatterns = [

    path("", include(router.urls))
    # path("posts/", views.post_list), 
    # path("posts/<int:pk>/", views.post_detail)
    
    # path("posts/", views.PostListCreateAPIView.as_view()),
    # path("posts/<int:pk>/", views.PostRetrieveUpdateDestroyView.as_view())
    
    
]
