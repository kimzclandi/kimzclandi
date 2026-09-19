"""Check local Markdown links and anonymous public repository/document targets."""
import concurrent.futures
import re
import urllib.request
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]


def collect_targets(root):
    urls = set()
    for path in [root / 'README.md', *sorted((root / 'docs').rglob('*.md'))]:
        content = path.read_text()
        for target in re.findall(r'\]\(([^)]+)\)', content):
            if '://' not in target and not target.startswith('#'):
                local = path.parent / unquote(target.split('#')[0])
                if not local.exists():
                    raise ValueError(f'Missing local target: {path.name}: {target}')
        for url in re.findall(r'https://github\.com/kimzclandi/[^\s)]+', content):
            parts = urlsplit(url).path.strip('/').split('/')
            if len(parts) == 2:
                urls.add(f'https://raw.githubusercontent.com/{parts[0]}/{parts[1]}/main/README.md')
            elif len(parts) > 4 and parts[2:4] == ['blob', 'main']:
                urls.add('https://raw.githubusercontent.com/' + '/'.join(parts[:2]) + '/main/' + '/'.join(parts[4:]))
    if not urls:
        raise ValueError('No public repository/document targets found')
    return urls


def check(url):
    with urllib.request.urlopen(url, timeout=30) as response:
        content = response.read()
        if response.status != 200 or len(content) < 50:
            raise ValueError(url)
    return url


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        checked = list(pool.map(check, sorted(collect_targets(ROOT))))
    print(f'Verified local links and {len(checked)} anonymous public README/document targets')


if __name__ == '__main__':
    main()
