import os
from dotenv import load_dotenv

load_dotenv()


def env(fn):
    def _do(*args):
        key = fn(args)
        val = os.getenv(key, '')
        if val == '':
            raise RuntimeError("环境变量{}未正确设置".format(key))
        return val
    return _do


class AliToken:

    @property
    @env
    def ali_access_key(self):
        return 'ali_access_key'

    @property
    @env
    def ali_access_key_secret(self):
        return 'ali_access_key_secret'

    @property
    @env
    def ali_oss_endpoint(self) -> str:
        return 'ali_oss_endpoint'

    @property
    @env
    def ali_oss_bucket_name(self) -> str:
        return 'ali_oss_bucket_name'

    @property
    @env
    def ali_oss_bucket_root(self):
        return 'ali_oss_bucket_root'

    @property
    @env
    def ali_multimediaai_region(self):
        return 'ali_multimediaai_region'

    @property
    @env
    def ali_multimediaai_app_id(self):
        return 'ali_multimediaai_app_id'
