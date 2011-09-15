from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from zebra.widgets import NoNameTextInput, NoNameSelect
from django.utils.dates import MONTHS

class MonospaceForm(forms.Form):

    def addError(self, message):
        self._errors[NON_FIELD_ERRORS] = self.error_class([message])

  
class CardForm(MonospaceForm):
    last_4_digits = forms.CharField(required=True, min_length=4, max_length=4, widget=forms.HiddenInput()  )
    stripe_token  = forms.CharField(required=True, widget=forms.HiddenInput())

class StripePaymentForm(CardForm):
    card_number         = forms.CharField(required=False, max_length=20, widget=NoNameTextInput())
    card_cvv            = forms.CharField(required=False, max_length=4,  widget=NoNameTextInput())
    card_expiry_month   = forms.ChoiceField(required=False, widget=NoNameSelect(), choices=MONTHS.iteritems())
    card_expiry_year    = forms.CharField(required=False, max_length=4,  widget=NoNameTextInput())