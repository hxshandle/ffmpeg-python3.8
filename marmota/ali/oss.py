# -*- coding: utf-8 -*-
import oss2
from pathlib import Path
from marmota.common import ALI_TOKEN

auth = oss2.Auth(ALI_TOKEN.ali_access_key, ALI_TOKEN.ali_access_key_secret)

bucket = oss2.Bucket(auth, ALI_TOKEN.ali_oss_endpoint, ALI_TOKEN.ali_oss_bucket_name)


def upload_file(path: Path):
    bucket.put_object_from_file("{}{}".format(ALI_TOKEN.ali_oss_bucket_root, path.name), str(path))
