import os
outputdata = 'helloworld'
dir = os.path.join(os.path.dirname(__file__), '../assets')

def guessFileType(fileName):
  if fileName.endswith('ico'):
    return 'image/x-icon'
  elif fileName.endswith('html'):
    return 'text/html'
  elif fileName.endswith('json'):
    return 'text/json'
  elif fileName.endswith('css'):
    return 'text/css'
  elif fileName.endswith('js'):
    return 'application/javascript'
  else:
    return None

def HTTPHandler(conn):
  message = conn.recv(1024)
  print('message: ', message)

  if not message:
    return

  lines = message.split()
  
  method = lines[0].decode()
  if method != 'GET':
    header = 'HTTP/1.1 404 Not Found'
    conn.send(header.encode())
    return

  route = lines[1].decode()
  if route == '/':
    route = '/index.html'

  outputdata = None
  filePath = dir + route
  try:
    print('loading file: ', filePath)
    outputdata = open(filePath, 'rb').read()
  except IOError:
    print('File not exist! ', route)
    header = 'HTTP/1.1 404 Not Found'
    conn.send(header.encode())
    return

  fileType = guessFileType(route) or 'text/plain'
  header = 'HTTP/1.1 200 OK\nConnection: close\nContent-Type: %s\nContent-Length: %d\n\n' % (fileType, len(outputdata))

  conn.send(header.encode())
  conn.send(outputdata)
  return
