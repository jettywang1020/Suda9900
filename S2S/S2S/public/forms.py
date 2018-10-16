from django import forms

class login_form(forms.Form):
	email = forms.EmailField(widget = forms.EmailInput(attrs = {'class':'form-control'}), required = True)
	password = forms.CharField(max_length=256, widget = forms.PasswordInput(attrs = {'class':'form-control'}),required = True)
	is_landlord = forms.BooleanField(widget = forms.CheckboxInput(attrs = {'class':'form-check-input'}) , required = False)

class signup_form(forms.Form):
	username = forms.CharField(max_length = 64, widget = forms.TextInput(attrs={'class':'form-control'}),required = True)
	email = forms.EmailField(widget = forms.EmailInput(attrs = {'class':'form-control'}), required = True)
	password = forms.CharField(max_length=256, widget = forms.PasswordInput(attrs = {'class':'form-control'}), required = True)
	confirm_password = forms.CharField(max_length=256, widget = forms.PasswordInput(attrs = {'class':'form-control'}), required = True)
	gender =  forms.ChoiceField(choices = (('M','Male'),('F','Female'),),  widget = forms.Select(attrs = {'class':'form-control'}), required = True)
	is_landlord = forms.BooleanField(widget=forms.CheckboxInput(attrs = {'class':'form-check-input'}), required = False)

class addhouse_form(forms.Form):
	name = forms.CharField(max_length = 256, widget = forms.TextInput(attrs={'class':'form-control'}),required = True)
	address = forms.CharField(max_length = 256, widget = forms.TextInput(attrs={'class':'form-control'}),required = True)
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

class addimage_form(forms.Form):
	image = forms.ImageField(widget = forms.ClearableFileInput(attrs={'class':'form-control','multiple': True}),required = True)

class profile_form(forms.Form):
	username = forms.CharField(max_length = 64, widget = forms.TextInput(attrs={'class':'form-control'}),required = True)
	firstname = forms.CharField(max_length = 64, widget = forms.TextInput(attrs={'class':'form-control'}),required = False)
	lastname = forms.CharField(max_length = 64, widget = forms.TextInput(attrs={'class':'form-control'}),required = False)
	email = forms.EmailField(widget = forms.EmailInput(attrs = {'class':'form-control'}), required = True)
	gender = forms.ChoiceField(widget = forms.Select(attrs = {'class':'form-control'}),choices = ([('M','Male'), ('F','Female'), ]), initial='1', required = False)
	phone = forms.CharField(max_length = 128, widget = forms.TextInput(attrs={'class':'form-control','placeholder':'61-00000000'}),required = False)
	profile = forms.CharField(max_length = 5000, widget = forms.Textarea(attrs={'class':'form-control','rows':5}),required = False)
	dob = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={'class':'form-control', 'data-provide':'datepicker', 'data-date-format':'dd/mm/yyyy', 'placeholder':'dd/mm/yyyy'}),required = False)
	profile = forms.CharField(max_length = 5000, widget = forms.Textarea(attrs={'class':'form-control','rows':5}),required = False)

class upload_photo_form(forms.Form):
	photo = forms.ImageField(widget = forms.ClearableFileInput(attrs={'class':'form-control','multiple': False}),required = True)

class tcomment_form(forms.Form):
	reputation = forms.IntegerField(min_value = 0, max_value = 5, widget = forms.NumberInput(attrs={'class':"col-sm-3",'placeholder':'eg. 1'}),required = False)

class hcomment_form(forms.Form):
	accuracy = forms.IntegerField(min_value = 0, max_value = 5, widget = forms.NumberInput(attrs={'class':"col-sm-3",'placeholder':'eg. 1'}),required = False)
	communication = forms.IntegerField(min_value = 0, max_value = 5, widget = forms.NumberInput(attrs={'class':"col-sm-3",'placeholder':'eg. 1'}),required = False)
	cleanliness = forms.IntegerField(min_value = 0, max_value = 5, widget = forms.NumberInput(attrs={'class':"col-sm-3",'placeholder':'eg. 1'}),required = False)
	location = forms.IntegerField(min_value = 0, max_value = 5, widget = forms.NumberInput(attrs={'class':"col-sm-3",'placeholder':'eg. 1'}),required = False)
	checkin = forms.IntegerField(min_value = 0, max_value = 5, widget = forms.NumberInput(attrs={'class':"col-sm-3",'placeholder':'eg. 1'}),required = False)
	value = forms.IntegerField(min_value = 0, max_value = 5, widget = forms.NumberInput(attrs={'class':"col-sm-3",'placeholder':'eg. 1'}),required = False)
	comment = forms.CharField(max_length = 5000, widget = forms.Textarea(attrs={'class':'form-control','rows':5}),required = False)

class adv_search_form(forms.Form):
	keyword = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={'class':'form-control'}),required = True)
	check_in = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={'class':'form-control', 'data-provide':'datepicker', 'data-date-format':'dd/mm/yyyy', 'placeholder':'dd/mm/yyyy', 'id':'checkin'}),required = True)
	check_out = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={'class':'form-control', 'data-provide':'datepicker', 'data-date-format':'dd/mm/yyyy', 'placeholder':'dd/mm/yyyy', 'id':'checkout'}),required = True)
	adult = forms.IntegerField(min_value = 0, widget = forms.NumberInput(attrs={'class':'form-control','value':'1'}),required = True)
	children = forms.IntegerField(min_value = 0, widget = forms.NumberInput(attrs={'class':'form-control','value':'0'}),required = True)


class post_form(forms.Form):
	title = forms.CharField(max_length = 256, widget = forms.TextInput(attrs={'class':'form-control col-10'}),required = True)
	area = forms.CharField(max_length = 128, widget = forms.TextInput(attrs={'class':'form-control col-10','placeholder':'eg. Kingsford'}),required = True)
	no_of_rooms =  forms.ChoiceField(choices = (('All','All'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),),  widget = forms.Select(attrs = {'class':'form-control col-3'}), required = True)
	rent_type =  forms.ChoiceField(choices = (('All','All'),('S','Share'),('W','Whole house'),),  widget = forms.Select(attrs = {'class':'form-control col-3'}), required = True)
	description = forms.CharField(max_length = 5000, widget = forms.Textarea(attrs={'class':'form-control col-10','rows':5}),required = False)
	name = forms.CharField(max_length = 256, widget = forms.TextInput(attrs={'class':'form-control col-10'}),required = True)
	email = forms.EmailField(widget = forms.EmailInput(attrs = {'class':'form-control col-10'}), required = True)
	mobile = forms.CharField(max_length = 256, widget = forms.TextInput(attrs={'class':'form-control col-10'}),required = False)

