from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^signup/',views.signup,name='signup'),
    url(r'^search',views.search,name='search'),
    url(r'^project/',views.projects,name='projects'),
    # url(r'^profile/(\d+)',views.profile,name='profile'),
    url(r'^update_profile/',views.update_profile,name='update_profile'),
    url(r'^comment/(\d+)/$',views.comment,name='comment'),
    url(r'rate/(\d+)', views.rate, name='rate'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/project/$', views.ProjectsList.as_view()),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)