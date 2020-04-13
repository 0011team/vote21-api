from django.contrib import admin
from django.urls import include, path, re_path
from vote21.schema import schema_view

from district.urls import urlpatterns as district_urlpatterns
from lawmaker.urls import urlpatterns as lawmaker_urlpatterns
from bills.urls import urlpatterns as bill_urlpatterns

urlpatterns = [
    re_path('^swagger/(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=0)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),

    path("admin/", admin.site.urls),
    # Enables the DRF browsable API page
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
] + district_urlpatterns + lawmaker_urlpatterns + bill_urlpatterns