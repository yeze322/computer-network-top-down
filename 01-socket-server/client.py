import socket

HOST = 'localhost'
PORT = 6666

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  while True:
    userInput = None
    try:
      userInput = input('>> ')
    except (KeyboardInterrupt, EOFError):
      print('End chat')
      s.close()
      break

    byteString = str.encode(userInput) + b'.'
    s.send(byteString)
    data = s.recv(1024)
    print('- ', data, flush=True)
    if not data or data == b'EOF':
      print('Finish data')
      s.close()
      break
