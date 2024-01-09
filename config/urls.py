from rest_framework_nested import routers
from api.views import UserViewSet, PostViewSet
from django.contrib import admin
from django.urls import path, include

from api import views

router = routers.SimpleRouter()

router.register(r'users', views.UserViewSet)
router.register(r'todos', views.TodoViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'posts', views.PostViewSet)

users_router = routers.NestedSimpleRouter(router, r'users', lookup='User')
users_router.register(r'users', views.UserViewSet)

todos_router = routers.NestedSimpleRouter(router, r'todos', lookup='Todo')
todos_router.register(r'todos', views.TodoViewSet)

posts_router = routers.NestedSimpleRouter(router, r'posts', lookup='Post')
posts_router.register(r'posts', views.PostViewSet)

comments_router = routers.NestedSimpleRouter(router, r'comments', lookup='Comment')
comments_router.register(r'comments', views.CommentViewSet)

# domains_router = routers.NestedSimpleRouter(router, r'domains', lookup='domain')
# domains_router.register(r'nameservers', NameserverViewSet, basename='domain-nameservers')


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path(r'', include(users_router.urls)),
   
]