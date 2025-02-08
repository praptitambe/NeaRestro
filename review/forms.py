from .models import Comments,Cuisine
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment','rating')

class RestroSearchForm(forms.Form):
    q = forms.CharField()
    c = forms.ModelChoiceField(queryset=Cuisine.objects.all().order_by('cuisine_type'), empty_label='Filter by Cuisine', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['c'].label = ''
        self.fields['c'].required = False
        self.fields['c'].label = 'Category'
        self.fields['q'].label = 'Search For'
        self.fields['q'].widget.attrs.update(
            {'class': 'form-control menudd'})
        self.fields['q'].widget.attrs.update(
            {'data-toggle': 'dropdown'})