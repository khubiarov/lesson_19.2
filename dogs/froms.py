from datetime import datetime

from django import forms
from dogs.models import Dog, Breed, Parent


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Dog
        fields = ('name', 'breed', 'photo', 'birth_day')

    def clean_birth_day(self):
        cleaned_data = self.cleaned_data['birth_day']

        now_year = datetime.now().year

        if (now_year - cleaned_data.year) > 100:
            raise forms.ValidationError('Собака должна быть моложе 100 лет')
        return cleaned_data


class ParentForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'


class BreedForm(forms.ModelForm):
    pass