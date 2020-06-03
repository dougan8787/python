for tag,sendAction in fileInfo:
    backTag = None

    try:
        self.send_tag(tag)
        self.recv_data()
    except InOutException as e:
        backTag = e.args[0]
    except Exception as e:
        self.send_tag(FILE_ABOUT_TAG)
        break
    error = None
    if not sendAction: continue
    try:
        sendAction()
        self.recv_data
     except InOutException as e:
        backTag = e.args[0]
    except Exception as e:
        error = FILE_ABOUT_TAG
        break
    if error:
        self.send_tag(error)
        return False
    if backTag != FILE_SUCCESS_TAG:
        return False
return True
