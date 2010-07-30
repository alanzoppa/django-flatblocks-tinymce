from django.contrib import admin
from flatblocks.models import FlatBlock
from flatblocks.forms import FlatBlockForm
 
class FlatBlockAdmin(admin.ModelAdmin):
    ordering = ['slug',]
    list_display = ('slug', 'header', 'content')
    search_fields = ('slug', 'header', 'content')
    form = FlatBlockForm


admin.site.register(FlatBlock, FlatBlockAdmin)
