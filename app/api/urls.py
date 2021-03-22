from rest_framework.routers import DefaultRouter

from .views import AccountViewSet, CourseViewSet, TokenViewSet

router = DefaultRouter()
router.register('accounts', AccountViewSet, 'user')
router.register('courses', CourseViewSet, 'course')
router.register('token', TokenViewSet, 'token')

urlpatterns = router.urls
