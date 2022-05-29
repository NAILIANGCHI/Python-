# author:Naraci
# time:14:44
# file:DouYing_Video.py
# IDE:PyCharm

import requests
import re
import os

print("欢迎使用奈良池DY无水印解析系统\n")
if os.path.exists('D:/抖音无水印解析视频'):
    wjml = os.path.exists
    print("检测到已有该目录")
else:
    os.makedirs("D:/抖音无水印解析视频")
    print("以为您创建下载目录")

pre_savename = 'D:/抖音无水印解析视频/'
name = "下载成功文件已保存至"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30 "
}


def UrlGet(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 输出异常信息
        r.encoding = r.apparent_encoding
        return r.text  # 将网页信息内容返回给其他程序块
    except:
        return ''  # 将异常内容返回空字符串


def UrlHandle(url):
    shorturl = re.findall("https?://[a-z./A-Z0-9]+", url)
    if len(shorturl) == 1:
        VideoShoutUrl = shorturl[0]
        url = requests.get(VideoShoutUrl, headers=headers).url
        VideoPage = requests.post(url=url, headers=headers)
        # 匹配视频地址
        regular = re.findall('src(.*?)mp4', VideoPage.text)[1]
        # 解码
        video_url = requests.utils.unquote(regular).replace('":"', 'https:')
        title = re.findall('<title data-react-helmet="true">(.*?)</title>', VideoPage.text)[0]

        print("正在下载：", title)
        # 创建文件夹
        f = open(pre_savename + "%s.mp4" % title, mode="wb")  # wb表示写入的内容为非文本文件,VideoName为视频标题
        f.write(requests.get(video_url, headers=headers).content)  # 向外取出图片数据，不是文本信息
        DiZhi = name + pre_savename
        print(DiZhi)


if __name__ == '__main__':
    run = 1
    while run == 1:
        url = input("请输入视频链接：")
        # url = '5.15 yGi:/ 喜欢你 很喜欢你 特别喜欢你.@ta  https://v.douyin.com/Ff1a79j/ 复制此链接，打开Dou音搜索，直接观看视频！ '
        html = UrlGet(url)
        UrlHandle(url)
        print(html)
