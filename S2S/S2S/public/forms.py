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