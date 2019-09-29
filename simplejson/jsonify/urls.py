from django.conf.urls import url

# internal imports
from .views import IndexView

urlpatterns = [
            url(r'$', IndexView.as_view(), name='index')
]
