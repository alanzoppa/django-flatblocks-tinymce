from django.forms import ModelForm
from django import forms
from tinymce.widgets import TinyMCE

from flatblocks.models import FlatBlock

class FlatBlockForm(ModelForm):
    content = forms.CharField(widget=TinyMCE(), required=False)
    class Meta:
        model = FlatBlock
        #exclude = ('slug', )
