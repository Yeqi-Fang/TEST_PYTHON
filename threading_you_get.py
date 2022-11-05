import os
from lxml import etree
import concurrent.futures

def download(url):
    # while True:
    # global paths
    s = os.system(f'you-get {url}')
    if not s:
        paths.remove(url)
        # if not s:
        #     break

if __name__ == '__main__':
    with open("(205) 263 - Object localization in images_ using GAP layer - YouTube.txt", 'r', encoding='utf-8') as f:
        txt = f.read()
    response = etree.HTML(txt)
    paths = response.xpath('//a[@id="wc-endpoint"]/@href')[100:][::-1]
    # os.chdir(os.path.split(__file__)[0])

    # with open("remaining_url.pkl", 'rb') as f:
    #         paths = pickle.load(f)
    # print(len(paths))
    os.chdir(r'F:\youtube\DS')
    # while True:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(download, paths)
    # print(len(paths))
    # with open("remaining_url.pkl", 'wb') as f:
    #     pickle.dump(paths, f)

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
