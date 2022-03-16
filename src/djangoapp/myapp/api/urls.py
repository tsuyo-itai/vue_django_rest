from django.urls import path, re_path
from myapp.api import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# https://drf-yasg.readthedocs.io/en/stable/readme.html
schema_view = get_schema_view(
   openapi.Info(
      title="GrandMenu API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="test@test.jp"),
      license=openapi.License(name="TEST License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path( 'get_test_information/', views.TestInformation.as_view(), name='get_test_information'),
    re_path( 'swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),     # Swagger-Editor用 json or yaml形式 ダウンロード 
    path( 'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),   # Swagger-UI形式
    path( 'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),       # Redoc形式
]