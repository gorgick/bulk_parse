import json

import requests

cookies = {
    '_wbauid': '7054570121769605419',
    'x_wbaas_token': '1.1000.2f78af87974343f9a4f299b588a041de.MHwxNDYuMTIwLjE5My4xMTN8TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgNi4xOyBXT1c2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwOS4wLjAuMCBTYWZhcmkvNTM3LjM2IE9QUi85NS4wLjAuMHwxNzcyNTM2MzcxfHJldXNhYmxlfDJ8ZXlKb1lYTm9Jam9pSW4wPXwwfDN8MTc3MTkzMTU3MXwx.MEUCIF0cV1A2go24zqbSB3f6QzFoe5yf6mD5mZbpEtlSJ1ubAiEAynV8Q4NY0lPe+SLNqn0OCt1kcn6tmb8ilqkkoFg6awc=',
}

headers = {
    'authority': 'www.wildberries.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_wbauid=7054570121769605419; x_wbaas_token=1.1000.2f78af87974343f9a4f299b588a041de.MHwxNDYuMTIwLjE5My4xMTN8TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgNi4xOyBXT1c2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwOS4wLjAuMCBTYWZhcmkvNTM3LjM2IE9QUi85NS4wLjAuMHwxNzcyNTM2MzcxfHJldXNhYmxlfDJ8ZXlKb1lYTm9Jam9pSW4wPXwwfDN8MTc3MTkzMTU3MXwx.MEUCIF0cV1A2go24zqbSB3f6QzFoe5yf6mD5mZbpEtlSJ1ubAiEAynV8Q4NY0lPe+SLNqn0OCt1kcn6tmb8ilqkkoFg6awc=',
    'deviceid': 'site_2a3193d84b164e9eba7e108a260acda1',
    'referer': 'https://www.wildberries.ru/catalog/0/search.aspx?search=%D0%BD%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE%D0%B4%D0%BD%D0%B8%D0%B5%20%D1%83%D0%BA%D1%80%D0%B0%D1%88%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B4%D0%BB%D1%8F%20%D0%B4%D0%BE%D0%BC%D0%B0%20%D0%BD%D0%B0%20%D1%81%D1%82%D0%BE%D0%BB',
    'sec-ch-ua': '"Opera";v="95", "Chromium";v="109", "Not;A=Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0',
    'x-queryid': 'qid705457012176960541920260217153558',
    'x-requested-with': 'XMLHttpRequest',
    'x-spa-version': '13.23.2',
    'x-userid': '0',
}

params = {
    'ab_testing': 'false',
    'appType': '1',
    'curr': 'rub',
    'dest': '-59202',
    'hide_dflags': '131072',
    'hide_dtype': '13',
    'hide_vflags': '4294967296',
    'inheritFilters': 'false',
    'lang': 'ru',
    'query': 'новогодние украшения для дома на стол',
    'resultset': 'catalog',
    'sort': 'popular',
    'spp': '30',
    'suppressSpellcheck': 'false',
}

response = requests.get(
    'https://www.wildberries.ru/__internal/u-search/exactmatch/sng/common/v18/search',
    params=params,
    cookies=cookies,
    headers=headers,
)