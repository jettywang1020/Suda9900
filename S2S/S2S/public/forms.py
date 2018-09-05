from django import forms

class login_form(forms.Form):
	email = forms.EmailField(widget = forms.EmailInput(attrs = {'class':'form-control'}), required = True)
	password = forms.CharField(widget = forms.PasswordInput(attrs = {'class':'form-control'}),required = True)
	is_landlord = forms.BooleanField(widget = forms.CheckboxInput(attrs = {'class':'form-check-input'}) , required = False)

class signup_form(forms.Form):
	username = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={'class':'form-control'}),required = True)
	email = forms.EmailField(widget = forms.EmailInput(attrs = {'class':'form-control'}), required = True)
	password = forms.CharField(widget = forms.PasswordInput(attrs = {'class':'form-control'}), required = True)
	confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'class':'form-control'}), required = True)
	gender =  forms.ChoiceField(choices = (('M','Male'),('F','Female'),),  widget = forms.Select(attrs = {'class':'form-control'}), required = True)
	is_landlord = forms.BooleanField(widget=forms.CheckboxInput(attrs = {'class':'form-check-input'}), required = False)

class addhouse_form(forms.Form):
	name = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={'class':'form-control'}),required = True)
	address = forms.CharField(max_length = 200, widget = forms.TextInput(attrs={'class':'form-control'}),required = True)
	postcode = forms.CharField(max_length = 4, widget = forms.TextInput(attrs={'class':'form-control'}),required = True)
	price = forms.IntegerField(min_value = 1, widget = forms.NumberInput(attrs={'class':'form-control','placeholder':"200 (per night)"}),required = True)
	profile = forms.CharField(max_length = 5000, widget = forms.Textarea(attrs={'class':'form-control','rows':5}),required = False)
	maxguest = forms.IntegerField(min_value = 1, widget = forms.NumberInput(attrs={'class':'form-control','placeholder':'eg. 1'}),required = True)
	bed = forms.IntegerField(min_value = 0, widget = forms.NumberInput(attrs={'class':'form-control','placeholder':'eg. 1'}),required = True)
	bedroom = forms.IntegerField(min_value = 0, widget = forms.NumberInput(attrs={'class':'form-control','placeholder':'eg. 1'}),required = True)
	bathroom = forms.IntegerField(min_value = 0, widget = forms.NumberInput(attrs={'class':'form-control','placeholder':'eg. 1'}),required = True)
	park = forms.IntegerField(min_value = 0, widget = forms.NumberInput(attrs={'class':'form-control','placeholder':'eg. 1'}),required = True)
	tv = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class':'form-check-input'}),required = False)
	kitchen = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class':'form-check-input'}),required = False)
	washer = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class':'form-check-input'}),required = False)
	fridge = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class':'form-check-input'}),required = False)
	conditioner = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class':'form-check-input'}),required = False)
	wifi = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class':'form-check-input'}),required = False)
	studyroom = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class':'form-check-input'}),required = False)
	pool = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class':'form-check-input'}),required = False)
	rule = forms.CharField(max_length = 5000, widget = forms.Textarea(attrs={'class':'form-control','rows':5}),required = False)
	cancellation = forms.CharField(max_length = 5000, widget = forms.Textarea(attrs={'class':'form-control','rows':5}),required = False)
	extra = forms.CharField(max_length = 5000, widget = forms.Textarea(attrs={'class':'form-control','rows':5}),required = False)