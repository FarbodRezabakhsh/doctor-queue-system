from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("doctor.urls")),
    path('comment/', include("comment.urls")),
    path('accounts/', include("accounts.urls")),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
