from mitmproxy import ctx
import re
import http.client
import json,os
import datetime

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
    "url": "http.*://office.chaoxing.com/data/apps/seat/config",
    "hack": [
      [
        '"reserveBeforeDay":1', 
        '"reserveBeforeDay":3'
      ]
    ]
  },
  {
    "url": "http.*://office.chaoxing.com/front/apps/seat/select",
    "hack": [
      [
        '提交</p>', 
        '''提交</p>
        <p class="order_submit" style="position: fixed;bottom: 20%;width: 20vw;height: 30px;line-height: 30px;right: 2%;bottom:13%;z-index:999;" v-if="chosedSeatNum != ''"onclick="owoseet()">保存抢座</p>
        <div id="owo3" style="display:none">{{chosedSeatNum}}</div>
        '''
      ],
      [
        'return dateArr',
        '''
        window.roomID = id
        return dateArr
        '''
      ],
      [
        '</body>',
        '''
        <script>
          let seatList = new Set()
          function owoseet (e) {
            const userCookie = document.querySelector('#resCookie').innerText
            const roomID = window.roomID
            seatList.add(document.querySelector('#owo3').innerText)
            var usernameS = localStorage.getItem('username')
            var sessionS = localStorage.getItem('session')
            const sendData = JSON.stringify({
              username: usernameS,
              session: sessionS,
              type: '学习通',
              value: {
                cookie: userCookie,
                roomID: roomID,
                seat: Array.from(seatList)
              }
            })
            fetch(`//going.run/userServer?route=updata`, {
              method: 'POST',
              headers: {
                "Content-Type": "application/json"
              },
              body: sendData
            }).then((response) => {return response.json();}).then((res) => {
              if (res.err === 0) {
                var r=confirm(`您已将${Array.from(seatList).length}个座位加入后台列表，点击确认跳转后台自助抢座，取消可继续添加座位`);
                if (r==true) {
                  window.location.href = 'http://cunchu.site/work/debug/index.html'
                }
              } else {
                alert(`保存失败: ${res.message}`)
              }
              outInfo()
            })
          }
        </script>
        '''
      ],
      [
        "if (!_this.submitStatus) {",
        "if (false) {"
      ],
    ]
  },
  {
    "url": ".*/ticketapi.sxhm.com/api/ticket/calendar",
    "hack": [
      [
        '"tp_last_stock_nfree":0', 
        '''"tp_last_stock_nfree":100'''
      ],
      [
        '"tp_last_stock":0', 
        '''"tp_last_stock":100'''
      ],
    ]
  },
  {
    "url": ".*/ticketapi.sxhm.com/api/ticket/detail",
    "hack": [
      [
        '"tp_last_stock":0', 
        '''"tp_last_stock":100'''
      ],
    ]
  },
  {
    "url": ".*/clientweb/m/ic2/default.aspx|office.chaoxing.com/front/apps/seat/index",
    "hack": [
      [
        '</body>', 
        '''
        <link charset="utf-8" rel="stylesheet" href="https://cunchu.site/work/login/mini.css">
        <script src="https://cunchu.site/work/login/mini.js" type="text/javascript" charset="UTF-8"></script>
        </body>
        '''
      ],
    ]
  },
  {
    "url": ".*/clientweb/m/a/resvsub.aspx",
    "hack": [
      [
        '<div class="content-block">', 
        '''
        <div class="" id="xinxi" style="height: 150px;">抢座信息</div>
        <script>
        function zidong () {
          alert('sd')
          // alert(app.formToJSON(fm[0]))
        }
        </script>
        '''
      ],
    ]
  },
  {
    "url": ".*/ic.ctbu.edu.cn/clientweb/m/ic2/app.js",
    "hack": [
      [
        'if (fm.mustItem())', 
        '''pro.confirm = function(text, callBack) {callBack()};
        if (!window.cishu) window.cishu = 1
        pro.msgBox = function(text) {document.querySelector('#xinxi').innerText = `[${window.cishu++}] ${text}`;}
        if (true)'''
      ]
    ]
  },
  {
    "url": ".*/ticket.sxhm.com/mm/ticketOrder/selectTicket",
    "hack": [
      [
        '</body>', 
        '''
        <script src="//cunchu.site/work/script/%E9%99%95%E8%A5%BF%E5%8E%86%E5%8F%B2%E5%8D%9A%E7%89%A9%E9%A6%86.js"></script>
        </body>
        '''
      ],
    ]
  },
  {
    "url": ".*/wechat.laixuanzuo.com/index.php/reserve/index.html|.*/wechat.laixuanzuo.com/index.php/prereserve/index.html",
    "hack": [
      [
        '</body>', 
        '''
        <script src="//cunchu.site/work/script/%E6%9D%A5%E9%80%89%E5%BA%A7.js"></script>
        </body>
        '''
      ],
    ]
  },
  {
    "url": ".*/wechat.v2.traceint.com/index.php/reserve/index.html|.*/wechat.v2.traceint.com/index.php/prereserve/index.html",
    "hack": [
      [
        '</body>', 
        '''
        <script src="//web-1251887489.cos.ap-shanghai.myqcloud.com/wqtsg.js"></script>
        </body>
        '''
      ],
    ]
  },
  # 天津大学我去图书馆
  {
    "url": ".*/seatw.lib.tju.edu.cn/index.php/reserve/index.html|.*/seatw.lib.tju.edu.cn/index.php/prereserve/index.html",
    "hack": [
      [
        '</body>', 
        '''
        <script src="https://cdn.bootcdn.net/ajax/libs/vConsole/3.4.0/vconsole.min.js"></script>
        <script>
            // init vConsole
            alert(VConsole)
            var vConsole = new VConsole();
        </script>
        <script src="//cunchu.site/work/script/%E6%B4%A5%E5%A4%A7.js"></script>
        </body>
        '''
      ],
    ]
  },
  # 一考即过
  # {
  #   "url": ".*/leosys.cn/hlju/rest/v2/room/layoutByDate",
  #   "hack": [
  #     [
  #       '"local":true', 
  #       '"local":false'
  #     ],
  #   ]
  # },
  {
    "url": ".*/web.traceint.com/web/index.html",
    "hack": [
      [
        '</body>', 
        '''
        <script src="//cunchu.site/work/script/wqtsg.js"></script>
        </body>
        '''
      ],
    ]
  },
  {
    "url": ".*/app.papa.com.cn/js/chunk-",
    "hack": [
      [
        't.next=12;', 
        '''t.next=8;'''
      ],
    ]
  },
  {
    "url": ".*/api.wesais.com/field/wxFieldBuyPlan/getList",
    "hack": [
      [
        '"is_lock":true', 
        '''"is_lock":false'''
      ],
      [
        '"is_overdue":true', 
        '''"is_overdue":false'''
      ],
      [
        '"lock_status":0', 
        '''"lock_status":204'''
      ],
      [
        '"price":0', 
        '''"price":"55.00"'''
      ],
    ]
  },
  {
    "url": ".*/app.papa.com.cn/js/chunk-",
    "hack": [
      [
        'disabled:!!t.controlTime', 
        'disabled:!!false'
      ],
      [
        'if(!this.controlTime)', 
        'if(true)'
      ]
    ]
  },
  {
    "url": ".*/ClientWeb/pro/ajax/device.aspx",
    "hack": [
      [
        '"state":"undo"', 
        '"state":"open"'
      ],
      [
        '"state":null', 
        '"state":"open"'
      ],
      [
        '"freeSta":-3',
        '"freeSta":0',
      ],
      [
        '"freeSta":-2',
        '"freeSta":0',
      ],
      [
        '"freeSta":-1',
        '"freeSta":0',
      ],
      [
        '"state":"close"', 
        '"state":"open"'
      ],
      [
        '"runsta":6', 
        '"runsta":0'
      ],
      [
        '}]}],',
        '}],"ts":[]}],'
      ]
    ]
  },
  # 盐湖图书馆
  {
    "url": "//yclib.reserve.alb.letoochina.cn/Reserve/getReservationTime",
    "hack": [
      [
        '"available":0', 
        '"available":9'
      ],
    ]
  },
  {
    "url": "//yclib.reserve.alb.letoochina.cn/Reserve/getDesks",
    "hack": [
      [
        '"reservable":false', 
        '"reservable":true'
      ],
    ]
  },
  # 车辆预约
  {
    "url": ".*//mmyx.mmsh.sinopec.com/Booking/GetBookingPlanList",
    "hack": [
      [
        '"BookedNum":10', 
        '"BookedNum":0'
      ],
      [
        '"BookedNum":11', 
        '"BookedNum":0'
      ],
      [
        '"BookedNum":12', 
        '"BookedNum":0'
      ],
    ],
  },
  # 医院预约
  {
    "url": ".*//wx.whyyy.com/MicroSY/reservegh",
    "hack": [
      [
        '"status":"2"', 
        '"status":"7"'
      ],
      [
        '"status":"6"', 
        '"status":"7"'
      ],
      [
        '"regFlag":-1', 
        '"regFlag":1'
      ]
    ],
  },
  {
    "url": "http://mmyx.mmsh.sinopec.com/Booking/BookingPlanM",
    "hack": [
      [
        '<script src="../../Scripts/ControlScripts/loading.js"></script>', 
        '''
<script src="../../Scripts/ControlScripts/loading.js"></script>
<script>
setTimeout(() => {
    $("#AfterBnt").css("background-color", "#ff4a1f");
    ISAFTERORDER = true;
    $("#PerBnt").css("background-color", "#ff4a1f");
    ISBEFORORDER = true;
}, 500);
</script>
        '''
      ]
    ],
  },
  {
    "url": "http://mmyx.mmsh.sinopec.com/Booking/BookingSubmitM",
    "hack": [
      [
        '<button class="bnt" style="height: 1.3rem;" id="ConfirmBnt" onclick="SubmitOrder()">', 
        '''
<input type="datetime-local" id="clock" />
<h3>延迟提交参数(单位秒)</h3>
<input type="number" id="yanchi" value="0">
<button class="bnt" style="height: 1.3rem;" id="zhengdian" onclick="tanchu()">
  整点提交
</button>
<button class="bnt" style="height: 1.3rem;" id="jiankong" onclick="jiankong()">
  监控提交
</button>

<script>
function getYZM (imgEl, callBack) {
    imgEl.crossOrigin = "anonymous";
    var canvas = document.createElement("canvas");
    var ctx = canvas.getContext("2d");  
    ctx.drawImage(imgEl, 0, 0);
    var dataURL = canvas.toDataURL('image/png');
    var base64Data = dataURL.split(',')[1]
    

    fetch("http://hanshu.run/yzmb", {
    method: 'POST',
    body: base64Data
    }).then(response => response.json())
    .then(result => {
      if (callBack) callBack(result.data.result)
    })
    .catch(error => console.log('error', error));
}

function getQueryVariable(variable, url) {
  var query = window.location.search.substring(1);
  if (url) {
    query = url.split('?')[1]
  }
  var vars = query.split("&");
  for (var i=0;i<vars.length;i++) {
          var pair = vars[i].split("=");
          if(pair[0] == variable){return pair[1];}
  }
  return(false);
}

let checkIndex = 0
function jiankong () {
  // getQueryVariable(, resReferer)
  var requestOptions = {
    method: 'GET',
    redirect: 'follow'
  };

  fetch(`http://mmyx.mmsh.sinopec.com/Booking/GetBookingPlanList?ProductID=${getQueryVariable('productID', resReferer)}&ShipPlaceID=${getQueryVariable('qYShipPlaceID', resReferer)}&BookingDate=${getQueryVariable('date')}&PreTruckNo=%E7%B2%A4K53676&LadingBillID=${getQueryVariable('Id', resReferer)}`, requestOptions)
    .then(response => response.json())
    .then(result => {
      let next = true
      result.forEach(element => {
        if (element.ID == getQueryVariable('PlanID')) {
          if (element.BookedNum >0) {
            next = false
            refreshCode()
            setTimeout(() => {
              getYZM(document.querySelector('#ImageCheck'), (yzm) => {
                document.querySelector('#InpCode').value = yzm
                AddBooking()
              })
              window.newAlert = function (text, type, callback) {
                if (text.includes('确认') && callback) {
                  callback()
                } else {
                  alert(text)
                }
              }
            }, 2000);
          }
        }
      });
      if (next) {
        checkIndex++
        document.querySelector('#jiankong').innerText = `检查次数:${checkIndex}`
        setTimeout(() => {
          jiankong()
        }, 5000);
      }
    })
    .catch(error => console.log('error', error));
}

function tanchu() {
  function getLocalTime(nS) {  
    return new Date(parseInt(nS)).toLocaleString().replace(/:\d{1,2}$/,' ');  
  }
  var yzmCh = false
  var data = new Date(document.querySelector('#clock').value.replace(/-/g,'/').replace('T',' ')).valueOf()
  var zhengdian = document.querySelector('#zhengdian')
  // alert(getLocalTime(data))
  function tempClock () {
    var cha = data - Date.now() - parseInt(document.querySelector('#yanchi').value * 1000)
    if (cha < 15000 && !yzmCh) {
      yzmCh = true
      refreshCode()
      setTimeout(() => {
        getYZM(document.querySelector('#ImageCheck'), (yzm) => {
          document.querySelector('#InpCode').value = yzm
        })
        window.newAlert = function (text, type, callback) {
          if (text.includes('确认')) {
            if(callback) callback()
            return
          }
          alert(text)
          if (callback) callback()
        }
      }, 2000);
    }
    if (cha > 200) {
      zhengdian.innerText = cha
      setTimeout(() => {
        tempClock()
      }, 100);
    } else {
      AddBooking()
    }
  }
  tempClock()
}
</script>
<button class="bnt" style="height: 1.3rem;" id="ConfirmBnt" onclick="SubmitOrder()">
        '''
      ]
    ],
  },
  # iobx
  {
    "url": ".*//www.ibox.art/zh-cn/item",
    "hack": [
      [
        '''</body>''',
        '''
        <script src="//cunchu.site/work/script/ibox.js" defer></script>
        </body>
        '''
      ]
    ]
  },
  {
    "url": "get_my_servertime",
    "hack": [
      [
        '''''',
        '''{"ret":1,"act":"get_my_servertime","msg":"ok","data":["2021-10-29","12:11"],"ext":null}'''
      ]
    ]
  },
  # 座位预约App
  {
    "url": ".*//zwyy-lib.chzu.edu.cn:9091/tsgintf/main/service|.*//220.180.184.9:9091/tsgintf/main/service",
    "hack": [
      [
        '''<script type="text/javascript">''', 
        '''<script type="text/javascript">
        
        api.showProgress = function (e) {console.log(e);checkSubmitFlg = false;}
        let allowList = ["2018213345", "2018212065", "2018210406", "2016214105", "2018211147", "2018211026", "2019214347", "2018214474", "2018210624", "2018210215", "2018212107", "2018211452", "2018211793", "2019214146", "2020220440", "2018210861", "2018210344", "2019211932", "2018210332", "2018210360", "2019211984", "2018211008", "2018210087"]
        if (allowList.includes(_key)) {
          alert('载入成功，现在关闭代理功能也可以使用功能，并获得更快速度。点击座位即可完成原来长按确认的操作，开抢前几秒一直点击基本可以预约到座位。')
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
  {
    "url": ".*//wmatch-api-1210.wangqiuban.cn/weather!getDateWeatherBySku",
    "hack": [
      [
        ''']}''',
        ''',{"week":"\xe6\x98\x9f\xe6\x9c\x9f\xe5\x9b\x9b","date":"''' + nextDaySecurity(8) + '''","weather":"\xe5\xa4\x9a\xe4\xba\x91","type":"PARTLY_CLOUDY_DAY"}]}''',
      ]
    ]
  },
  {
    "url": ".*//leosys.cn/hlju/rest/v2/free/filters",
    "hack": [
      [
        '"]},',
        '","' + nextDay(1) + '"]},',
      ]
    ]
  },
  {
    "url": ".*//www.360banke.com/xiaotu/Seatresv/GetResvInfo.asp",
    "hack": [
      [
        ']}]}',
        ']},{"date": "' + nextDay(1) + '","weekday": "\xd0\xc7\xc6\xda\xc8\xfd","start": "07:00","end": "22:30","timeslot": ["07:00","22:30"]}]}',
      ]
    ]
  }
]

reqHackList = [
  # 座位预约
  # ".*//211.70.171.14:9999/tsgintf/main/service",
  # ".*//zwyy-lib.chzu.edu.cn:9091/tsgintf/main/service"
  "http://sw.xianmaigu.com/api/YySeatAppointment/addes.html",
  "https://prod.zixishi.tech/srapi/app/member/supplier-or-merchant-info/v1/2/211"
]


class ModifyResponse:

  def response(self,flow):
    for item in hackList:
      if ('url' in item and flow.request.url):
        findList = pattern = re.compile(item['url']).findall(flow.request.url)
        if (len(findList) > 0):
          ctx.log.info('请求被重写:' + flow.request.url)
          # flow.response.headers['Expires'] = 0
          flow.response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate'
          flow.response.headers['Pragma'] = 'no-cache'
          returnText = flow.response.text
          # print(returnText)
          if ('</body>' in returnText):
            returnText = returnText.replace('</body>', '''<div id="resCookie" style="display: none;">%s</div>\r\n<script>var resCookie = '%s';var resReferer = '%s'</script>\r\n</body>''' % (flow.request.headers.get('cookie'), flow.request.headers.get('cookie'), flow.request.headers.get('referer')))
          for value in item['hack']:
            if (value[0] != ""):
              returnText = returnText.replace(value[0], value[1])
            else:
              returnText = value[1]
          flow.response.set_text(returnText)
  
  def request(self, flow):
    if (flow.request.url):
      for item in reqHackList:
        findList = pattern = re.compile(item).findall(flow.request.url)
        if (len(findList) > 0):
          print(flow.request.headers)
          # flow.request.headers['owoHost'] = flow.request.host
          # flow.request.headers['owoPath'] = flow.request.path
          # flow.request.path = "/redirect"
          # flow.request.host = "hanshu.run"
          # flow.request.port = 80
          # flow.request.scheme = 'http'
          headersTemp = {}
          for item in flow.request.headers:
            headersTemp[item] = flow.request.headers[item]
          conn = http.client.HTTPSConnection("hanshu.run")
          conn.request("POST", "/redirect", json.dumps({
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
          print(data.decode("utf-8"))
        
addons = [
  ModifyResponse()
]