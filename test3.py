import os
from lxml import etree
import concurrent.futures


def download(url):
    while True:
        s = os.system(f'you-get {url}')
        if not s:
            break


def thre():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(download, paths)
    return results

if __name__ == '__main__':
    with open("D:\multi_media\DeskTop\(205) 263 - Object localization in images_ using GAP layer - YouTube.txt", 'r', encoding='utf-8') as f:
        txt = f.read()
    response = etree.HTML(txt)
    paths = response.xpath('//a[@id="wc-endpoint"]/@href')
    length = len(paths)
    sub_len = length//4
    print(sub_len)
    a1 = paths[:60]
    a2 = paths[60:120]
    a3 = paths[120:180]
    a4 = paths[180:]
    path = [a1, a2, a3, a4]
    # print(len(paths))
    os.chdir(r'F:\youtube\DS\test')
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
