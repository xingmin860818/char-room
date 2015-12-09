import socket,select,string,sys

def prompt():
        sys.stdout.write('<You> ')
        sys.stdout.flush()

if __name__ == '__main__':
        if (len(sys.argv)) < 3:
                print 'Usage: python client.py hostname port'
                sys.exit()
        host = sys.argv[1]
        port = int(sys.argv[2])

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(2)
        #connect to remote host
        try:
                s.connect((host,port))
        except:
                print 'Unable to connect'
                sys.exit()
        print 'connected to remote host. Start sending message'
        prompt()

        while True:
                rlist = [sys.stdin,s]
                #get the list sockets which are reachable
                read_list,write_list,error_list = select.select(rlist,[],[])
                for sock in read_list:
                        if sock == s:
                                data = sock.recv(4096)
                                if not data:
                                        print '\nDisconnected from chat server'
                                        sys.exit()
                                else:
                                        #print data
                                        sys.stdout.write(data)
                                        prompt()
                        #user entered a message
                        else:
                                msg = sys.stdin.readline()
                                s.send(msg)
                                prompt()
