from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import PlanBuyCarsVactionsModel


class PlanBuyCarsVactionsForm(forms.ModelForm):
    class Meta:
        model = PlanBuyCarsVactionsModel
        exclude = ["created", "modified"]
        widgets = {
            "period": forms.DateInput(attrs={"type": "date"}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))