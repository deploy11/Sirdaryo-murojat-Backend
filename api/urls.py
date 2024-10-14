from django.urls import path,include
from .views import *
from .user_views import *
from .api_views import *

urlpatterns = [
     path('api/', SorovApiView.as_view()),
     path('api/sorov-statistics/', SorovStatisticsView.as_view(), name='sorov_statistics'),
     path('get-user-id/', GetUserIdFromSession.as_view(), name='get_user_id'),
     # home
     path('hokim/',hokimpaneli,name='home'),
     path("hokim/1124424434354235412425/", hbarchasi, name="hammasi"),
     path('',hokimiyatPanel,name='hp'),
     # hps
     path('ars1/',filter_ariza_tur1,name='at1'),

     path('barchasis/',at,name='barchasi'),
     path('barchasi/<str:at>/',barcha,name='barchasisa'),
     path('bajarilgan_a_t/',br,name='br'),
     path('bajarilgan/<str:at>/',bajarilgan,name='bajarilgan'),
     path('md/',muddat,name='md'),
     path('bj/<str:at>/',bj,name='bj'),
     path('bjr/',bjr,name='bjr'),
     path('del/<int:id>',delete,name='del'),
     path('mudot/<int:id>',mudot,name='mudot'),
     path('bja/<int:pk>', updatebajar,name='bja'),
     path('sorov/<int:id>/',sorovid,name='sorovid'),
     path('user_ariza/<str:name>/',user_ariza,name='userariza'),
     # user views-
     path('login/',loginPage,name='login'),
     path('logout/',LogoutPage,name='logout'),
     path('saiduwa/',CreateBlog.as_view(),name='new'),
     path('rahmat/',ramat,name='rahmat'),
     path('fwa/',fuwr,name='usw'),
     path('searching/',searching,name='searching'),
     # hokim
     path('hokim/tashbiriktirlgan/',Tbir,name='tbir'),
     path('hokim/tashbiriktirilgan/',Tno,name='tno'),

     path('silk/', include('silk.urls', namespace='silk')),

]