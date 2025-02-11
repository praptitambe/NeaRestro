from .models import Comments, Cuisine
from django import forms

# <---------Comment form------------->
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment', 'rating')


# <---------Restaurant search form------------->
class RestroSearchForm(forms.Form):
    q = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Search for a restaurant by name or city'
            }
        )
    )
    c = forms.ModelChoiceField(
        queryset=Cuisine.objects.all().order_by('cuisine_type'),
        empty_label='Filter by Cuisine',
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['c'].label = ''
        self.fields['c'].required = False
        self.fields['c'].label = 'Cuisine'
        self.fields['q'].label = 'Search For'
        self.fields['q'].widget.attrs.update({'class': 'form-control menudd'})
        self.fields['q'].widget.attrs.update({'data-toggle': 'dropdown'})
