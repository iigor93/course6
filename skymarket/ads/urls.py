from django.urls import include, path
from rest_framework import routers

from ads import views

from rest_framework.routers import Route, DynamicRoute, SimpleRouter


router = routers.SimpleRouter()
router.register('', views.AdModelView)


router_me = routers.SimpleRouter()
router_me.register('me', views.AdMeModelView, basename='ad')

router_comment = routers.SimpleRouter()
router_comment.register('(?P<aid>\d+)/comment', views.CommentModelView, basename='comment')

urlpatterns = [

]


urlpatterns += router_comment.urls
urlpatterns += router_me.urls
urlpatterns += router.urls
