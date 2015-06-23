from django import forms
from .utils import move_file


class FormUploadMixin(forms.ModelForm):
    file_fields = []
    destination = "/"

    def move_file(self, field):
        data = self.data.getlist(field)
        path_files = []
        print data

        for file in data:
            i = file.find(',')

            if(i == -1):
                if(len(data) > 1):
                    url_dst = move_file(file, self.destination)
                    path_files.append(url_dst)
                else:
                    url_dst = move_file(file, self.destination)
                    path_files = url_dst
                    break;
            else:
                files = self.data[field].split(",")

                for file_1 in files:
                    url_dst = move_file(file_1, self.destination)
                    path_files.append(url_dst)

        self.cleaned_data[field] = path_files

    def is_valid(self):
        data = self.data.getlist("documents_copy")
        for index, file in enumerate(data):
            if(file == ""):
                data.pop(index)

        valid = super(
            FormUploadMixin, 
            self).is_valid()

        if(valid):
            for field in self.file_fields:
                self.move_file(field)

        return valid