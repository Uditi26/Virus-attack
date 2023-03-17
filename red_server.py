import socket
import pickle

HOST = ""  # Standard loopback interface address (localhost)
PORT = 25698  # Port to listen on (non-privileged ports are > 1023)

TTT=[[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]]
win=0
t=1

def print_board():
    global TTT
    for i in TTT:
        print(i)

def send_msg(sock):
    # Prefix each message with a 4-byte length (network byte order)
    row,column=input().split()
    row = int(row)
    column = int(column)
    global TTT,win
    TTT[row][column]=1  
    move = pickle.dumps(TTT)
    #msg = struct.pack('>I', len(msg)) + msg
    win=win_or_pass(row,column)
    sock.sendall(move) 

def recv_data(sock):
    data=sock.recv(4096)
    global TTT
    TTT=pickle.loads(data)
    print_board()


def win_or_pass(r,c):
    global TTT,check 
    check = 0
    
    for i in range(3):
        if(TTT[i][c]==t):
            check=1 
            continue 
        else:
            check=0 
            break

    if(check==0):
        for i in range(3):
            if(TTT[r][i]==t):
                check=1
                continue 
            else:
                check=0
                break

    if(check==0 and r==c):
        for i in range(3):
            if(TTT[i][i]==t):
                check=1
                continue
            else:
                check=0
                break 

    if(check==0 and r+c==2):
        for i in range(3):
            if(TTT[i][2-i]==t):
                check=1
                continue 
            else:
                check=0 
                break
    return check

 

 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        try:
            for i in range(0,5):
                print(f"Connected by {addr}")
                send_msg(conn)
                if (win==1):
                    print("You won")
                    
                    break
                else:
                    recv_data(conn)
           
        except Exception:
             if(check==0):
                print("Draw")
             else:
                print("You Lost") 
