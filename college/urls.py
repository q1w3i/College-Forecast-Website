from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^seventeen/$', views.Seventeen.as_view()),
    # url(r'^eighteen/$', views.Eighteen.as_view()),
    # url(r'^nineteen/$', views.Nineteen.as_view()),
    # url(r'^twenty/$', views.Twenty.as_view()),
    # url(r'^eighteen/(?P<pk>\d+)/$', views.Eighteen.as_view()),
    # url(r'^nineteen/(?P<pk>\d+)/$', views.Nineteen.as_view()),
    # url(r'^twenty/(?P<pk>\d+)/$', views.Twenty.as_view()),
]
from  rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register(r'seventeen',views.Seventeen,basename="waylon")
urlpatterns += router.urls
router.register('eighteen',views.Eighteen,basename="waylon")
urlpatterns += router.urls
router.register('nineteen',views.Nineteen,basename="waylon")
urlpatterns += router.urls
router.register('twenty',views.Twenty,basename="waylon")
urlpatterns += router.urls
