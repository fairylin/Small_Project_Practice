#encoding=utf-8
#-*- encoding : utf-8 -*-
#/python-pachong/music-baidu/music_spider.py
import requests
import re
import urllib2
import urllib


# data = {
#     'key': '刘德华'
# }
# search_url = 'http://music.baidu.com/search?key='


ids = {0,20,40}
data = {
    'key': "刘德华",
    's': 1,
    'start': ','.join(str(ids)),
    'size': 20,
    'third_type': 0,
}


search_url = 'http://music.baidu.com/search/song'
search_response = requests.get(search_url,params=data)
search_response.encoding="utf-8"

search_html = search_response.text

# print search_html
song_ids = re.findall(r'sid&quot;:(\d+),', search_html)
data = {
    'songIds': ','.join(song_ids),
    'hq': 0,
    'type': 'm4a,mp3',
    'pt': 0,
    'flag': -1,
    's2p': -1,
    'prerate': -1,
    'bwt': -1,
    'dur': -1,
    'bat': -1,
    'bp': -1,
    'pos': -1,
    'auto': -1,
}
song_link = 'http://play.baidu.com/data/music/songlink'
song_response = requests.post(song_link, data=data)
# 将返回的数据转换为字典
song_info = song_response.json()
song_info = song_info['data']['songList']

# 遍历数组，获取其中的歌曲名称和链接
for song in song_info:
    song_name = song['songName']
    with open('%s.mp3' % song_name, "wb") as f:
        response = requests.get(song['songLink'])
        f.write(response.content)