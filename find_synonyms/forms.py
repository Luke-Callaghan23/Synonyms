
from django import forms


class MainSearchForm (forms.Form):
    class Meta:
        fields = [
            'search_bar'
        ]
    search_bar = forms.CharField (
        required=False,
        label='Search a New Term . . . ',
        widget=forms.TextInput (
            attrs={
                'class': 'line-item search-bar',
                'id': 'main-search',
                'action': '/synonyms/search/'
            },
        ),
        max_length=255
    )


class SubSearchForm (forms.Form):
    class Meta:
        fields = [
            'search_bar'
        ]
    search_bar = forms.CharField (
        required=False,
        label='',
        widget=forms.TextInput (
            attrs={
                'placeholder': 'Search . . . ',
                'class': 'search-item sub-searchbar',
                'style': 'width: 500px',
                'id': 'sub-search'
            }
        ),
        max_length=255
    )

