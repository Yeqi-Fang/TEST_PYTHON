import os
from lxml import etree
import concurrent.futures
import pickle

def download(url):
    # while True:
    os.system(f'you-get {url}')
    # print(s)
    # if not s:
    #     break


def thre(path):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download, path)
    # return results


if __name__ == '__main__':
    with open("(205) 263 - Object localization in images_ using GAP layer - YouTube.txt", 'r', encoding='utf-8') as f:
        txt = f.read()
    response = etree.HTML(txt)
    paths = response.xpath('//a[@id="wc-endpoint"]/@href')
    length = len(paths)
    sub_len = length // 4
    # print(sub_len)
    a1 = paths[:60:-1]
    a2 = paths[60:120:-1]
    a3 = paths[120:180:-1]
    a4 = paths[180::-1]
    path = [a2, a3, a4]
    # print(len(paths))
    os.chdir(r'F:\youtube\DS')
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(thre, path)

# https://www.youtube.com/watch?list=PLZsOBAyNTZwbIjGnolFydAN33gyyGP7lT&amp;v=Pql6ShORpNU
# b = re.compile(r'["]https://www.youtube.com/watch\?list=(.*)&amp;v=(\w{5,13})["]')
# b = re.compile(r'<yt-button-shape><a class="yt-spec-button-shape-next yt-spec-button-shape-next--tonal yt-spec-button-shape-next--overlay yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-leading " href="https://www.youtube.com/watch(\w*)[" rel="nofollow" target="" ]')
# b = re.compile(r'https://www.youtube.com(.{,60})["]')
# a = re.findall(b, txt)
# # print(a[0])
# L = []
# for i in a:
#     if 'watch' in i and ''
# print(len(a))
