from django.forms import ModelForm

from .models import Photographer

class PhotographerForm(ModelForm):
    class Meta:
        model = Photographer
        fields = "__all__"