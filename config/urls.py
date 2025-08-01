from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from everycheese.cheeses.views import (
    CheeseListView, CheeseCreateView, CheeseDetailView,
    CheeseUpdateView, CheeseDeleteView, CheeseAddCustomView
)

urlpatterns = [
    path("cheeses/", include("everycheese.cheeses.urls", namespace="cheeses")),
    path("cheeses/add-custom/", CheeseAddCustomView.as_view(), name="cheese_add_custom"),
    path("cheeses/<int:pk>/delete/", CheeseDeleteView.as_view(), name="cheese_delete"),
    path("cheeses/<int:pk>/edit/", CheeseUpdateView.as_view(), name="cheese_update"),
    path("cheeses/<int:pk>/", CheeseDetailView.as_view(), name="cheese_detail"),
    path("cheeses/add/", CheeseCreateView.as_view(), name="cheese_add"),
    path(
        "cheeses/",
        CheeseListView.as_view(), 
        name="cheese_list"),
    path(
        "",
        TemplateView.as_view(template_name="pages/home.html"),
        name="home",
    ),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path(
        "users/",
        include("ejercicio_django.users.urls", namespace="users"),
    ),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls))
        ] + urlpatterns
