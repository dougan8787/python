def InitIO(handle):
    readers = {
        bytes: StringIO,
        io.IOBase: FileIO,
        socket.socket:NetworkIO,
        }
    return readers.get(type(handle),lambda n:None)(handle)
