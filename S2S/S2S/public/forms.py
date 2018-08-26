from django import forms

class login_form(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),required=True)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
	is_landlord = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}),required=False)

class signup_form(forms.Form):
	username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
	first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
	last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),required=True)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
	is_landlord = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}),required=False)