from django import forms
from django.core.exceptions import ValidationError

from pages.models import Post

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['priority'].empty_label = "Категория не выбрана"

    class Meta:
        model = Post
        fields = ['name', 'price', 'description', 'photo', 'priority']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return name
        