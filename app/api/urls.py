from rest_framework.routers import DefaultRouter

from .views import AccountViewSet, TokenViewSet

router = DefaultRouter()
router.register('accounts', AccountViewSet, 'user')
router.register('token', TokenViewSet, 'token')

urlpatterns = router.urls
