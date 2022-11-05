import os
from lxml import etree
import concurrent.futures
import pickle

def download(url):
    # while True:
    s = os.system(f'you-get {url}')
    print(s)
    # if not s:
    #     break


def thre(path):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(download, path)
    # return results


if __name__ == '__main__':
    with open("(207) Pytorch Tutorial - Setting up a Deep Learning Environment (Anaconda & PyCharm) - YouTube.txt", 'r', encoding='utf-8') as f:
        txt = f.read()
    response = etree.HTML(txt)
    paths = response.xpath('//a[@id="wc-endpoint"]/@href')
    length = len(paths)
    print(length)
    # sub_len = length // 4
    # # print(sub_len)
    a1 = paths[:10:-1]
    a2 = paths[10:20:-1]
    a3 = paths[30:40:-1]
    a4 = paths[40::-1]
    path = [a1, a2, a3, a4]
    # print(len(paths))
    os.chdir(r'F:\youtube\AP')
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
