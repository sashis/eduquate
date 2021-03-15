from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from courses.views import IndexPageView
from contacts.views import ContactView

urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('courses/', include('courses.urls', namespace='courses')),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('api-auth/', include('rest_framework.urls')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=settings.DEBUG))),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns.extend(
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )

    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
