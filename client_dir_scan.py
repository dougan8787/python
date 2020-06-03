visited={}

for filename in scan_dir(start_dir):
    filesize = os.path.getsize(filename)    #檔案大小
    filetime = os.path.getmtime(filename)   #檔案修改時間
    singature = [filesize,filemtime]        #合成判斷值
    if visited.get(filename) == signature:  #判斷是否存在、相同
        continue    	                    #相同就不傳
    handler.send_file(filename)
    visited[filename] = signature           #更新判斷值
