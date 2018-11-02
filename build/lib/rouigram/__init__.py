import requests
import json
from six.moves.urllib.request import urlopen

class getInformation:
    
    def __init__(self,username):
        link = "http://api.pythony.ir/v1/?username="+username
        response = urlopen(link)
        self.parsed = json.loads(response.read())

    def user_id(self):
        return self.parsed['rouigram']['user_id']

    def username(self):
        return self.parsed['rouigram']['username']

    def fullname(self):
        return self.parsed['rouigram']['fullname']

    def follower_count(self):
        return self.parsed['rouigram']['follower_count']
    
    def following_count(self):
        return self.parsed['rouigram']['following_count']
        
    def media_count(self):
        return self.parsed['rouigram']['media_count']

    def external_url(self):
        return self.parsed['rouigram']['external_url']
        
    def is_private(self):
        return self.parsed['rouigram']['is_private']

    def biography(self):
        return self.parsed['rouigram']['biography']
        
    def profile_hd_photo(self):
        return self.parsed['rouigram']['profile_hd_photo']
		
def main():
    """Entry point for the application script"""
    print("Rouigram :)")
