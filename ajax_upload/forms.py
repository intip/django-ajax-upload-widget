from django import forms
from .utils import move_file


class FormUploadMixin(forms.ModelForm):
    file_fields = []
    destination = "/"

    def move_file(self, field):
        i = self.data[field].find(',')
        if(i == -1):
            data = self.data[field]
            url_dst = move_file(data, self.destination)
            self.cleaned_data[field] = url_dst
        else:
            files = self.data[field].split(",")
            path_files = []

            for file in files:
                url_dst = move_file(file, self.destination)
                path_files.append(url_dst)

            self.cleaned_data[field] = path_files

    def is_valid(self):
        valid = super(
            FormUploadMixin, 
            self).is_valid()

        if(valid):
            for field in self.file_fields:
                self.move_file(field)

        return valid