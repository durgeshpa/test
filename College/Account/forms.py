from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _
from Account.models import Profile


class  SignUpForm(UserCreationForm):
	username=forms.CharField(max_length=30,widget=forms.TextInput(attrs={ 'placeholder':" Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only." }))
	first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}) )
	last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control',}) )
	email = forms.EmailField(max_length=150,label=_('email'),widget=forms.TextInput(attrs={'class':'form-control','placeholder':'example: xyz@gmail.com'}) )
	password1 = forms.CharField(label=_("password"),widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':' password atleast 8 characters  Letters, digits and @/./+/-/_ only.'}))
	password2 = forms.CharField(label=_("conform password"),widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confiorm Password'}))
	

	class Meta:
		model = User
		fields='__all__'
		fields = ('username', 'first_name', 'last_name',
				  'email', 'password1', 'password2',)
		#labels={'username':_("username"),'first_name':_(""),'last_name':_(""),'email':_(""),'password2':_(""),'password1':_("")}
	

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	image=forms.FileField(widget=forms.FileInput(attrs={}))


	class Meta:
		model = Profile
		fields = ['image']
		labels={'image':_(''),}
		#attrs=_('')
