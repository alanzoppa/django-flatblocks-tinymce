from django.forms import ModelForm
from django import forms
from flatblocks.models import FlatBlock

try:
    from tinymce.widgets import TinyMCE
    tiny_mce = True
except ImportError:
    tiny_mce = False

class FlatBlockForm(ModelForm):
    if tiny_mce:
        content = forms.CharField(widget=TinyMCE(), required=False)
    class Meta:
        model = FlatBlock
        #exclude = ('slug', )
