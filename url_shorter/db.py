import time
import random 
import hashlib
import base64

class Database:
    def __init__(self):
        self.url_to_hash = {}
        self.hash_to_url = {}

    def get_hash_from_url(self, url):
        return self.url_to_hash.get(url)

    def get_url_from_hash(self, hsh):
        print(hsh)
        return self.hash_to_url.get(hsh)

    def store_url_hash(self, url, url_hash):
        self.url_to_hash[url] = url_hash
        self.hash_to_url[url_hash] = url

    def remove_url_hash(self, hsh):
        print(hsh)

        url = self.hash_to_url.pop(hsh, None)
        if url:
            self.url_to_hash.pop(url, None)

