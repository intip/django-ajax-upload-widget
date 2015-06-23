from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.conf import settings

import base64
import uuid

def get_a_uuid():
    r_uuid = base64.urlsafe_b64encode(uuid.uuid4().bytes)
    return r_uuid.replace('=', '')


class AjaxUploaderView(View):
    MESSAGE_ERROR = u'Tipo de arquivo invalido.'

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('file')
        data = {}
        path_files = []
        error = 0

        for file in files:
            file_name = file._name
            type = file_name[file_name.rfind('.'):]
            if self.get_test_regex(type):
                name = "tmp/%s" % (get_a_uuid() + type)
                path = settings.MEDIA_ROOT + name

                path_files.append(name)

                destination = open(path, 'wb+')
                destination.write(file.read())
                destination.close()
            else:
                error = 1

        if error == 0:
            return JsonResponse({'path': path_files })
        else:
            return JsonResponse({'error': self.MESSAGE_ERROR})

    def get_test_regex(self, test_value):
        return True
