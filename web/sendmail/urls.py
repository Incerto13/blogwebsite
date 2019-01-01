
from django.conf.urls import url

from . import views

app_name = 'sendmail'
urlpatterns = [
    url(r'^email/$', views.send_email, name='email'),
    url(r'^success/$', views.email_success, name='success'),
]