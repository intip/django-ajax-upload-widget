from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

class AjaxUploadException(Exception):
    pass


class AjaxClearableFileInput(forms.ClearableFileInput):
    template_with_clear = ''  # We don't need this
    template_with_initial = '%(input)s'
    reverse_default = 'ajax-upload'
    multiple_uploads = False

    def render(self, name, value, attrs=None):
        attrs = attrs or {}
        if value:
            filename = u'%s' % value
        else:
            filename = ''
        attrs.update({
            'class': attrs.get('class', '') + 'ajax-upload',
            'data-filename': filename, 
            'data-required': self.is_required or '',
            'data-upload-url': reverse(self.reverse_default),
            'data-multiple-uploads': self.multiple_uploads,
        })
        output = super(AjaxClearableFileInput, self).render(name, value, attrs)
        return mark_safe(output)

    def value_from_datadict(self, data, files, name):
        return data.get(name)
