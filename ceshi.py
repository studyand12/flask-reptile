import json
import asyncio
import aiohttp

search_params = {
    'm': 'vod-search'
}


async def main(search_txt: str):
    async with open('All_web.json', 'r', encoding='utf-8') as f:
        web_list = json.load(f)
        web_dict = web_list.items()
        vale_lis = []
        key_lis = []
        for line in web_dict:
            for key, vale in line:
                head = await add_headers(vale)
                key_lis.append(key)
                vale_lis.append(head)
        text = await request(key_lis, vale_lis, search_txt)


async def add_headers(web_home: str):
    """
    添加header信息
    :return:
    """
    return f"""
    search_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.122 Safari/537.36',
        'Referer': {web_home},
        'Origin': {web_home},
        'Host': {web_home}
    }"""


def for_in(list_txt):
    for a in list_txt:
        return a


async def request(search_url, search_headers, search_data):
    for one, two in search_url, search_headers:
        async with aiohttp.ClientSession as repose:
            first_html = await repose.post(url=one, params=search_params, headers=two, data=search_data)

