import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView
from showroom.yasg import urlpatterns as doc_urls

from showroom.views import CarViewSet, CarManufacturerViewSet, CustomerViewSet, SupplierViewSet, \
    ShowroomViewSet

router = routers.DefaultRouter()
router.register(r'car', CarViewSet)
router.register(r'manufacturer', CarManufacturerViewSet)
router.register(r'customer', CustomerViewSet)
# router.register(r'user', UserViewSet)
router.register(r'supplier', SupplierViewSet)
router.register(r'showroom', ShowroomViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('__debug__/', include(debug_toolbar.urls)),

]

urlpatterns += doc_urls