"""
TinyURL is a URL shortening service where you enter a URL
such as https://leetcode.com/problems/design-tinyurl and
it returns a short URL such as http://tinyurl.com/4e9iAk.

length --> decode str-int
Using hashcode -- inbuilt function hashCode()
 map.put(longUrl.hashCode(), longUrl);
 Using random number
"""
class Codec:
    def __init__(self):
        self.urls = []

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.urls.append(longUrl)
        return 'http://tinyurl.com/' + str(len(self.urls)-1)
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls[int(shortUrl.split('/')[-1])]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))