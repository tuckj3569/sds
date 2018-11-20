from django.forms import ModelForm
from django import forms

from .models import Client,Behavior,Hobbie,Like,Dislike,FamilyMember,Friend,HealthcareProfessional,Assessment,HouseMates, FBATool

class ClientCreate(ModelForm):
    class Meta:
        model = Client
        fields = ['Client_FirstName', 'Client_LastName', 'Client_DOB', 'Client_Gender', 'Client_ServiceProvider','Client_CommunicationStyle',]


class FBATool(ModelForm):
	SETTING_CHOICES = (
		('Is in the community', 'Is in the community'),
		('Has recently been disciplined', 'Has recently been disciplined'),
		('Is engaged in an activity or task they dislike','Is engaged in an activity or task they dislike'),
		('Is eating', 'Is eating'),
		('Is working in a group', 'Is working in a group'),
		('Is working independently', 'Is working independently'),
		('Is playing', 'Is playing'),
		('Has had a change in routine', 'Has had a change in routine'),
		('Is attending a special event', 'Is attending a special event'),
		('Is in a specialist lesson', 'Is in a specialist lesson'),
		('Is transitioning between activities or settings', 'Is transitioning between activities or settings'),
		('Is unwell or tired', 'Is unwell or tired'),
		)
	
	ANTECEDENT_CHOICES = (
		('directs them to start or continue with a disliked task','directs them to start or continue with a disliked task'),
		('directs them to stop a liked task',  'directs them to stop a liked task'),
		('does not respond to their approach', 'does not respond to their approach'),
		('does not respond to their request', 'does not respond to their request'),
		('gives a physical prompt', 'gives a physical prompt'),
		('gives a verbal direction or request', 'gives a verbal direction or request'),
		('gives verbal praise', 'gives verbal praise'),
		('gives a verbal reminder', 'gives a verbal reminder'),
		('gives a verbal reprimand', 'gives a verbal reprimand'),
		('makes an unexpected noise or sound', 'makes an unexpected noise or sound'),
		('moves away', 'moves away'),
		('moves closer', 'moves closer'),
		('refuses a request', 'refuses a request'),
		)
		
	BEHAVIOUR_CHOICES = (
		('is off task and distracting other', 'is off task and distracting other'),
		('does not respond to the direction or request', 'does not respond to the direction or request'),
		('makes repetitive requests or sounds', 'makes repetitive requests or sounds'),
		('verbally refuses or rejects direction or request', 'verbally refuses or rejects direction or request'),
		('becomes verbally abusive', 'becomes verbally abusive'),
		('becomes physically aggressive', 'becomes physically aggressive'),
		('destroys property', 'destroys property'),
		)
		
		
	CONSEQUENCE_CHOICES = (
		('given a verbal direction to stop the behaviour','given a verbal direction to stop the behaviour'),
		('given more information or clarification of the direction or request','given more information or clarification of the direction or request'),
		('allowed to remain with preferred task or activity','allowed to remain with preferred task or activity'),
		('reminded of the rules and consequences','reminded of the rules and consequences'),
		('asked the Responsible Thinking questions','asked the Responsible Thinking questions'),
		('given a forced choice','given a forced choice'),
		('ignored','ignored'),
		('given attention by peers','given attention by peers'),
		('given 1:1 attention from adult','given 1:1 attention from adult'),
		('given reduced task demands','given reduced task demands'),
		('redirected to a different task or activity','redirected to a different task or activity'),
		('isolated','isolated'),
		('sent to another area','sent to another area'),
		)
	
	FUNTION_CHOICES = (
		('Escape/Avoid stimulation or sensation','Escape/Avoid stimulation or sensation'),
		('Escape/Avoid item or activity','Escape/Avoid item or activity'),
		('Escape/Avoid social situation','Escape/Avoid social situation'),
		('Obtain/Get stimulation or sensation','Obtain/Get stimulation or sensation'),
		('Obtain/Get item or activity','Obtain/Get item or activity'),
		('Obtain/Get social situation','Obtain/Get social situation'),
		)
 
	FBATool_Antecedent = forms.ChoiceField(choices=ANTECEDENT_CHOICES, widget=forms.RadioSelect())
	FBATool_Setting = forms.ChoiceField( choices=SETTING_CHOICES, widget=forms.RadioSelect())
	FBATool_Behaviour = forms.ChoiceField( choices=BEHAVIOUR_CHOICES, widget=forms.RadioSelect())
	FBATool_Consequence = forms.ChoiceField( choices=CONSEQUENCE_CHOICES, widget=forms.RadioSelect())
	FBATool_Function = forms.ChoiceField( choices=FUNTION_CHOICES, widget=forms.RadioSelect())
	class Meta:
		model = FBATool
		fields = ['FBATool_Title','FBATool_Setting','FBATool_Antecedent','FBATool_Behaviour','FBATool_Consequence','FBATool_Function','FBATool_Brief',]
		
	

#		'Client_Hobbies', 'Client_Likes', 'Client_Dislikes', 'Client_Family', 'Client_Friend',
#		'Client_Behaviors', 'Client_HealthcareProfessional', 'Client_HouseMates', 'Client_Assessments',	]
