#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status"""


import urllib.request

if __name__ == "__main__":
    with urllib.request.\
            urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        content_type = type(content)
        utf8_content = content.decode('utf-8')

    print("Body response:")
    print(f"    - type: {content_type}")
    print(f"    - content: {content}")
    print(f"    - utf8 content: {utf8_content}")
