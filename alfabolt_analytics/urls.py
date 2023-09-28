from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/marketing/',include('marketing.urls')),
    path("api/utilization/",include('engineer_utilization.urls')),
    path("api/sales/",include('sales.urls'))
]
