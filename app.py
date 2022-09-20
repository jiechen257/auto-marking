# -*- coding: utf-8 -*
import requests
from requests.api import head
import yagmail

"""
@Author  : jiechen
@Email   : xxx@qq.com
@Filename: app
@Date    :  2022/9/19
@Todo:易校园自动打卡
"""


def eMail(email_to, email_title, email_content):
    # 邮件用户
    mail_user = 'xxx@qq.com'
    # 授权码
    mail_key = ''
    # smtp服务器
    mail_host = 'smtp.qq.com'
    try:
        mail_server = yagmail.SMTP(
            user=mail_user, password=mail_key, host=mail_host)
        mail_server.send(email_to, email_title,
                         email_content, attachments=None)
        mail_server.close()
        return True
    except Exception as e:
        print(e)
        return False


def DoDetail(json, userid):
    # 输入打卡信息
    data = json
    # 添加打卡信息
    data['address'] = ''
    # 填写Tokan信息
    data['uuToken'] = ''
    # 填写Userid
    data['loginUserId'] = ''
    # 填写学校id
    data['loginSchoolCode'] = ''
    # 填写学校名称
    data['loginSchoolName'] = ''
    # 填写体温信息
    data['temperature'] = ''
    # 填写打卡地址
    data['locationInfo'] = ""
    # 填写经纬度信息
    data['longitudeAndLatitude'] = ''
    data["loginUserId"] = userid
    data["ymId"] = userid
    data["sessionId"] = ""
    data["loginUserName"] = ""
    data["loginSchoolCode"] = ""
    data["loginSchoolName"] = ""
    data["platform"] = ""
    requests.packages.urllib3.disable_warnings()
    # 请求易校园接口
    response = requests.post(
        "https://h5.xiaofubao.com/marketing/health/doDetail", headers=headers, data=data, verify=False)
    return response.json()

    # 获取userid


def GetDetail(userid):
    data1 = {
        "loginUserId": userid,
        "ymId": userid,
        "sessionId": "",
        "loginUserName": "",
        "loginSchoolCode":"",
        "loginSchoolName": "",
        "platform": "",
    }
    requests.packages.urllib3.disable_warnings()
    response = requests.post(
        "https://h5.xiaofubao.com/marketing/health/getDetail", headers=headers, data=data1, verify=False)
    return response.json()

    # 伪造请求头
if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SEA-AL10 Build/HUAWEISEA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 ZJYXYwebviewbroswer ZJYXYAndroid tourCustomer/yunmaapp.NET/4.2.8/yunma03c72fa3-9ef6-4b4c-9cfd-9c0743ffcd80',
               'Cookie': ''}


    globalUserId = ''

    data['uuToken'] = globalUserId
    # 填写Userid

    json = GetDetail(globalUserId)

    print(json)
    print('======================================================================'*2)
    if(json['success'] == True):
        json = DoDetail(json['data'], globalUserId)
        print(json)

    print('======================================================================'*2)

    if(json['success'] == True):
        eMail(email_to='xxx@qq.com',
                  email_title='健康打卡成功!', email_content=str(json))
        print('成功')
    else:
        eMail(email_to='xxx@qq.com',
                  email_title='健康打卡失败!', email_content=str(json))
        print('失败')
