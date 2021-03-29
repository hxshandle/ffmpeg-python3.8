from unittest import TestCase
from marmota.ali import oss
from pathlib import Path
from marmota.common import *


class TestOss(TestCase):
    def test_upload_file(self):
        path = Path(__file__).parent.parent.parent.joinpath('data/hello.txt')
        print(path)
        oss.upload_file(path)

    def test_t(self):
        tk = AliToken()
        print(ALI_TOKEN.ali_access_key)
        c = 1
