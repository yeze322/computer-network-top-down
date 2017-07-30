import os
import sys
import time
import socket
from multiprocessing import Process
from handlers.chat import chatHandler

def userInterruptHandler():
  while True:
    try:
      ss = input('.....')
      print(ss)
    except KeyboardInterrupt:
      print('Goodbye')
      break
    except Exception as err:
      print(err)
      break

def socketMain(connHandler):
  HOST = 'localhost'
  PORT = 6666

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
      conn, addr = s.accept()
      print('[Connected]: ', addr)
      connHandler(conn)
      print('[Disconnect]: ', addr)
      conn.close()

if __name__ == '__main__':
  p_socket = Process(target=socketMain, args=(chatHandler,))
  p_socket.start()
  print('Socket process running... PID: ', p_socket.pid)
  print('Bg process is running... PID: ', os.getpid())

  userInterruptHandler()
  print('Quit...')
  p_socket.terminate()
  