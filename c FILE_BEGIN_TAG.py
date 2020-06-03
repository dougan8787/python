self.send_tag(FILE_BEGIN_TAG)
self.send_tag(FILE_NAME_TAG)
self.send_name(fileName)
self.send_tag(FILE_SIZE_TAG)
self.send_size(fileSize)

if fileSize > self.blockSize:
    self.send_tag(FILE_BLOCKS_TAG)
    self.send_blocks(path)
else:
    self.send_tag(FILE_CONTENT_TAG)
    self.send_content(path)
self.send_tag(FILE_END_TAG)
