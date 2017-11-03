#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status
        # 我手动测试了编码。并设置好，这样有助于效率的提升

        r.encoding = ('utf-8')
        return r.text
    except:
        return "Someting Wrong！"


# 获取该小说每个章节的url,创建小说文件+开头添上小说名。更换第18行的小说网址即可以下载不同小说。
html_single_fiction = get_html("http://www.qu.la/book/3802/")
bsObj_single_fiction = BeautifulSoup(html_single_fiction, "lxml")
chapter_List = bsObj_single_fiction.findAll("dd")
url_list = []
for long_url in chapter_List:
    url_list.append('http://www.qu.la' + long_url.a['href'])
fiction_name = bsObj_single_fiction.find('h1').text

with open('D://fiction_0/{}.txt'.format(fiction_name), "ab") as f:
    fiction_name = fiction_name.encode('utf-8')
    f.write(b'''%s

     ''' % (fiction_name))
    fiction_name = fiction_name.decode('utf-8')

# 获取单页文章的内容并保存到本地
'''
    获取小说每个章节的文本
    并写入到本地
    '''


def parser():
    for single_url in url_list:
        html = get_html(single_url).replace('<br/>', '\n')
        soup = BeautifulSoup(html, 'lxml')
        chapter_name = soup.find("h1")
        try:
            txt = soup.find('div', id='content').text.replace(
                'chaptererror();', '')
            title = soup.find('h1').text

            txt = txt.encode("utf-8")
            title = title.encode("utf-8")

            with open('D://fiction_0/{}.txt'.format(fiction_name), "ab") as f:

                f.write(b'''%s

                ''' % (title))
                f.write(b'''%s

                ''' % (txt))

                txt = txt.decode("utf-8")
                title = title.decode("utf-8")
                print('当前小说：{} 当前章节: {} 已经下载完毕'.format(fiction_name, title))
        except:
            print('someting wrong')
        f.close()

        # parser()


if __name__ == '__main__':
    parser()



