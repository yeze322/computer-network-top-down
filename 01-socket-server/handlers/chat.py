def chatHandler(conn):
  while True:
    try:
      data = conn.recv(1024)
    except:
      print('Err at recv', flush=True)
      break

    print('<< ', data, flush=True)
    if data:
      try:
        conn.sendall(data + b'heheda')
      except Exception as err:
        print('Err at sendall', err, flush=True)
        break
    else:
      print('Empty data, Client closed')
      break
  return
