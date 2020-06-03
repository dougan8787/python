essential_flag={FILE_NAME_TAG:1,FILE_SIZE_TAG:2,
                FILE_CONTENT_TAG:4,FILE_BLOCKS_TAG:4}


flag = sum([essential_flag.get(x) for x in result.keys()])

if flag !=7: result = None

return result
