from django.urls import re_path as url

from portfo import views
urlpatterns = [
	
    url(r'^$'  , views.firstpage, name='firstpage'),
    url(r'^form'  , views.contact_me, name='contact_me'),
    url(r'^mywork'  , views.mywork, name='mywork'),
    url(r'^aboutus'  , views.aboutus, name='aboutus'),
    url('', views.PostList.as_view(), name='home'),
    url('<str:slug>/', views.post_Detail, name='post_Detail'),
    url(r'^index'  , views.index, name='index'),
    url(r'^postdetai'  , views.postdetai, name='postdetai'),

    url(r'^blog'  , views.blog, name='blog'),
   

    


    
]