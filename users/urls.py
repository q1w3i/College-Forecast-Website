from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.Login.as_view()),
    # url(r'^users/$',views.Users.as_view()),
    # url(r'^users/(?P<user_id>\d+)/$',views.UsersDetail.as_view()),
    # url(r'^users_all/$',views.UsersAll.as_view({'get': 'list',"post":"create"})),
    # url(r'^users_all/(?P<pk>\d+)/$',views.UsersAll.as_view({'get': 'retrieve','put':'update','delete':'destroy'})),
    # url(r'^users_all/s/(?P<pk>\d+)/$',views.UsersAll.as_view({'put':'update_user'})),
]
from rest_framework.routers import SimpleRouter,DefaultRouter
router = DefaultRouter()
router.register('users',views.UsersAll,basename="waylon")
urlpatterns += router.urls
print(urlpatterns)