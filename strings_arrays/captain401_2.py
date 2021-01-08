
# take in a json string with comments that start with "//"
# return string with comments removed 
"""Valid for transforming the comment into string

 >>> del_comments({
  "key1": "value1",   // this is a comment
  "urls": ["https://captain401.com"]
})

{
  "key1": "value1",
  "urls": ["https://captain401.com"]
}


"""
json_str = """
    {
      "key1": "value1",   // this is a comment
      "urls": ["https://captain401.com"]
    }
    """

def get_comment_indices(split_json):

  for item in split_json:
      print(item)
      comment_index = item.index("\n")
      comment_indices.append(comment_index)
  return comment_indices

def del_comments(json_str):
    
    split_json = json_str.split("// ")
    get_comment_indices(split_json)
        
    processed = ""
    
    for item in split_json:
      for char in item:
        del_idx = comment_indices.pop(0)
        stripped = item[: del_idx]

        processed.join(stripped)
    return processed


del_comments(json_str)    
    

# if __name__ == '__main__':
#     import doctest
#     if doctest.testmod().failed == 0:
#         print("\n*** ALL TESTS PASSED. !\n") 