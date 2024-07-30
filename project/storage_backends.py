from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
from storages.backends.s3boto3 import *
import os


class InternalWriteDjangoDomainReadBaseStorageClass(S3Boto3Storage):
    def url(self, name, parameters=None, expire=None, http_method=None):
        url = super().url(name=name)
        if settings.OBJECT_STORAGE=="MINIO":
            return url.replace("internal.minio.redirect", os.environ.get("DJANGO_SERVERNAME", "django.localhost"))
        return url


class S3StaticStorage(InternalWriteDjangoDomainReadBaseStorageClass):
    location = settings.PUBLIC_MEDIA_LOCATION + "/static"
    default_acl = "public-read"
    file_overwrite = False
    querystring_auth = False


class S3PublicMediaStorage(InternalWriteDjangoDomainReadBaseStorageClass):
    location = settings.PUBLIC_MEDIA_LOCATION
    default_acl = "public-read"
    file_overwrite = False
    querystring_auth = False


class S3PrivateMediaStorage(InternalWriteDjangoDomainReadBaseStorageClass):
    location = settings.PRIVATE_MEDIA_LOCATION
    default_acl = "private"
    file_overwrite = False
