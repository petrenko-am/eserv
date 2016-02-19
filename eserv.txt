import socket                                                                   
                                                                                
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                           
s.bind(('127.0.0.1', 2222))                                                     
s.listen(5)                                                                     
while True:                                                                     
    client, address = s.accept()                                                
    data = s.recv(1024)                                                         
    if data.find('close') != -1 or data.find('Close') != -1:                    
        client.close()                                                          
        s.close()                                                               
        break;                                                                  
    if data:                                                                    
        clinet.send(data)