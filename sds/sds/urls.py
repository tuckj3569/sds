
from django.contrib import admin
from django.urls import path, re_path
from cms import views

urlpatterns = [
	path('admin/', admin.site.urls),
	re_path(r'^$', views.home),
	
	
	path('create/', views.client_create),
	path('client-list/', views.client_list),
	path('fba-tool/', views.fba_tool),
	re_path(r'^client/(\d+)/$', views.client_detail, name='client-detail'),
	re_path(r'^client/(\d+)/hobbie/', views.manage_Hobbie, name='manage-hobbie'),
	re_path(r'^client/(\d+)/like/', views.manage_Like, name='manage-like'),
	re_path(r'^client/(\d+)/dislike/', views.manage_Dislike, name='manage-dislike'),
	re_path(r'^client/(\d+)/familymember/', views.manage_FamilyMember, name='manage-familymember'),
	re_path(r'^client/(\d+)/friend/', views.manage_Friend, name='manage-friend'),
	re_path(r'^client/(\d+)/healthcareprofessional/', views.manage_HealthcareProfessional, name='manage-healthcareprofessional'),
	re_path(r'^client/(\d+)/assessment/', views.manage_Assessment, name='manage-assessment'),
	re_path(r'^client/(\d+)/housemates/', views.manage_HouseMates, name='manage-housemates'),
	re_path(r'^client/(\d+)/behavior/', views.manage_Behavior, name='manage-behavior'),
	
]