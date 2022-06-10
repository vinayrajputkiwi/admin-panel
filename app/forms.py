from django import forms
from .models import Register
class SignupForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,label='password')
    password1=forms.CharField(widget=forms.PasswordInput,label='confirm password')
    class Meta:
        model=Register
        fields=['full_name','email','password','password1']
    def clean(self):
        clean_data=super().clean()
        valname1=self.cleaned_data['password']
        valname2=self.cleaned_data['password1']
        if len(valname1)<8:
            raise forms.ValidationError('Password should be more than 8 characters')
        if len(valname2)<8:
            raise forms.ValidationError('Password should be more than 8 characters')
        if valname1!= valname2:
            raise forms.ValidationError('Password And Confirm Password Not Matched')
