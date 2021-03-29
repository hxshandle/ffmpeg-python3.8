# -*- coding: utf8 -*-
from aliyunsdkcore.client import AcsClient
from marmota.common import ALI_TOKEN
from aliyunsdkmultimediaai.request.v20190810 import CreateLabelTaskRequest
from aliyunsdkmultimediaai.request.v20190810 import CreateCoverTaskRequest
from aliyunsdkmultimediaai.request.v20190810 import CreateGifTaskRequest
from aliyunsdkmultimediaai.request.v20190810 import GetTaskStatusRequest
from aliyunsdkmultimediaai.request.v20190810 import GetTaskResultRequest
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
import json

# 创建 AcsClient 实例
client = AcsClient(ALI_TOKEN.ali_access_key, ALI_TOKEN.ali_access_key_secret, ALI_TOKEN.ali_multimediaai_region)


def create_video_analysis_job(video_url: str, video_name: str, app_id: str = ALI_TOKEN.ali_multimediaai_app_id):
    request = CreateLabelTaskRequest.CreateLabelTaskRequest()
    request.set_VideoUrl(video_url)
    request.set_VideoName(video_name)
    request.set_ApplicationId(app_id)
    # request.set_CallbackUrl("<yourCallbackUrl>")  # 回调通知Url，此参数为可选
    # request.set_TemplateId("<yourTemplateId>")    # 自定义模板id，此参数为可选，不传会使用默认模板
    try:
        response = client.do_action_with_exception(request)
        print(response)
    except ServerException as e:
        print(e.get_error_code())
        print(e.get_error_msg())
    except ClientException as e:
        print(e.get_error_code())
        print(e.get_error_msg())
