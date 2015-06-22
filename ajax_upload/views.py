from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.views.generic.base import View

import base64
import re
import uuid

def get_a_uuid():
    r_uuid = base64.urlsafe_b64encode(uuid.uuid4().bytes)
    return r_uuid.replace('=', '')


class AjaxUploaderView(View):
    MESSAGE_ERROR = 'Tipo de arquivo inválido.'

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        import ipdb; ipdb.set_trace()
        files = request.FILES.getlist('file')
        data = {}
        path_files = []
        error = 0

        for file in files:
            file_name = file._name
            type = file_name[file_name.rfind('.'):]

            if self.get_test_regex(type):
                name = get_a_uuid() + type
                path = settings.MEDIA_ROOT + "tmp/%s" % name

                path_files.append(path)

                destination = open(path, 'wb+')
                destination.write(file.read())
                destination.close()
            else:
                error = 1

        if error == 0:
            return JsonResponse({'path': path_files })
        else:
            return JsonResponse({'error': MESSAGE_ERROR})


    def get_test_regex(self, value):
        return True
