from django.conf.urls import patterns, url
from transport import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^index/$', views.index, name='index'),
	url(r'^download/$', views.download, name='download'),
	url(r'^about/$', views.about, name='about'),
	url(r'^i/ps(.+)/$', views.ind_select, name='ind_selects'),
	url(r'^i/info/$', views.info, name='info'),
	url(r'^i/pwd/$', views.pwd, name='pwd'),
	url(r'^individual/$', views.individual, name='individual'),
	url(r'^i/list/$', views.orderlist, name='orderlist'),
	url(r'^i/detail/id(.+)$', views.orderdetail, name='orderdetail'),
	url(r'^i/publish/$', views.orderpublish, name='orderpublish'),
	url(r'^i/receive/id(.+)s(.+)$', views.orderreceive, name='orderreceive'),
	url(r'^i/confirm/id(.+)$', views.offer_confirm, name='offer_confirm'),
	url(r'^login/$', views.login, name='login'),
	url(r'^question/$', views.question, name='question'),
	url(r'^reg/$', views.reg, name='reg'),
	url(r'^reg_validator/$', views.reg_validator, name='reg_validator'),
	url(r'^conf_mail/$', views.conf_mail, name='conf_mail'),
	url(r'^sendMail/$', views.send_mail, name='send_mail'),
	url(r'^dreg/$',views.dreg,name='dreg'),
	url(r'^logout/$',views.logout,name='logout'),
	url(r'^f_pwd/$',views.f_pwd_1,name='f_pwd_1'),
	url(r'^f_pwd_2/$',views.f_pwd_2,name='f_pwd_2'),
	url(r'^f_pwd_3/$',views.f_pwd_3,name='f_pwd_3'),
	url(r'^f_pwd_code/$',views.f_pwd_code,name='f_pwd_code'),
	url(r'^order_column/$',views.order_column,name='order_column'),
	url(r'^order_pie/$',views.order_pie,name='order_pie'),

	url(r'^app/reg/$',views.driver_reg,name='driver_reg'),
	url(r'^app/login/$',views.driver_login,name='driver_login'),
	url(r'^app/order/$',views.get_order,name='get_order'),
	url(r'^app/order_search/$',views.get_order_search,name='get_order_search'),
	url(r'^app/detail/$',views.get_order_detail,name='get_order_detail'),
	url(r'^app/pwd/$',views.driver_pwd,name='driver_pwd'),
	url(r'^app/update/$',views.driver_update,name='driver_update'),
	url(r'^app/offer/$',views.driver_offer,name='driver_offer'),
	url(r'^app/order_list/$',views.get_order_offer,name='get_order_offer'),
	url(r'^app/location/$',views.set_location,name='set_location'),
	url(r'^app/order_finish/$',views.set_order_finish,name='set_order_finish'),
	)