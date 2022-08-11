# 爬一张图片 Ctrl + / 是注释
import requests
# url = 'https://p3.music.126.net/X3lwU-K8ahwkswzKmm_xMA==/3435973846756513.jpg?param=2000y2000'
# res = requests.get(url)
# print(res.content)
# with open('wangy.png', 'wb') as f:
#     f.write(res.content)


# 爬音乐
# m4a是媒体文件

# url = 'https://m701.music.126.net/20220811135859/8a5c5b3da7015623a30e621b1a153889/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/14096432793/a684/17b0/706f/f9bcbe1cac45142450c4d69aede0bbe3.m4a'
# headers ={
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# }
#
# res = requests.get(url,headers=headers)
# with open('漠河舞厅.mp3','wb') as f:
#     f.write(res.content)

# 网易云有接口，可以批量下载

# MV下载
url = 'https://vodkgeyttp8.vod.126.net/cloudmusic/JDAxITExNDhgYyJgICMgIA==/mv/309003/4a7f329f68c49c4d53d7996fbcecb57e.mp4?wsSecret=51e6073a5e8a5955d95976cc69d40aff&wsTime=1660202257'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
res = requests.get(url, headers = headers)

with open('网易云视频1.mp4', 'wb') as f:
    f.write(res.content)
