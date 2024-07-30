import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from .views import HomeView

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Django Template Api Doc",
# # <<<<<<< Updated upstream
#         default_version="v1",
# # =======
# # <<<<<<< Updated upstream
#         default_version='v1',
# # =======
#         default_version="v1",   
# # >>>>>>> Stashed changes
# # >>>>>>> Stashed changes
#     ),
# )

urlpatterns = [
# <<<<<<< Updated upstream
    path("", HomeView.as_view()),
    path("admin/", admin.site.urls),
    path("api/v1/user/", include("user.urls")),
# =======
# <<<<<<< Updated upstream
    path('', HomeView.as_view()),
    # path('map/',include('map.urls.map_urls')),
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('user.urls')),
    
# =======
    path("", HomeView.as_view()),
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),
    path ("core/", include("core.urls")),
# >>>>>>> Stashed changes
# >>>>>>> Stashed changes
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
        # path(
        #     "api/docs/",
        #     schema_view.with_ui("swagger", cache_timeout=0),
        #     name="schema-swagger-ui",
        # ),
    ]
