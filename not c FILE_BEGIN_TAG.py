try:
    self.send_tag(FILE_BEGIN_TAG)
except InOutException as e:
    print('Exception:',str(e))
    if FILE_SUCCESS_TAG not in e.args:
        continue
    except Exception as e:
        print('Exception:',str(e))
        self.send_tag(FILE_ABORT_TAG)
        continue
    try:            #後面都一樣的try....except
        self.send_tag(FILE_NAME_TAG)
        self.send_name(fileName)
    except InOutException as e:
    print('Exception:',str(e))
    if FILE_SUCCESS_TAG not in e.args:
        continue
    except Exception as e:
        print('Exception:',str(e))
        self.send_tag(FILE_ABORT_TAG)
        continue
    
