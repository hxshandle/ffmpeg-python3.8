# -*- coding: utf-8 -*-
from unittest import TestCase
from marmota.ali import multimediaai as ai


class Testmultimediaai(TestCase):
    def test_create_video_analysis_job(self):
        ai.create_video_analysis_job('https://handle-bucket-sh.oss-cn-shanghai.aliyuncs.com/tmp/test.mp4', "test-sdk")
