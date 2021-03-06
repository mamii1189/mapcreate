from unicodedata import name
from django.contrib import admin
from django.urls import path, include
# from testRoot.views import index, list_play, list_eat, test, list_all, test_direction, rootDisplay, test1, test2, test3, test4, test5, user, save, detail, like, topPage, topPage1
from testRoot.views import index, test_direction, test1, test2, user, detail, like, topPage, topPage1
# from testRoot.views import list_play, list_eat, test, list_all, rootDisplay, test3, test4, test5, save
from django.views.generic import RedirectView
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='topPage/')),
    path('testRoot/', index, name='index'),
    path('testRoot/test_direction', test_direction, name='test_direction'),
    path('testRoot/test1', test1, name='test1'),
    path('testRoot/test2', test2, name='test2'),
    path('user/<int:id>', user, name='user'),
    path('testRoot/<int:id>/detail', detail, name='detail'),
    path('testRoot/<int:id>/like', like, name='like'),
    path('testRoot/topPage', topPage, name='topPage'),
    path('topPage/', topPage1, name='topPage1'),
    # path('testRoot/list_play', list_play, name='list_play'),
    # path('testRoot/list_eat', list_eat, name='list_eat'),
    # path('testRoot/list_all', list_all, name='list_all'),
    # path('testRoot/test', test, name='test'),
    # path('testRoot/test3', test3, name='test3'),
    # path('testRoot/test4', test4, name='test4'),
    # path('testRoot/test5', test5, name='test5'),
    # path('testRoot/save', save, name='save'),
    # path('testRoot/rootDisplay', rootDisplay, name='rootDisplay'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)