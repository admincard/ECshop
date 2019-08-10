import requests
import json

class SendMethod:
    @staticmethod
    def send_method(method,url,data=None):
        #格式化请求数据
        req_data = {"json":json.dumps(data)}
        if method == 'post':
            response = requests.request(method=method,url=url, data=req_data)
        elif method == 'get':
            response = requests.request(method=method,url=url)
        else:
            response = None
        return response.json()
    #美化
    @staticmethod
    def response_dumps(response):
        return json.dumps(response,indent=2,ensure_ascii=False)