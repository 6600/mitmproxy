import json
import asyncio
import requests
import websockets

websocketClient = []



linkList = {}

async def hello(uri):
  global linkList
  global websocketClient
  async with websockets.connect(uri) as websocket:
    
    print('服务器连接成功!')
    # await websocket.send("Hello world!")
    while True:
      message = await websocket.recv()
      data = json.loads(message)
      # test = websocket.read_message()
      # print(json.dumps(test))
      # 获取url
      # resource = data['resource']
      # print(data)
      if ('data' in data and 'request' in data['data']):
        remote_address = data['data']['client_conn']['address'][0]
        # 获取URL
        request = data['data']['request']
        url = '%s://%s%s' % (request['scheme'], request['host'], request['path'])
        ind = 0
        for client in websocketClient:
          # 判断是否是拦截的url
          for item in client['config']['intercept']:
            if (item in url and data['cmd'] == 'update' and 'response' in data['data'] and data['data']['response']['timestamp_end']):
              messageId = data['data']['id']
              # 判断是否有缓存
              if ('tempList' not in client):
                client['tempList'] = []
              # 判断是否已经命中了缓存
              if (messageId in client['tempList']):
                break
              # 设置缓存
              client['tempList'].append(messageId)
              if ('needBody' in client['config']):
                response = requests.get('http://127.0.1.1:8081/flows/' + messageId + '/response/content.data', headers={})
                response.encoding='utf-8'
                response2 = requests.get('http://127.0.1.1:8081/flows/' + messageId + '/request/content.data', headers={})
                response2.encoding='utf-8'
                data['data']['request']['data'] = response2.text
                data['data']['response']['data'] = response.text
              # print(message)
              
              data['data']['request']['url'] = url
              try:
                await client['client'].send(json.dumps(data['data']))
              except:
                del websocketClient[ind]
              ind += 1


async def echo(websocket, path):
  global linkList
  async for message in websocket:
    message = json.loads(message)
    if (message['type'] == 'login'):
      print(message)
      websocketClient.append({
        "config": message,
        "tempList": [],
        "client": websocket
      })
    # 
    # await websocketClient[0].send(message)

print('服务端启动')
asyncio.get_event_loop().run_until_complete(websockets.serve(echo, '0.0.0.0', 8082))
asyncio.get_event_loop().run_until_complete(hello('ws://127.0.0.1:8081/updates'))
asyncio.get_event_loop().run_forever()
