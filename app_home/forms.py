
from django.forms import ModelForm

from app_home.models import ContactModel


class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].widget.attrs["placeholder"] = field


