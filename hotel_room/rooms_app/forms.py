from django import forms
from .models import Reservation
from django.core.exceptions import ValidationError


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['check_in', 'check_out', 'num_guests']      
        widgets = {
                'check_in': forms.DateInput(attrs={'type': 'date'}),
                'check_out': forms.DateInput(attrs={'type': 'date'}),
            }  
        
    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        # Check if check_out is less than or equal to check_in
        if check_in and check_out and check_out <= check_in:
            raise ValidationError(("Check-out date must be later than the check-in date"))