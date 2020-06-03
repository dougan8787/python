def recv_file(self):
    while True:
        
        tag = None
        
        try:
            
            data = self.recv_data()#無用資料
            if not data: break #沒資料了，結束
            continue
        
        except InOutException as e :
            
            tag =e.args[0]  #取得檔案標籤
            
        except socket.error:  #網路的錯誤無法這裡解決
            
            
            return
        
        except Exception as e:
            
            print('Exception:',str(e))
            break
        
        if not tag :continue   #不是標籤，重新取得
        
        try:
            
            data = self.recv_data()

        #取得檔案資料
            if not data:break     #沒資料就是停止了
            result[tag] = data   #有資料就加入傳回值
            
        except InOutException as e:
            
            tag   = e.args[0] #取得檔案標籤
            break  #這裡不該取得標籤，無論是什麼，都中斷
        
        except socket.error: #網路的錯誤無法這裡解決
            
            return
        
        except InOutExcption as e:
            
            print('Exception:',str(e))
            tag  = e.args[0]
            
        if not tag : continue
        
        elif tag == FILE_BEGIN_TAG: #檔案傳送開始
            
            
            result = {} #result 初始化
            
            self.send_success()
            
        elif tag == FILE_END_TAG:
            
             self.send_success()
             break
            
        elif tag == FILE_ABORT_TAG:
            
             break      #跳出迴圈
            
        if not result: #客戶端如果結束、中斷連線，result會是空的
            
                       
           result = None
            
        else:

            if FILE_NAME_TAG not in result:    #缺了檔名
                
                print('name not found',result)
                result = None
                
            elif FILE_SIZE_TAG not in result: #缺了檔案大小

                print('size not found',result)
                result = None

            elif FILE_CONTENT_TAG not in result and FILE_BLOCKS_TAG not in result:   #缺了檔案內容

                print('content not found',result)
                result = None
                
            response = FILE_SUCCESS_TAG if result else FILE_FAIL_TAG

            self.send_tag(response)   #沒缺資料就傳成功，否則傳送失敗
                
        if tag == FILE_NAME_TAG:
            
             data = self.recv_data()
             
        elif tag == FILE_SIZE_TAG:

             data = self.recv_size()
             
        elif tag == FILE_CONTENT_TAG:
            
             data = self.recv_content()
             
        elif tag == FILE_BLOCKS_TAG:

             data = self.recv_blocks()
             
                     
        else:
               break
        if not data :
                 break
        result[tag] = data

        
def send_file(self,path):
    
    filename = '\t'.join(split_path(path))
    filesize = os.path.getsize(path)
    filedata = open(path,'rb').read()
    
    try:


def send_blocks(self,fileName):
    fp = open(fileName,'rb')
    blockID =0
    totalSize = 0
    while True:
        block = fp.read(self.blockSize) #讀檔
        if not block:break              #沒資料就是結束
        blockID +=1                     #區塊編號
        self.send_data(blockID)         #送出區塊編號
        self.send_data(block)           #送出檔案區塊
        backID =self.recv_data()
        if backID !=blockID:
            self.send_fail()
            break
        totalSize += len(block)
    self.send_data(0)
    return totalSize

def recv_blocks(self):
    totalSize = 0
    lastBlockID = 0
    fileName = os.path.abspath(os.path.join(self.savePath,'TEMP%x' % int(time.time())))   #決定暫存檔名
    dirname = os.path.dirname(fileName)
    if not os.path.exists(dirname):     #產生目錄
        os.makedirs(dirname)
    while open(fileName,'wb') as fp:
        blockID = self.recv_data()      #取得區塊編號
        if not isinstance(blockID,int): #要求是數字形態
            
raise TypeError('invalid type of block id %s'% type(blockID))
        if blockID ==0:                 #結束編號
            break
        if lastBlockID + 1 != blockID:  #比對編號是否正確
           raise ValueError('block ID error last:%d current:%d'%d(lastBlockID,blockID))
        lastBlockID = blockID          #記下編號
        block = self.recv_data()       #收取資料
        if not isinstance(block,bytes): 
            raise TypeError('invalid type of block id %s'%type(blockID)) #資料應該是bytes
        if len(block) + totalSize > self.maxSize:               #收取資料總數太大，產生例外
            raise RuntimeError('exceed max file size limit')
        fp.write(block)       #寫進暫存檔
        self.send_data(blockID)
return fileName        
      
def save_file(fileInfo,target):
    filename = fileInfo.get(FILE_NAME_TAG)
    filesize = fileInfo.get(FILE_SIZE_TAG)
    content  = fileInfo.get(FILE_CONTENT_TAG)
    if filename and fileszie and content:
    if content or tempFile:       #有content 或是暫存檔
        fullName = os.path.join(target,fileName)
        dirname = os.path.dirname(fullName)
        if not os.path.exists(dirname):  #建立存檔目錄
            os.makedirs(dirname)
        if content:          #如果content就存到檔名
           if len(content) !=filesize:
            raise RuntimeError('size unmatched')
           with open(fullname,'wb') as fp:
            fp.write(content)
        else:             #如果是暫存檔，將暫存檔檔名改成真正檔名
            if os.path.getsize(tempFile) !=fileSize:
                raise RuntimeError('size unmatched')
            shutil.move(tempFile,fullName)
       return True
    else:             #沒內容也沒暫存檔，檔案傳送是失敗
        return False
        
