from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Client, Behavior,Hobbie,Like,Dislike,FamilyMember,Friend,HealthcareProfessional,Assessment,HouseMates
from . import forms
from django.forms import inlineformset_factory


def home(request):
	return render(request, 'home.html')

def client_list(request):
	clients = Client.objects.all()
	return render(request, 'clients/client_list.html', {'clients':clients})
	
def client_detail(request, id):
	client = Client.objects.get(id = id)
	return render(request, 'clients/client_detail.html', {'client':client})
	
def fba_tool(request):
	return render(request, 'fba-tool.html')

def client_create(request):
	if request.POST:
		form = forms.ClientCreate(request.POST)
		if form.is_valid():
			new_client = form.save()
			
			return HttpResponseRedirect(reverse('manage-hobbie', args=[new_client.pk],))
	else:
		form = forms.ClientCreate()

	return render(request, 'clients/client_create.html', {'form':form})
	
	
def manage_Hobbie(request, client_id):
	client = Client.objects.get(pk=client_id)
	ClientInlineFormSet = inlineformset_factory(Client, Hobbie, exclude = [])
	if request.method == "POST":
		try:
			formset = ClientInlineFormSet(request.POST, request.FILES, instance=client)
		except ValidationError:
			formset = none
		if formset.is_valid():
			formset.save()
			return HttpResponseRedirect(reverse('manage-like', args=[client.pk],))
				
	else:
		try:
			formset = ClientInlineFormSet(instance=client)
		except ValidationError:
			formset = none
	return render(request, 'clients/manage_Hobbie.html', {'formset': formset})

	
	
def manage_Like(request, client_id):
	client = Client.objects.get(pk=client_id)
	ClientInlineFormSet = inlineformset_factory(Client, Like, exclude = [])
	if request.method == "POST":
		try:
			formset = ClientInlineFormSet(request.POST, request.FILES, instance=client)
		except ValidationError:
			formset = none
		if formset.is_valid():
			formset.save()
			return HttpResponseRedirect(reverse('manage-dislike', args=[client.pk],))
				
	else:
		try:
			formset = ClientInlineFormSet(instance=client)
		except ValidationError:
			formset = none
	return render(request, 'clients/manage_Like.html', {'formset': formset})
	
def manage_Dislike(request, client_id):
	client = Client.objects.get(pk=client_id)
	ClientInlineFormSet = inlineformset_factory(Client, Dislike, exclude = [])
	if request.method == "POST":
		try:
			formset = ClientInlineFormSet(request.POST, request.FILES, instance=client)
		except ValidationError:
			formset = none
		if formset.is_valid():
			formset.save()
			return HttpResponseRedirect(reverse('manage-familymember', args=[client.pk],))
				
	else:
		try:
			formset = ClientInlineFormSet(instance=client)
		except ValidationError:
			formset = none
	return render(request, 'clients/manage_Dislike.html', {'formset': formset})
	
def manage_FamilyMember(request, client_id):
	client = Client.objects.get(pk=client_id)
	ClientInlineFormSet = inlineformset_factory(Client, FamilyMember, exclude = [])
	if request.method == "POST":
		try:
			formset = ClientInlineFormSet(request.POST, request.FILES, instance=client)
		except ValidationError:
			formset = none
		if formset.is_valid():
			formset.save()
			return HttpResponseRedirect(reverse('manage-friend', args=[client.pk],))
				
	else:
		try:
			formset = ClientInlineFormSet(instance=client)
		except ValidationError:
			formset = none
	return render(request, 'clients/manage_FamilyMember.html', {'formset': formset})
	
def manage_Friend(request, client_id):
	client = Client.objects.get(pk=client_id)
	ClientInlineFormSet = inlineformset_factory(Client, Friend, exclude = [])
	if request.method == "POST":
		try:
			formset = ClientInlineFormSet(request.POST, request.FILES, instance=client)
		except ValidationError:
			formset = none
		if formset.is_valid():
			formset.save()
			return HttpResponseRedirect(reverse('manage-healthcareprofessional', args=[client.pk],))
				
	else:
		try:
			formset = ClientInlineFormSet(instance=client)
		except ValidationError:
			formset = none
	return render(request, 'clients/manage_Friend.html', {'formset': formset})

def manage_HealthcareProfessional(request, client_id):
	client = Client.objects.get(pk=client_id)
	ClientInlineFormSet = inlineformset_factory(Client, HealthcareProfessional, exclude = [])
	if request.method == "POST":
		try:
			formset = ClientInlineFormSet(request.POST, request.FILES, instance=client)
		except ValidationError:
			formset = none
		if formset.is_valid():
			formset.save()
			return HttpResponseRedirect(reverse('manage-assessment', args=[client.pk],))
				
	else:
		try:
			formset = ClientInlineFormSet(instance=client)
		except ValidationError:
			formset = none
	return render(request, 'clients/manage_HealthcareProfessional.html', {'formset': formset})
	
def manage_Assessment(request, client_id):
	client = Client.objects.get(pk=client_id)
	ClientInlineFormSet = inlineformset_factory(Client, Assessment, exclude = [])
	if request.method == "POST":
		try:
			formset = ClientInlineFormSet(request.POST, request.FILES, instance=client)
		except ValidationError:
			formset = none
		if formset.is_valid():
			formset.save()
			return HttpResponseRedirect(reverse('manage-housemates', args=[client.pk],))
				
	else:
		try:
			formset = ClientInlineFormSet(instance=client)
		except ValidationError:
			formset = none
	return render(request, 'clients/manage_Assessment.html', {'formset': formset})
	
def manage_HouseMates(request, client_id):
	client = Client.objects.get(pk=client_id)
	ClientInlineFormSet = inlineformset_factory(Client, HouseMates, exclude = [])
	if request.method == "POST":
		try:
			formset = ClientInlineFormSet(request.POST, request.FILES, instance=client)
		except ValidationError:
			formset = none
		if formset.is_valid():
			formset.save()
			return HttpResponseRedirect(reverse('manage-behavior', args=[client.pk],))
				
	else:
		try:
			formset = ClientInlineFormSet(instance=client)
		except ValidationError:
			formset = none
	return render(request, 'clients/manage_HouseMates.html', {'formset': formset})

def manage_Behavior(request, client_id):
	client = Client.objects.get(pk=client_id)
	ClientInlineFormSet = inlineformset_factory(Client, Behavior, exclude = [])
	if request.method == "POST":
		try:
			formset = ClientInlineFormSet(request.POST, request.FILES, instance=client)
		except ValidationError:
			formset = none
		if formset.is_valid():
			formset.save()
			return HttpResponseRedirect(reverse('client-detail', args=[client.pk],))
				
	else:
		try:
			formset = ClientInlineFormSet(instance=client)
		except ValidationError:
			formset = none
	return render(request, 'clients/manage_Behavior.html', {'formset': formset})
