import requests as reqs
from bs4 import BeautifulSoup as BS
import shutil
import sys

ROOT_URL = 'https://data.vision.ee.ethz.ch/cvl/DIV2K/'

def main(root_url, dw_addr):
    root_req = reqs.get(root_url)

    if root_req.status_code != 200:
        raise Exception(f"Server is down at {root_url}")

    soup = BS(root_req.content, 'lxml')
    a_s = soup.select('li > a')
    for a in a_s:
        url = a['href']
        if url is not None:
            try:
                print(f"Downloading from {url}")
                fn = url.split('/')[-1]
                addr = f"{dw_addr}/{fn}"
                with reqs.get(url, stream=True) as r:
                    with open(addr, 'wb') as f:
                        shutil.copyfileobj(r.raw, f)
            except Exception as e:
                print(f"Couldn't download from {url}")
                print(e)


if __name__ == "__main__":
    main(ROOT_URL, sys.argv[1])

