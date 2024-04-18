from django import forms
from .models import UserProfile
from django.utils.translation import gettext as _

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': _('Phone Number'),
            'default_postcode': _('Postal Code'),
            'default_town_or_city': _('Town or City'),
            'default_street_address1': _('Street Address 1'),
            'default_street_address2': _('Street Address 2'),
            'default_county': _('County, State or Locality'),
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                placeholder = placeholders.get(field, '')
                self.fields[field].widget.attrs['placeholder'] = f"{placeholder} {'*' if self.fields[field].required else ''}"
                self.fields[field].widget.attrs['class'] = 'stripe-form-input focus-highlight'
                self.fields[field].label = False