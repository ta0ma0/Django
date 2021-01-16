from authapp.forms import forms
from authapp.models import ShopUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from firstapp.models import ProductCategory, Product


class AdminShopUserCreateForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = (
            'username', 'first_name', 'last_name', 'is_superuser',
            'password1', 'password2', 'email', 'age', 'avatar'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Пользователь слишком молод!")
        return data


class AdminShopUserUpdateForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = (
            'username', 'first_name', 'last_name', 'is_superuser',
            'password', 'email', 'age', 'avatar', 'is_active', 'is_staff'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Пользователь слишком молод!")
        return data


class AdminProductCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class AdminProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
