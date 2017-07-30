outputdata = 'helloworld'

def HTTPHandler(conn):
  message = conn.recv(1024)
  print('message: ', message)
  if not message:
    return
  outputdata = open('index.html').read()
  header = 'HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outputdata))
  conn.send(header.encode())
  conn.send(outputdata.encode())
  return
