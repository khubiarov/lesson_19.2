from django import forms
from blog.models import Blog, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class BlogForm(StyleFormMixin, forms.ModelForm):
    wrong_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Blog
        fields = ('heading', 'content', 'preview')

    def clean_heading(self):
        cleaned_data = self.cleaned_data.get('heading')

        if cleaned_data.lower() in self.wrong_words:
            raise forms.ValidationError('В заголовке есть недопустимое слово')
        return cleaned_data

    def clean_content(self):
        cleaned_data = self.cleaned_data.get('content')

        if cleaned_data.lower() in self.wrong_words:
            raise forms.ValidationError('В описании есть недопустимое слово')
        return cleaned_data


class VersionFrom(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
