from django.db import models

# Create your models here.
class Client(models.Model):
	Client_FirstName = models.CharField(max_length=30, blank=True)
	Client_LastName = models.CharField(max_length=30, blank=True)
	Client_DOB = models.DateField(auto_now=False, auto_now_add=False)
	GENDER_CHOICES = (('m', 'Male'),('f', 'Female'),('o', 'Other'))
	Client_Gender = models.CharField(max_length=1, blank=True, choices=GENDER_CHOICES)
	Client_ServiceProvider = models.CharField(max_length=30, blank=True)
	Client_AdditionalServiceProvider = models.CharField(max_length=30, blank=True)
	COMMUNICATIONSTYLES_CHOICES = (('NV', 'Non-verbal'),('V', 'Verbal'),)
	Client_CommunicationStyle = models.CharField(max_length=2, blank=True, choices=COMMUNICATIONSTYLES_CHOICES)
	

		
	
	# Client_Hobbies = models.ManyToManyField(Hobbie,related_name='+', blank=True)
	# Client_Likes = models.ManyToManyField(Like,related_name='+', blank=True)
	# Client_Dislikes = models.ManyToManyField(Dislike,related_name='+', blank=True)
	# Client_Family = models.ManyToManyField(FamilyMember,related_name='+', blank=True)
	# Client_Friend = models.ManyToManyField(Friend,related_name='+', blank=True)
	# 
	# Client_Behaviors = models.ManyToManyField(Behavior,related_name='+', blank=True)
	# Client_HealthcareProfessional = models.ManyToManyField(HealthcareProfessional,related_name='+', blank=True)
	# Client_HouseMates = models.ManyToManyField(HouseMates,related_name='+', blank=True)
	# Client_Assessments = models.ManyToManyField(Assessment,related_name='+', blank=True)
	
	def __str__(self):
		return '%s %s' % (self.Client_FirstName, self.Client_LastName)
		

class Behavior(models.Model):
	Behavior_Client = models.ForeignKey('Client', on_delete=models.CASCADE,related_name="Client_Behavior")
	
	FUNCTION_CHOICES = (('SA', 'Social Attention'),('TA', 'Tangibles or Activities'),('EA', 'Escape or Avoidance'),('SS', 'Sensory Stimulation'))
	HARMTYPE_CHOICES = (('verbal', 'verbal'),('Physical', 'Physical'))
	HARMSUBTYPEPHYSICAL_CHOICES = (('punching', 'punching'),('kicking', 'kicking'),('slapping', 'slapping'),('shaking', 'shaking'),('pushing', 'pushing'))
	HARMTYPEVERBAL_CHOICES = (('Threatening', 'Threatening'),('Name calling', 'Name calling'),('Ordering', 'Ordering'),('Denial', 'Denial'),('Abusive anger', 'Abusive anger'))
	
	HARMLOCATION_CHOICES = (('SA', 'Social Attention'),('TA', 'Tangibles or Activities'),('EA', 'Escape or Avoidance'),('SS', 'Sensory Stimulation'))
	
	Behavior_Title = models.CharField(max_length=30, blank=True)
	Behavior_Function = models.CharField(max_length=2, blank=True, choices=FUNCTION_CHOICES)
	Behavior_Antecedent = models.CharField(max_length=30, blank=True)
	Behavior_Consequence  = models.CharField(max_length=30, blank=True)
	Behavior_Description  = models.TextField(blank=True)
	Behavior_HarmToSelf = models.BooleanField(default=True)
	Behavior_HarmToSelfTypePhysical = models.CharField(max_length=10, blank=True, choices=HARMSUBTYPEPHYSICAL_CHOICES)
	Behavior_HarmToSelfTypePhysical = models.CharField(max_length=10, blank=True, choices=HARMTYPEVERBAL_CHOICES)
	
	Behavior_HarmToOthers = models.BooleanField(default=True)
	Behavior_HarmToOthersTypePhysical = models.CharField(max_length=10, blank=True, choices=HARMSUBTYPEPHYSICAL_CHOICES)
	Behavior_HarmToOthersTypePhysical = models.CharField(max_length=10, blank=True, choices=HARMTYPEVERBAL_CHOICES)

	def __str__(self):
		return '%s' % (self.Behavior_Title)
	
class Hobbie(models.Model):
	Hobbie_Client = models.ForeignKey('Client', on_delete=models.CASCADE,related_name="Client_Hobbie")
	Hobbie_Name = models.CharField(max_length=30, blank=True)
	Hobbie_frequency = models.IntegerField( blank=True)
	Hobbie_location = models.CharField(max_length=30, blank=True)
	
	def __str__(self):
		return '%s' % (self.Hobbie_Name)

class Like(models.Model):
	Like_Client = models.ForeignKey('Client', on_delete=models.CASCADE,related_name="Client_Like")
	Likes_Name = models.CharField(max_length=30, blank=True)
	def __str__(self):
		return '%s' % (self.Likes_Name)
	
class Dislike(models.Model):
	Dislike_Client = models.ForeignKey('Client', on_delete=models.CASCADE,related_name="Client_Dislike")
	Dislikes_Name = models.CharField(max_length=30, blank=True)
	
	def __str__(self):
		return '%s' % (self.Dislikes_Name)

class FamilyMember(models.Model):
	FamilyMember_Client = models.ForeignKey('Client', on_delete=models.CASCADE,related_name="Client_FamilyMember")
	FamilyMember_FirstName = models.CharField(max_length=30, blank=True)
	FamilyMember_LastName = models.CharField(max_length=30, blank=True)
	RELATIONSHIP_CHOICE = (('mother', 'Mum'),('father', 'Dad'),('brother', 'Brother'),('sister', 'Sister'),('uncle', 'Uncle'),('auntie', 'Auntie'),('nephew', 'Nephew'),('son', 'Son'),('daughter', 'Daughter'))
	FamilyMember_Relationship = models.CharField(max_length=30, blank=True, choices= RELATIONSHIP_CHOICE)
	FamilyMember_ContactNumber = models.IntegerField(blank=True)
	
	def __str__(self):
		return '%s %s' % (self.FamilyMember_FirstName, "(" + self.FamilyMember_Relationship + ")")

class Friend(models.Model):
	Friend_Client = models.ForeignKey('Client', on_delete=models.CASCADE,related_name="Client_Friend")
	Friend_FirstName = models.CharField(max_length=30, blank=True)
	Friend_LastName = models.CharField(max_length=30, blank=True)
	Friend_ContactNumber = models.IntegerField(blank=True)
	def __str__(self):
		return '%s %s' % (self.Friend_FirstName, '(friend)')

class Assessment(models.Model):
	Assessment = models.ForeignKey('Client', on_delete=models.CASCADE,related_name="Client_Assessment")
	Assessment_type = models.CharField(max_length=30, blank=True)
	Assessment_Assessor = models.ForeignKey('HealthcareProfessional',on_delete=models.CASCADE)
	Assessment_Date = models.DateField(auto_now=False, auto_now_add=False)
	Assessment_Brief  = models.TextField(blank=True)
	
	def __str__(self):
		return '%s' % (self.Assessment_type)
		
class HealthcareProfessional(models.Model):
	HealthcareProfessional = models.ForeignKey('Client', on_delete=models.CASCADE,related_name="Client_HealthcareProfessional")
	HealthcareProfessional_FirstName = models.CharField(max_length=30, blank=True)
	HealthcareProfessional_LastName = models.CharField(max_length=30, blank=True)
	HealthcareProfessional_ContactNumber = models.IntegerField(blank=True)
	HealthcareProfessional_Profession = models.CharField(max_length=30, blank=True)
	
	def __str__(self):
		return '%s %s' % (self.HealthcareProfessional_FirstName, self.HealthcareProfessional_LastName)

class HouseMates(models.Model):
	HouseMates = models.ForeignKey('Client', on_delete=models.CASCADE,related_name="Client_HouseMates")
	HouseMates_FirstName = models.CharField(max_length=30, blank=True)
	HouseMates_LastName = models.CharField(max_length=30, blank=True)
	
	def __str__(self):
		return '%s %s' % (self.HouseMates_FirstName, self.HouseMates_LastName)




		
		

		
