from .models import Document
from django.forms import ModelForm


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['document', 'description']