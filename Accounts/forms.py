from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from Accounts.models import User
from django.contrib.auth import authenticate


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["email", 'fullname']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["email", "password", "date_of_birth", "is_active", "is_admin"]


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'type': "password", 'class': "form-control", 'id': "password", 'placeholder': "Your password",
        'required': "required", }))
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(attrs={
        'type': "password", 'class': "form-control", 'id': "password", 'placeholder': "Your password",
        'required': "required", }))

    class Meta:
        model = User
        fields = ['fullname', 'email']
        widgets = {
            'fullname': forms.TextInput(
                attrs={'type': "text", 'class': "form-control", 'id': "name", 'placeholder': "Your Name",
                       'required': "required"}),
            'email': forms.EmailInput(
                attrs={'type': "email", 'class': "form-control", 'id': "email", 'placeholder': "Your Email",
                       'required': "required"})
        }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords dose not match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.CharField(max_length=60, widget=forms.EmailInput(
        attrs={'type': "text", 'class': "form-control", 'id': "name", 'placeholder': "Your email",
               'required': "required"}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={'type': "password", 'class': "form-control", 'id': "email", 'placeholder': "Your password",
               'required': "required"}))
    confirmpassword = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={'type': "password", 'class': "form-control", 'id': "password", 'placeholder': "confirm password",
               'required': "required"}))

    def clean(self):
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')
        user = authenticate(email=email, password=password)
        if user is None:
            raise ValidationError('User or Password is wrong')


    def clean_confirmpassword(self):
        password = self.cleaned_data.get('password')
        confirmpassword = self.cleaned_data.get('confirmpassword')
        if confirmpassword != password:
            raise ValidationError('Passwords are Not same', code='001')
        else:
            return confirmpassword
    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            user = User.objects.get(email=email)
            return email
        except:
            raise ValidationError('User dose not exist', code="002")


