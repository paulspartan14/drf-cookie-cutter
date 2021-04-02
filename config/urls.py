from django.contrib import admin
from django.urls import path, include

# Documentation dependecies
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url

# DRF Routes
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView

###from aaaimx.views import GroupView, UserViewSet

# Documentation Schema
schema_view = get_schema_view(
   openapi.Info(
      title="DRF AAAIMX API",
      default_version='v1',
      description="Test description",
      contact=openapi.Contact(email="support@aaaimx.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

# register userViewSet on routerDefault
###router = routers.DefaultRouter()
###router.register(r'users', UserViewSet)

auth_urlpatterns = [
    ###path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    ###path('groups/', GroupView. as_view()),
]

api_urlpatterns = [
    ###path('', include(router.urls)),
    ###path('auth/', include(auth_urlpatterns)),

    # documentation urls
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
]

