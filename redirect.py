from flask import Flask,request,render_template
import requests
import json

app = Flask(__name__)
 
@app.route('/tsgintf/main/service', methods=['GET', 'POST'])
def req():
    data = str(request.get_data())
    if ('QRY_LOGIN' in data):
        return '{"result_code":"0","result_desc":"成功","result_data":{"totalPage":0,"currentPage":0,"entityOrField":false,"start":0,"limit":10,"end":10,"total":0,"clean":true,"param":{"size":10,"start":0},"userId":19185,"userPhysicalCard":"2018013544","studentCard":"2018013544","userName":"夏昕辰","mobile":"","password":"52283aaa29679c1428e038b7771a432b","userType":1,"grade":"","isValid":1,"orderHoursMax":"17","orderHoursMin":"2","appBackgroundAudioSwith":"yes","appBackgroundAudioName":"backmusic0.mp3","appAudioInterval":60,"appDeviceType":"mix","monitorCode":"WXXY","sysUUID":"FDA50693-A4E2-4FB1-AFCF-C6EB07647826","ibeaconList":["701_1","701_18","701_2","701_15","701_17","701_10"],"wifiList":["70:ba:ef:af:b3:e2","70:ba:ef:af:b3:e1","70:ba:ef:af:b3:e0","70:ba:ef:af:b3:e3","70:ba:ef:af:b3:f3","70:ba:ef:af:eb:63","70:ba:ef:af:eb:62","70:ba:ef:af:eb:61","70:ba:ef:af:eb:60","70:ba:ef:af:ea:e2","70:ba:ef:af:ea:e1","70:ba:ef:af:ea:e0","70:ba:ef:af:e8:51","70:ba:ef:af:e8:52","70:ba:ef:af:e8:50","70:ba:ef:af:ea:e3","70:ba:ef:af:b3:f1","70:ba:ef:af:b3:f2","70:ba:ef:af:e8:53","70:ba:ef:af:af:62","70:ba:ef:af:af:61","70:ba:ef:af:af:63","70:ba:ef:af:b3:f0","70:ba:ef:af:af:60","70:f9:6d:d7:da:82","70:f9:6d:d7:da:83","70:f9:6d:d7:da:81","70:f9:6d:d7:da:90","70:ba:ef:af:e8:43","70:ba:ef:af:e8:42","70:ba:ef:af:e8:41","70:f9:6d:d7:da:80","70:ba:ef:af:e8:40","70:ba:ef:af:e6:31","70:f9:6d:d7:da:92","70:ba:ef:af:e5:70","70:ba:ef:af:b2:83","70:ba:ef:af:e6:20","70:ba:ef:af:b2:81","70:ba:ef:af:b2:82","70:ba:ef:af:b2:80","70:f9:6d:d7:da:91","70:ba:ef:af:e5:72","70:ba:ef:af:e6:23","70:ba:ef:af:e6:22","70:ba:ef:af:e6:21","70:ba:ef:af:ea:f1","70:ba:ef:af:e5:71","70:ba:ef:af:ea:f3","70:ba:ef:af:ea:f2","70:ba:ef:af:ea:f0","70:ba:ef:af:e5:73","70:ba:ef:af:e6:32","70:f9:6d:d7:da:93","d4:61:fe:e6:7a:30","70:ba:ef:af:af:70","70:ba:ef:af:eb:70","70:ba:ef:af:e5:61","70:ba:ef:af:e5:60","70:ba:ef:af:eb:72","70:ba:ef:af:eb:71","70:ba:ef:af:b0:03","70:ba:ef:af:b0:01","70:ba:ef:af:e5:62","70:ba:ef:af:e5:63","70:ba:ef:af:eb:73","70:ba:ef:af:b0:00","70:ba:ef:af:b0:02","70:ba:ef:af:ae:e3","70:ba:ef:af:ae:e2","70:ba:ef:af:ae:e0","d4:61:fe:e6:7a:63","70:ba:ef:af:ae:e1","70:ba:ef:af:ea:43","d4:61:fe:e6:7a:62","70:ba:ef:af:ea:41","70:ba:ef:af:ea:40","70:ba:ef:af:ea:42","70:ba:ef:af:af:72","70:ba:ef:af:e6:30","d4:61:fe:e6:7a:33","70:ba:ef:af:b0:11","d4:61:fe:e6:7a:31","70:ba:ef:af:b0:13","70:ba:ef:af:e6:33","d4:61:fe:e6:44:b1","d4:61:fe:e6:7a:60","70:ba:ef:af:b2:90","70:ba:ef:af:af:71","70:ba:ef:af:1f:42","70:ba:ef:af:1f:41","70:ba:ef:af:1f:40","70:ba:ef:af:af:73","70:ba:ef:af:b2:93","70:ba:ef:af:b2:91","70:ba:ef:af:ea:70","70:ba:ef:af:ea:72","70:ba:ef:af:ae:f3","70:ba:ef:af:ae:f0","70:ba:ef:af:1f:43","70:ba:ef:af:b3:40","70:ba:ef:af:ea:63","70:ba:ef:af:ea:62","70:ba:ef:af:ea:61","70:ba:ef:af:ea:60","70:ba:ef:af:b3:81","70:ba:ef:af:b3:82","70:ba:ef:af:b3:80","70:ba:ef:af:b3:83","70:ba:ef:af:b2:92","70:ba:ef:af:b3:43","70:ba:ef:af:b3:41","70:ba:ef:af:b3:42","70:ba:ef:af:eb:31","d4:61:fe:e6:7a:71","d4:61:fe:e6:7a:70","d4:61:fe:e6:7a:72","70:ba:ef:af:b0:10","d4:61:fe:e6:44:a2","d4:61:fe:e6:44:a1","d4:61:fe:e6:44:a0","d4:61:fe:e6:44:a3","d4:61:fe:e6:7a:73","70:ba:ef:af:ea:71","70:ba:ef:af:ae:f1","70:ba:ef:af:ae:f2","d4:61:fe:e6:44:b0","70:ba:ef:af:ea:50","70:ba:ef:af:ea:53","d4:61:fe:e6:44:b3","d4:61:fe:e6:4a:90","d4:61:fe:e6:44:b2","70:ba:ef:af:b3:90","70:ba:ef:af:b3:91","d4:61:fe:e6:4a:92","70:ba:ef:af:ea:73","d4:61:fe:e6:4a:93","d4:61:fe:e6:4a:91","d4:61:fe:e6:7a:61","70:ba:ef:af:d8:82","70:ba:ef:af:d8:81","70:ba:ef:af:d8:80","70:ba:ef:af:d8:83","70:ba:ef:af:d8:90","70:ba:ef:af:d8:92","70:ba:ef:af:ea:81","70:ba:ef:af:ea:80","70:ba:ef:af:d5:c3","70:ba:ef:af:d5:c2","70:ba:ef:af:d5:c1","70:ba:ef:af:d5:c0","70:ba:ef:af:e4:e3","70:ba:ef:af:e4:e2","70:ba:ef:af:ea:83","70:ba:ef:af:ea:82","70:ba:ef:af:a4:a3","70:ba:ef:af:a4:a0","70:ba:ef:af:a4:a2","70:ba:ef:af:a4:a1","70:ba:ef:af:d8:93","d4:61:fe:e6:7a:32","70:ba:ef:af:dc:62","70:ba:ef:af:dc:61","70:ba:ef:af:dc:63","70:ba:ef:af:dc:60","70:ba:ef:af:df:f3","d4:61:fe:e6:7a:21","d4:61:fe:e6:7a:20","d4:61:fe:e6:7a:23","d4:61:fe:e6:7a:22","70:ba:ef:af:d4:82","70:ba:ef:af:d4:81","d4:61:fe:e6:4a:83","70:ba:ef:af:d4:83","70:ba:ef:af:d4:80","d4:61:fe:e6:4a:81","d4:61:fe:e6:4a:80","70:ba:ef:af:eb:21","70:ba:ef:af:eb:20","70:ba:ef:af:eb:23","70:ba:ef:af:eb:22","70:ba:ef:af:ea:93","70:f9:6d:d7:d8:61","70:f9:6d:d7:d8:63","70:f9:6d:d7:d8:62","70:f9:6d:d7:d8:60","70:f9:6d:d7:d5:81","70:f9:6d:d7:d5:80","70:f9:6d:d7:d5:83","70:f9:6d:d7:d5:82","70:f9:6d:d7:d5:91","70:f9:6d:d7:d8:71","70:f9:6d:d7:d8:73","70:f9:6d:d7:d8:72","70:f9:6d:d7:d8:70","70:f9:6d:d7:d5:92","70:f9:6d:d7:d5:90","70:ba:ef:af:b2:60","70:ba:ef:af:b2:61","70:ba:ef:af:b2:63","70:ba:ef:af:b2:62","70:f9:6d:d7:d5:93","70:ba:ef:af:b2:70","70:ba:ef:af:b2:71","70:ba:ef:af:b2:73","70:ba:ef:af:dc:71","70:ba:ef:af:dc:70","70:ba:ef:af:b2:72","70:ba:ef:af:b3:61","70:ba:ef:af:b3:63","70:ba:ef:af:dc:73","70:ba:ef:af:b3:60","70:ba:ef:af:b3:62","70:ba:ef:af:dc:72","70:ba:ef:af:e5:e0","70:ba:ef:af:e5:e2","70:ba:ef:af:e5:e1","70:ba:ef:af:e5:e3","70:f9:6d:d4:26:91","70:f9:6d:d4:26:93","70:ba:ef:af:df:e1","70:f9:6d:d4:26:92","70:ba:ef:af:df:e3","70:ba:ef:af:df:e2","70:ba:ef:af:df:e0","70:f9:6d:d4:26:90","70:ba:ef:af:d5:d0","70:ba:ef:af:d8:91","70:f9:6d:d4:26:81","70:f9:6d:d4:26:82","70:ba:ef:af:b3:70","70:f9:6d:d4:26:83","70:f9:6d:d4:26:80","70:ba:ef:af:e5:f0","70:ba:ef:af:e5:f2","70:ba:ef:af:e5:f1","70:ba:ef:af:e5:f3","70:ba:ef:af:b3:72","70:ba:ef:af:df:f0","70:ba:ef:af:df:f1","70:ba:ef:af:df:f2","70:ba:ef:af:b3:73","70:ba:ef:af:b3:71","d4:61:fe:e6:79:b1","d4:61:fe:e6:79:b0","70:ba:ef:af:b3:52","70:ba:ef:af:1f:50","70:ba:ef:af:1f:51","70:ba:ef:af:1f:52","70:ba:ef:af:1f:53","70:ba:ef:af:b3:53","70:ba:ef:af:eb:30","70:ba:ef:af:b3:50","70:ba:ef:af:b3:51","70:ba:ef:af:b0:12","70:ba:ef:af:eb:33","70:ba:ef:af:eb:32","70:ba:ef:af:b3:92","70:ba:ef:af:b3:93","70:ba:ef:af:ea:52","70:ba:ef:af:ea:51","d4:61:fe:e6:79:b2","d4:61:fe:e6:4a:82"],"seatId":0,"remindSet":"","startHourToNxtD":"12","preholdMinutes":"10","token":"f26de2916c19441ab98013bfb8ee82a3"}}'
    if ('QRY_NOTICE' in data):
        return '{"result_code":"0","result_desc":"成功","result_data":{"totalPage":1,"currentPage":1,"entityOrField":true,"start":0,"limit":5,"end":5,"total":3,"rows":[{"totalPage":0,"currentPage":0,"entityOrField":false,"start":0,"limit":10,"end":10,"total":0,"clean":true,"param":{"size":10,"start":0},"id":4,"msgTitle":"版本V2.6.0重要更新","type":0,"operationTime":1572441145000,"startDate":"2019-10-30","endDate":"2099-03-01","createuid":"1","createUsername":"root","stateName":"有效"},{"totalPage":0,"currentPage":0,"entityOrField":false,"start":0,"limit":10,"end":10,"total":0,"clean":true,"param":{"size":10,"start":0},"id":3,"msgTitle":"入座失败常见问题","type":0,"operationTime":1567407600000,"startDate":"2017-05-27","endDate":"2099-03-01","createuid":"1","createUsername":"root","stateName":"有效"},{"totalPage":0,"currentPage":0,"entityOrField":false,"start":0,"limit":10,"end":10,"total":0,"clean":true,"param":{"size":10,"start":0},"id":2,"msgTitle":"重要说明请阅读","type":0,"operationTime":1566334386000,"startDate":"2017-05-27","endDate":"2099-03-01","createuid":"1","createUsername":"root","stateName":"有效"}],"clean":true,"param":{"size":5,"start":0}}}'
    if ('QRY_PRE_LIBRARY' in data):
        return '{"result_code":"0","result_desc":"成功","result_data":[{"totalPage":0,"currentPage":0,"entityOrField":false,"start":0,"limit":10,"end":10,"total":0,"clean":true,"param":{"size":10,"start":0},"libraryId":1,"libName":"皖西学院","category":1,"address":"月亮岛","zip":"239000","tel":"0550-0000000","schoolCode":"1"}],"page":{"currentPage":1,"limit":10,"total_page":1,"total_count":1}}'
    if ('QRY_OPENHOURS' in data):
        return '{"result_code":"0","result_desc":"成功","result_data":[{"totalPage":0,"currentPage":0,"entityOrField":false,"start":0,"limit":10,"end":10,"total":0,"clean":true,"param":{"size":10,"start":0},"id":22,"libraryId":1,"libName":"皖西学院","day":"1","startHour":"06:30","endHour":"23:00","type":"1","typeName":"全天"},{"totalPage":0,"currentPage":0,"entityOrField":false,"start":0,"limit":10,"end":10,"total":0,"clean":true,"param":{"size":10,"start":0},"id":23,"libraryId":1,"libName":"皖西学院","day":"2","startHour":"06:30","endHour":"23:00","type":"1","typeName":"全天"},{"totalPage":0,"currentPage":0,"entityOrField":false,"start":0,"limit":10,"end":10,"total":0,"clean":true,"param":{"size":10,"start":0},"id":24,"libraryId":1,"libName":"皖西学院","day":"3","startHour":"06:30","endHour":"23:00","type":"1","typeName":"全天"},{"totalPage":0,"currentPage":0,"entityOrField":false,"start":0,"limit":10,"end":10,"total":0,"clean":true,"param":{"size":10,"start":0},"id":25,"libraryId":1,"libName":"皖西学院","day":"4","startHour":"06:30","endHour":"23:00","type":"1","typeName":"全天"},{"totalPage":0,"currentPage":0,"entityOrField":false,"start":0,"limit":10,"end":10,"total":0,"clean":true,"param":{"size":10,"start":0},"id":26,"libraryId":1,"libName":"皖西学院","day":"5","startHour":"06:30","endHour":"23:00","type":"1","typeName":"全天"},{"totalPage":0,"currentPage":0,"entityOrField":false,"start":0,"limit":10,"end":10,"total":0,"clean":true,"param":{"size":10,"start":0},"id":27,"libraryId":1,"libName":"皖西学院","day":"6","startHour":"06:30","endHour":"23:00","type":"1","typeName":"全天"},{"totalPage":0,"currentPage":0,"entityOrField":false,"start":0,"limit":10,"end":10,"total":0,"clean":true,"param":{"size":10,"start":0},"id":28,"libraryId":1,"libName":"皖西学院","day":"7","startHour":"06:30","endHour":"23:00","type":"1","typeName":"全天"}]}'
    if ('QRY_PRE_ROOM' in data):
        return '{"result_code":"0","result_desc":"成功","result_data":[{"totalPage":0,"currentPage":0,"entityOrField":false,"start":0,"limit":10,"end":10,"total":0,"clean":true,"param":{"size":10,"start":0},"freeCount":0,"libraryId":1,"roomId":8,"roomName":"105自习室"},{"totalPage":0,"currentPage":0,"entityOrField":false,"start":0,"limit":10,"end":10,"total":0,"clean":true,"param":{"size":10,"start":0},"freeCount":0,"libraryId":1,"roomId":9,"roomName":"202自习室"},{"totalPage":0,"currentPage":0,"entityOrField":false,"start":0,"limit":10,"end":10,"total":0,"clean":true,"param":{"size":10,"start":0},"freeCount":0,"libraryId":1,"roomId":10,"roomName":"203自习室"},{"totalPage":0,"currentPage":0,"entityOrField":false,"start":0,"limit":10,"end":10,"total":0,"clean":true,"param":{"size":10,"start":0},"freeCount":0,"libraryId":1,"roomId":12,"roomName":"101自习室"}],"page":{"currentPage":1,"limit":50,"total_page":1,"total_count":4}}'
    if ('QRY_PRE_SEAT' in data):
        return '''
<style>
.button {
    background-color: #009fe9;
    height: 40px;
    line-height: 40px;
    margin: 10px;
    font-size: 14px;
    border-radius: 3px;
    color: white;
}
</style>
<script>
function GetDateStr(AddDayCount) {
    var dd = new Date();
    dd.setDate(dd.getDate()+AddDayCount);//获取AddDayCount天后的日期
    var y = dd.getFullYear();
    var m = dd.getMonth()+1;//获取当前月份的日期
    var d = dd.getDate();
    return y+"-"+m+"-"+d;
}
// alert(roomId)
// document.body.innerText = document.body.innerHTML
</script>
<div class="button" onclick="document.body.innerText = document.body.innerHTML">B21</div>
<div class="button" onclick="doPreSeat('B22', '29',GetDateStr(1), '2018213345', '06:30','22:00','0')">B22</div>
<div class="button" onclick="doPreSeat('B23', '29',GetDateStr(1), '2018213345', '06:30','22:00','0')">B23</div>
<div class="button" onclick="doPreSeat('B24', '29',GetDateStr(1), '2018213345', '06:30','22:00','0')">B24</div>
        '''
    if ('UPD_PRE_SEAT' in data):
        return '{"result_desc":"请关闭代理切换至校园网提交!"}'

# 静谧自习室
@app.route('/srapi/app/member/supplier-or-merchant-info/v1/2/211', methods=['GET', 'POST'])
def srapi():
    print()
    url = "https://user.hanshu.run/adminUpdata"

    payload = json.dumps({
    "username": "admin",
    "session": "5Cm9OU_sWViuhNPXPj-3Bg",
    "userid": 783,
    "type": "静谧自习室",
    "value": request.headers.get('token')
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return request.headers.get('token')

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port="8867")