	
	
Behavior,Hobbie,Like,Dislike,FamilyMember,Friend,HealthcareProfessional,Assessment,HouseMates
	
def manage_yyyyyyyy(request, client_id):
	client = Client.objects.get(pk=client_id)
	ClientInlineFormSet = inlineformset_factory(Client, yyyyyyyy, exclude = [])
	if request.method == "POST":
		try:
			formset = ClientInlineFormSet(request.POST, request.FILES, instance=client)
		except ValidationError:
			formset = none
		if formset.is_valid():
			formset.save()
			# Do something. Should generally end with a redirect. For example:
			#return HttpResponseRedirect(client.get_absolute_url())
				
	else:
		try:
			formset = ClientInlineFormSet(instance=client)
		except ValidationError:
			formset = none
	return render(request, 'clients/manage_client.html', {'formset': formset})