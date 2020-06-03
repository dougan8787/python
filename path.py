import os

def split_path(path):
    result = []
    while True:
        head,tail = os.path.split(path)
        if tail:
          result.insert(0,tail)
          path = head
        else:    #到達根目錄時
          head = head.strip('/:\\')  
          result.insert(0,head)
          break
    return result    
