if isinstance(filename,str):
    dirname = os.path.dirname(filename)   #獲取目錄和檔案名
    if not os.path.exists(dirname):      #如果沒有這檔案
        os.makedirs(dirname)            #就創一個
    with open(filename,'w') as fp:      #把檔案以寫的方式打開
        json.dump(visited,fp)           #將python物件轉換成JSON並寫入檔案
        
if isinstance(filename,str) and os.path.exists(filename):#把更新的檔案傳上來
    
    with open(filename) as fp:  	#打開檔案

        visited=json.load(fp)           #將JSON轉換成python物件
