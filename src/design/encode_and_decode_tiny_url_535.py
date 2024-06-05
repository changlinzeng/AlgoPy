import base64


class Codec:

    def __init__(self):
        self.short_to_full = {}
        self.full_to_short = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        start = longUrl.index('://')
        protocol = longUrl[0:start + 3]
        base_url = longUrl[start + 3:]
        if longUrl in self.full_to_short:
            return self.full_to_short[base_url]
        short_url = base64.b64encode(bytes(base_url, 'utf-8')).decode()
        while short_url in self.short_to_full:
            short_url = base64.b64encode(bytes(base_url, 'utf-8'))
        self.short_to_full[short_url] = base_url
        return f'{protocol}{short_url}'

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        start = shortUrl.index('://')
        protocol = shortUrl[0:start + 3]
        base_url = shortUrl[start + 3:]
        return f'{protocol}{self.short_to_full[base_url]}'


if __name__ == '__main__':
    codec = Codec()
    print(codec.encode('https://leetcode.com/problems/design-tinyurl'))
