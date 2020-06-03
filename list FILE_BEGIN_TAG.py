
if fileSize > self.blockSize:
    fileTag,fileSend = (FILE_BLOCKS_TAG, lambda:self.send_blocks(path),)
else:
    fileTag,fileSend = (FILE_CONTENT_TAG,lambda:self.send_content(path),)

fileInfo = [(FILE_BEGIN_TAG, None,),
            (FILE_NAME_TAG, lambda:self.send_name(fileName),),
            (FILE_SIZE_TAG, lambda:self.send_size(fileSize),),
            (fileTag,fileSend,),
            (FILE_END_TAG, None,),]
