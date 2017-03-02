from django import forms
from .models import Stock1

class StockForm(forms.ModelForm):
  class Meta:

      model=Stock1
      fields=['data','desc']