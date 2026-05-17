import urllib.request
import re

urls = [
    'https://maps.app.goo.gl/JwRn1jZBcomEHBSp9',
    'https://maps.app.goo.gl/vJhAM3jidYcxFCUT6',
    'https://maps.app.goo.gl/hev9rZeCPvxEpiqU6'
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        match = re.search(r'meta property="og:image" content="([^"]+)"', html)
        if match:
            print('FOUND:', match.group(1))
        else:
            print('NOT FOUND IN', url)
    except Exception as e:
        print('ERROR:', str(e))
