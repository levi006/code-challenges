import requests
from pprint import pprint

# given this json document url, compute some basic things
feed_url = 'https://jsonfeed.org/feed.json'
# 1. fetch the file over https
# 2. recursively count the total number of keys (15)
# 3. determine the key with the largest value (in terms of characters in the value)

#download the response
#count the keys
#tells you how many keys in whole response, deeply nested
#find key with largest string value


response = requests.get(feed_url)
json = response.json()
pprint(json)
pprint(json.keys())


d = {'a': {'b': 'c'}}


def all_keys(d):
  keys = []
  if isinstance(d, dict):
    for k in d:
      keys.append(k)
      keys.extend(all_keys(d[k]))
  elif isinstance(d, list):
    for v in d:
      keys.extend(all_keys(v))
  else:
    # d is string, int, null, ...
    pass
  return keys



# smallest problem is: is this value at this key a dictionary? 

def count_keys(json):
    
    if isinstance(json, dict):
        for k in json:
            # do something
            # key_count = key_count + 1 + count_keys(json[k])
    
# keys=[]
    
# while there are parent nodes/keys
# iterate through the nodes
# check current node
# if current node has children(keys)
# add current node to keys 
# check current.children 
    

    #conditions:
    def check_keys():
    # if value is string:
    #    add the key  
    # if value is a dictionary:
    #    iterate over the keys
    # if value is an array:
    #    iterate over items in list
    #    return keys   


