
from django.forms.widgets import CheckboxInput
from said_synonyms.scripts.view_syns import get_intersections
from django import forms


class SearchForm (forms.Form):
    class Meta:
        fields = [
            'search_bar',
            'get_intersections'
        ]
    search_bar = forms.CharField (
        required=False,
        label='Search a Category . . . ',
        widget=forms.TextInput (
            attrs={
                'class': 'line-item search-bar',
                'id': 'main-search',
                'action': '/search/',                
                'style': 'float: inherit;',
                'autocompletable': 'true',
                'name': 'search_bar'
            },
        ),
        max_length=255
    )


    get_intersections = forms.BooleanField(
        required=False,
        label='Combos',
        initial=False,
        help_text='This may take a while!',
        widget=forms.CheckboxInput (
            attrs={
                'class': 'intersection-button',
                'id': 'checkid'
            }
        )
    )

class AddForm (forms.Form):
    class Meta:
        fields = [
            'search_bar',
        ]
    search_bar = forms.CharField (
        required=False,
        label='Add Synonym: Sobbed . . . ',
        widget=forms.TextInput (
            attrs={
                'class': 'line-item search-bar',
                'id': 'main-search',
                'action': '/search/',                
                'style': 'float: inherit;',
                'autocompletable': 'true',
                'name': 'search_bar'
            },
        ),
        max_length=255
    )
    synonym_file = forms.FileField (
        required=True,
        label='',
        widget=forms.FileInput (
            attrs={
                'class': 'file-input',
                'id': 'file',
                'name':'synonym_file'
            }
        )
    )