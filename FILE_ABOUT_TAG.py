self.send_tag(FILE_NAME_TAG)    #送出檔名標籤
self.send_name(fileName)        #送出檔案名稱
self.send_tag(FILE_SIZE_TAG)    #送出檔案大小標籤
self.send_size(filesize)        #送出檔案大小

if filesize > self.blockSize:
    self.send_tag(FILE_BLOCKS_TAG)  #太大用區塊傳
    self.send_blocks(path)
else:
    self.send_tag(FILE_CONTENT_TAG) #小檔整個傳
    self.send_content(path)
self.send_tag(FILE_END_TAG)
