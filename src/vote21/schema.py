from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title='vote 21 API',
        default_version='v1',
        description='API documentation for vote 21',
        contact=openapi.Contact(email="team0011kr@gmail.com")
    ),
    validators=['flex'],
    public=True,
    authentication_classes=(),
    permission_classes=(AllowAny,)
)
