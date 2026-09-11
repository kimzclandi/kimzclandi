"""Resolve linked public repository READMEs and documents without credentials."""
import concurrent.futures
import re
import urllib.request
from pathlib import Path
from urllib.parse import urlsplit

urls=set()
for url in re.findall(r'https://github\.com/kimzclandi/[^\s)]+',Path('README.md').read_text()):
    parts=urlsplit(url).path.strip('/').split('/')
    if len(parts)==2:
        urls.add(f'https://raw.githubusercontent.com/{parts[0]}/{parts[1]}/main/README.md')
    elif len(parts)>4 and parts[2:4]==['blob','main']:
        urls.add('https://raw.githubusercontent.com/'+parts[0]+'/'+parts[1]+'/main/'+'/'.join(parts[4:]))


def check(url):
    with urllib.request.urlopen(url,timeout=30) as response:
        content=response.read()
        if response.status!=200 or len(content)<50:raise ValueError(url)
    return url


with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    checked=list(pool.map(check,sorted(urls)))
print(f'Verified {len(checked)} anonymous public README/document targets')
