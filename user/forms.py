from django import forms

class Registerform (forms.Form):

    username = forms.CharField(max_length=50,label="Kullanıcı Adı")
    password =forms.CharField(max_length=30,label="Parola",widget=forms.PasswordInput)
    confirm  =forms.CharField(max_length=50,label="Parola Doğrulama Alanı",widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm  = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm :
            raise forms.ValidationError("PAROLALAR AYNI DEĞİL !")

        values = {

                "username": username,
                "password": password}
        return values

class Loginform (forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola",widget=forms.PasswordInput)

    