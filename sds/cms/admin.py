from django.contrib import admin
from .models import Client,Behavior,Hobbie,Like,Dislike,FamilyMember,Friend,HealthcareProfessional,Assessment,HouseMates
# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display=['Client_FirstName','Client_LastName']
	
@admin.register(Behavior)
class BehaviorAdmin(admin.ModelAdmin):
	list_display=['Behavior_Title']
	
@admin.register(Hobbie)
class HobbiesAdmin(admin.ModelAdmin):
	list_display=['Hobbie_Name']
	
@admin.register(Like)
class LikesAdmin(admin.ModelAdmin):
	list_display=['Likes_Name']
	
@admin.register(Dislike)
class DislikesAdmin(admin.ModelAdmin):
	list_display=['Dislikes_Name']
	
@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
	list_display=['FamilyMember_FirstName']
	
@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
	list_display=['Friend_FirstName']
	
@admin.register(HealthcareProfessional)
class HealthcareProfessionalAdmin(admin.ModelAdmin):
	list_display=['HealthcareProfessional_FirstName']

@admin.register(Assessment)
class Assessment(admin.ModelAdmin):
	pass

@admin.register(HouseMates)
class HouseMates(admin.ModelAdmin):
	list_display=['HouseMates_FirstName']
	
