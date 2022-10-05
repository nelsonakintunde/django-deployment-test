from django.conf.urls import url
from basicapp import views

appname = 'basicapp'

urlpatterns=[
    url('relative/',views.relative,name='relative'),
    url('new/',views.new,name='new'),
]
