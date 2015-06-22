import shutil

from django.conf import settings

def move_file(_file, dir):
    url_dst = dir + "/%s" % _file
    src = settings.MEDIA_ROOT + "tmp/%s" % _file
    dst = settings.MEDIA_ROOT + dir +"/%s" % _file
    shutil.move(src, dst)
    return url_dst