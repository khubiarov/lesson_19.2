from django import forms
from main.models import Student, Subject


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class StudentFrom(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'  если нужно все поля указать
        fields = ('first_name', 'last_name', 'avatar', 'email')
        # exclude = ('is_active,)если нужно исключить поле(поля)

    def clean_email(self):
        cleaned_data = self.cleaned_data['email']

        if 'sky.pro' not in cleaned_data:
            raise forms.ValidationError('Почта должна относиться к учебному заведению')

        return cleaned_data


class SubjectForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

    '''def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    '''
