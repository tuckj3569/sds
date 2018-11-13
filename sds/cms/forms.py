from django.forms import ModelForm

from .models import Client,Behavior,Hobbie,Like,Dislike,FamilyMember,Friend,HealthcareProfessional,Assessment,HouseMates

class ClientCreate(ModelForm):
    class Meta:
        model = Client
        fields = ['Client_FirstName', 'Client_LastName', 'Client_DOB', 'Client_Gender', 'Client_ServiceProvider','Client_CommunicationStyle',]


class HobbieCreate(ModelForm):
	class Meta:
		model = Hobbie
		fields = ['Hobbie_Name','Hobbie_frequency','Hobbie_location']

		
	

#		'Client_Hobbies', 'Client_Likes', 'Client_Dislikes', 'Client_Family', 'Client_Friend',
#		'Client_Behaviors', 'Client_HealthcareProfessional', 'Client_HouseMates', 'Client_Assessments',	]