import shutil

from django.conf import settings

def move_file(_file, dir):
    url_dst = dir + "/%s" % _file[4:]
    src = settings.MEDIA_ROOT + _file
    dst = settings.MEDIA_ROOT + url_dst
    shutil.move(src, dst)
    return url_dst