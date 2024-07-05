from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("doctor.urls")),
    path('commit/', include("commit.urls")),
    path('accounts/', include("user.urls")),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
