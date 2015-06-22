from django import forms
from .utils import move_file


class FormUploadMixin(forms.ModelForm):
    file_fields = []
    destination = "/"

    def move_file(self, field):
        data = self.data[field]
        url_dst = move_file(data, self.destination)
        self.cleaned_data[field] = url_dst
    
    def is_valid(self):
        valid = super(
            FormUploadMixin, 
            self).is_valid()

        if(valid):
            for field in self.file_fields:
                self.move_file(field)

        return valid