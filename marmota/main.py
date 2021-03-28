# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from platform_urls import douyin


def get_douyin_m3u8(share_link):
    return douyin.get_real_url(share_link)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    share_link = input("抖音分享链接")
    print(get_douyin_m3u8(share_link))
