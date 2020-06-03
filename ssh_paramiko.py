import threading
import paramiko
import subprocess

def ssh_command(ip,user,passwd,command): #建立ssh_command函數
    client = paramiko.SSHClient() #連接一台SSH伺服器
    #client.load_host_keys('/home/justin/.ssh/known_hosts') 執行單一指令 paramiko支援金鑰
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #取代或配合密碼認證
    client.connect(ip,username = user,password = passwd)#沿用傳統使用者名稱及密碼
    ssh_session = client.get_transport().open_session() #自動接受連現
    if ssh_session.active: #連現ssh伺服器的金鑰
        ssh_session.exec_command(command)   #建立連現
        print(ssh_session.recv(1024))       #印出連線狀態 
    return

ssh_command('192.168.100.131','justin','lovesthepython','id') #呼叫ssh_command函式傳入command,範例為id
