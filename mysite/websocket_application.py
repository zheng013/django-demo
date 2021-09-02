async def websocket_application(scope,receive,send):
  while True:
    msg=await receive()
    type=msg['type']
    print(msg)
    if type=='websocket.connect':
        await send({'type':'websocket.accept'})
    elif type=='websocket.receive':
        if msg['text']=='ping':
          await send({'type':'websocket.send','text':'pong'})
    elif type=='websocket.disconnect':
      break
    else:
      pass
  print('[disconnect]')
