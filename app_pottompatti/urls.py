from django.urls import include, path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.rolunk, name='rolunk'),
    re_path(r'rolunk', views.rolunk, name='rolunk'),
    re_path(r'kapcsolat', views.kapcsolat, name='kapcsolat'),
    re_path(r'uzletunk', views.sikeresmail, name='uzletunk'),
    re_path(r'kinalat', views.kinalat, name='kinalat'),
    re_path(r'eskuvo', views.eskuvo, name='eskuvo'),
    re_path(r'rendezvenyek', views.rendezvenyek, name='rendezvenyek'),
    re_path(r'esemenyek', views.esemenyek, name='esemenyek'),
    re_path(r'karrier', views.karrier, name='karrier'),
    ]