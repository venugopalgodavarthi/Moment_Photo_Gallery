from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Page_Reg.models import categoriesmodel, imagesmodel


class signup_form(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(signup_form, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class categoriesform(forms.ModelForm):
    class Meta:
        model = categoriesmodel
        fields = '__all__'


class Imageform(forms.ModelForm):
    class Meta:
        model = imagesmodel
        # fields = '__all__'
        exclude = ('userid',)
    def save(self, commit:True):
        
        
        return super().save(commit)


class Selectcategoriesform(forms.Form):
    ctname = forms.ModelChoiceField(queryset=categoriesmodel.objects.all())
