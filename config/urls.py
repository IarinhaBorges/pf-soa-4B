from rest_framework_nested import routers
from views import UserViewSet, PostViewSet
from django.contrib import admin
from django.urls import path, include

from api import views

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

router.register(r'users', views.UserViewSet)
router.register(r'todos', views.UserViewSet)
router.register(r'comments', views.UserViewSet)
router.register(r'posts', views.UserViewSet)

users_router = router.NestedSimpleRouter(router, r'users', lookup='user')
users_router.register(r'users', views.TodoViewSet, basename='users-todos')

todos_router = router.NestedSimpleRouter(router, r'users', lookup='user')
todos_router.register(r'todos', views.TodoViewSet, basename='users-todos')

# domains_router = routers.NestedSimpleRouter(router, r'domains', lookup='domain')
# domains_router.register(r'nameservers', NameserverViewSet, basename='domain-nameservers')


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path(r'', include(users_router.urls)),
   
]
