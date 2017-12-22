#!/usr/bin/env Python
# coding=utf-8
import bs4
import sys
import time
import random
import requests
import hashlib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import render_template,Flask,request,url_for,make_response,send_from_directory,send_file,redirect
def writeClass(className,teacher,room,week,lesson,jsonMode):
	global year,term,data,month,day,timetable
	if(jsonMode):
		data=data+"{'summary': '"+className+"','iCalUID': '"+str(random.randint(100000,999999))+"@aoaoao.me','location': '"+room+"','description': 'By"+teacher+"','start': {'dateTime': '"+getStart(week,lesson,True)+"','timeZone': 'Asia/Shanghai'},'end': {'dateTime': '"+getEnd(week,lesson,True)+"','timeZone': 'Asia/Shanghai'},'recurrence': ['RRULE:FREQ=WEEKLY;COUNT="+getWeekCount(week)+";BYDAY="+getWeekSign(lesson)+"']},"
	else:
		data=data+'\nBEGIN:VEVENT\nDTSTART;TZID=Asia/Shanghai:'+getStart(week,lesson)+'\nDTEND;TZID=Asia/Shanghai:'+getEnd(week,lesson)+'\nRRULE:FREQ=WEEKLY;COUNT='+getWeekCount(week)+';BYDAY='+getWeekSign(lesson)+'\nUID:'+str(random.randint(100000,999999))+'@aoaoao.me\nDESCRIPTION:By'+teacher+'\nLAST-MODIFIED:20171219T073432Z\nLOCATION:'+room+'\nSEQUENCE:0\nSTATUS:CONFIRMED\nSUMMARY:'+className+'\nTRANSP:OPAQUE\nEND:VEVENT\n'
def writeJsonClass(className,teacher,room,week,lesson):
	global year,term,json_data,month,day,timetable
	json_data=json_data+"{'summary': '"+className+"','iCalUID': '"+str(random.randint(100000,999999))+"@aoaoao.me','location': '"+room+"','description': 'By"+teacher+"','start': {'dateTime': '"+getStart(week,lesson,True)+"','timeZone': 'Asia/Shanghai'},'end': {'dateTime': '"+getEnd(week,lesson,True)+"','timeZone': 'Asia/Shanghai'},'recurrence': ['RRULE:FREQ=WEEKLY;COUNT="+getWeekCount(week)+";BYDAY="+getWeekSign(lesson)+"']},"
def getWeekCount(week):
	weekStart=week.split("-")[0]
	if("-" in week):
		weekEnd=week.split("-")[1]
	else:
		weekEnd=weekStart
	return str(int(weekEnd)-int(weekStart)+1);
def getStart(week,lesson,isJson=False):
	global year,term,month,day,timetable
	weekday=getWeekday(lesson)
	weekStart=week.split("-")[0]
	dayNow=int(day)+weekday-1
	timeArray = time.strptime(year+month+str(dayNow).zfill(2)+timetable[int(getTime(lesson)[0])]["start"]+"00", "%Y%m%d%H%M%S")
	timeArray = time.strptime(year+month+str(dayNow).zfill(2)+timetable[int(getTime(lesson)[0])]["start"]+"00", "%Y%m%d%H%M%S")
	timestamp = time.mktime(timeArray)+(int(weekStart)-1)*604800
	time_local = time.localtime(timestamp)
	if(isJson):
		return time.strftime("%Y-%m-%dT%H:%M:%S",time_local)
	return time.strftime("%Y%m%dT%H%M%S",time_local)
def getEnd(week,lesson,isJson=False):
	global year,term,month,day,timetable
	weekday=getWeekday(lesson)
	weekStart=week.split("-")[0]
	dayNow=int(day)+weekday-1
	timeArray = time.strptime(year+month+str(dayNow).zfill(2)+timetable[int(getTime(lesson)[1])]["end"]+"00", "%Y%m%d%H%M%S")
	timestamp = time.mktime(timeArray)+(int(weekStart)-1)*604800
	time_local = time.localtime(timestamp)
	if(isJson):
		return time.strftime("%Y-%m-%dT%H:%M:%S",time_local)
	return time.strftime("%Y%m%dT%H%M%S",time_local)
def getWeekday(lesson):
	week = lesson.split("[")[0]
	if(week=="一"):
		week = "1"
	elif(week=="二"):
		week = "2"
	elif(week=="三"):
		week = "3"
	elif(week=="四"):
		week = "4"
	elif(week=="五"):
		week = "5"
	elif(week=="六"):
		week = "6"
	elif(week==u"日"):
		week = "7"
	return int(week)
def getWeekSign(lesson):
	week = lesson.split("[")[0]
	if(week=="一"):
		week = "MO"
	elif(week=="二"):
		week = "TU"
	elif(week=="三"):
		week = "WE"
	elif(week=="四"):
		week = "TH"
	elif(week=="五"):
		week = "FR"
	elif(week=="六"):
		week = "SA"
	elif(week=="日"):
		week = "SU"
	return week
def getTime(lesson):
	lesson = lesson.split("[")[1]
	if("-" in lesson):
		classStart = lesson.split("-")[0]
		classEnd = lesson.split("-")[1].split("节")[0]
	else:
		classStart = lesson.split("节")[0]
		classEnd = classStart
	return [classStart,classEnd]
def md5sum(obj):
	 md5=hashlib.md5(obj.encode('gb2312')).hexdigest()
	 return md5
def chkpwd(pwd,stu):
	s = md5sum(stu + md5sum(pwd)[:30].upper() + '10611')[:30].upper()
	dsdsdsdsdxcxdfgfg = s 
	return dsdsdsdsdxcxdfgfg
def chkyzm(yzm):
	s = md5sum(md5sum(yzm.upper())[:30].upper() + '10611')[:30].upper()
	fgfggfdgtyuuyyuuckjg = s
	return fgfggfdgtyuuyyuuckjg
year="2017"
month="09"
day="4"
term=1
json_data="["
timetable={
	1:{"start":"0830","end":"0915"},
	2:{"start":"0925","end":"1010"},
	3:{"start":"1030","end":"1115"},
	4:{"start":"1120","end":"1210"},
	5:{"start":"1400","end":"1445"},
	6:{"start":"1455","end":"1540"},
	7:{"start":"1600","end":"1645"},
	8:{"start":"1655","end":"1740"},
	9:{"start":"1900","end":"1945"},
	10:{"start":"1955","end":"2040"},
	11:{"start":"2050","end":"2135"},
	12:{"start":"2145","end":"2230"},
	13:{"start":"2240","end":"2325"},
	14:{"start":"2335","end":"2359"},
}
data=""
uid=""
def generator(all_the_text,jsonMode=False):
	global year,term,data,month,day,timetable,uid
	if(jsonMode):
		data='''['''
	else:
		data='''BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:lzx2000228@gmail.com
X-WR-TIMEZONE:Asia/Shanghai

BEGIN:VTIMEZONE
TZID:Asia/Shanghai
X-LIC-LOCATION:Asia/Shanghai
BEGIN:STANDARD
TZOFFSETFROM:+0800
TZOFFSETTO:+0800
TZNAME:CST
DTSTART:19700101T000000
END:STANDARD
END:VTIMEZONE
'''
	soup = bs4.BeautifulSoup(all_the_text, "html.parser")
	try:
		tab = soup.find_all('table')[1]
	except:
		return (u"无法获取课表")
	data_list = []
	i=0
	for tr in tab.findAll('tr'):
		single_info=[]
		tdId=0
		if(i < 2):
			ii=0
		else:
			for td in tr.findAll('td'):
				if(tdId ==1 and td.getText() == ""):
					continue
				if(i < 2):
					ii=0
				else:
					single_info.append(td.getText())
				tdId=tdId+1
			data_list.append(single_info)
		i=i+1
	className=""
	teacher=""
	room=""
	for classLine in data_list:
		if(len(classLine)==13):
			className = classLine[1].split("]")[-1]
			teacher = classLine[9]
			room = classLine[12]
			if("," in classLine[-3]):
				for x in classLine[-3].split(","):
					writeClass(className,teacher,room,x,classLine[-2],jsonMode)
			else:
				writeClass(className,teacher,classLine[-1],classLine[-3],classLine[-2],jsonMode)
		else:
			if("," in classLine[-3]):
				for x in classLine[-3].split(","):
					writeClass(className,teacher,room,x,classLine[-2],jsonMode)
			else:
				writeClass(className,teacher,classLine[-1],classLine[-3],classLine[-2],jsonMode)
	ex=1
	try:
		tab = soup.find_all('table')[3]
	except:
		ex=0
	data_list = []
	i=0
	if (ex ==1):
		for tr in tab.findAll('tr'):
			single_info=[]
			tdId=0
			if(i < 2):
				ii=0
			else:
				for td in tr.findAll('td'):
					if(tdId ==1 and td.getText() == ""):
						continue
					if(i < 2):
						ii=0
					else:
						single_info.append(td.getText())
					tdId=tdId+1
				data_list.append(single_info)
			i=i+1
		className=""
		teacher=""
		room=""
		for classLine in data_list:
			if(len(classLine)==12):
				className = classLine[1].split("]")[-1]
				teacher = classLine[-5]
				room = classLine[11]
				if("," in classLine[-3]):
					for x in classLine[-3].split(","):
						writeClass(className,teacher,room,x,classLine[-2],jsonMode)
				else:
					writeClass(className,teacher,classLine[-1],classLine[-3],classLine[-2],jsonMode)
			elif (len(classLine)==11):
				className = classLine[1].split("]")[-1]
				teacher = classLine[-4]
				room = classLine[-1]
				if("," in classLine[-3]):
					for x in classLine[-3].split(","):
						writeClass(className,teacher,room,x,classLine[-2],jsonMode)
				else:
					writeClass(className,teacher,classLine[-1],classLine[-3],classLine[-2],jsonMode)
			else:
				if("," in classLine[-3]):
					for x in classLine[-3].split(","):
						writeClass(className,teacher,room,x,classLine[-2],jsonMode)
				else:
					writeClass(className,teacher,classLine[-1],classLine[-3],classLine[-2],jsonMode)
	try:
		tab = soup.find_all('table')[5]
	except:
		ex=0
	data_list = []
	i=0
	if (ex ==1):
		for tr in tab.findAll('tr'):
			single_info=[]
			tdId=0
			if(i < 2):
				ii=0
			else:
				for td in tr.findAll('td'):
					if(tdId ==1 and td.getText() == ""):
						continue
					if(i < 2):
						ii=0
					else:
						single_info.append(td.getText())
					tdId=tdId+1
				data_list.append(single_info)
			i=i+1
		className=""
		teacher=""
		room=""
		for classLine in data_list:
			if(len(classLine)==12):
				className = classLine[1].split("]")[-1]
				teacher = classLine[-5]
				room = classLine[11]
				if("," in classLine[-3]):
					for x in classLine[-3].split(","):
						writeClass(className,teacher,room,x,classLine[-2],jsonMode)
				else:
					writeClass(className,teacher,classLine[-1],classLine[-3],classLine[-2],jsonMode)
			elif (len(classLine)==11):
				className = classLine[1].split("]")[-1]
				teacher = classLine[-4]
				room = classLine[-1]
				if("," in classLine[-3]):
					for x in classLine[-3].split(","):
						writeClass(className,teacher,room,x,classLine[-2],jsonMode)
				else:
					writeClass(className,teacher,classLine[-1],classLine[-3],classLine[-2],jsonMode)
			else:
				if("," in classLine[-3]):
					for x in classLine[-3].split(","):
						writeClass(className,teacher,room,x,classLine[-2],jsonMode)
				else:
					writeClass(className,teacher,classLine[-1],classLine[-3],classLine[-2],jsonMode)
	if(jsonMode):
		filename = uid;
		file_object = open(filename+".json", 'w')
		file_object.write(data+"]")
		file_object.close( )
		return redirect("/importGoogle?uid="+filename)
	else:
		filename = uid;
		file_object = open(filename, 'w')
		file_object.write(data+'END:VCALENDAR\n')
		file_object.close( )
		response = make_response(send_file(filename))
		response.headers["Content-Disposition"] = "attachment; filename=classTable.ics;"
	return response;
app = Flask(__name__)
@app.route('/getList', methods=['POST', 'GET'])
def getList():
	global year,term,data,month,day,timetable,uid
	uid="0"
	pwd="s"
	if request.method == 'POST':
		uid = request.form['uid']
		pwd = request.form['pwd']
	s = requests.Session()
	token = s.get('http://202.202.1.41/_data/index_login.aspx')
	tokenSoup = bs4.BeautifulSoup(token.text, "html.parser")
	VIEWSTATE = tokenSoup.select("[name='__VIEWSTATE']")[0]['value']
	VIEWSTATEGENERATOR = tokenSoup.select("[name='__VIEWSTATEGENERATOR']")[0]['value']
	payload = {'Sel_Type': 'STU', '__VIEWSTATE':VIEWSTATE,'__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,"txt_dsdsdsdjkjkjc": uid,'txt_dsdfdfgfouyy':"","txt_ysdsdsdskgf":"","pcInfo":"","typeName":"","aerererdsdxcxdfgfg":"","efdfdfuuyyuuckjg":chkpwd(pwd,uid)}
	r = s.post('http://202.202.1.41/_data/index_login.aspx',data=payload)
	if("正在加载权限数据" in r.text):
		ii=0
	else:
		return "登陆失败"
	payload2 = {'Sel_XNXQ': '20170', 'rad': 'on','px':"0"}
	table =s.post('http://202.202.1.41/znpk/Pri_StuSel_rpt.aspx',data=payload2)
	all_the_text = table.text
	response = generator(all_the_text,False)
	return response
@app.route('/getListBySource', methods=['POST', 'GET'])
def getListBySource():
	global year,term,data,month,day,timetable,uid
	if request.method == 'POST':
		all_the_text = request.form['content']
	uid=str(random.randint(10000,99999))
	response = generator(all_the_text,False)
	return response
@app.route('/getJsonBySource', methods=['POST', 'GET'])
def getJsonBySource():
	global year,term,data,month,day,timetable,uid
	if request.method == 'POST':
		all_the_text = request.form['content']
	uid=str(random.randint(10000,99999))
	response = generator(all_the_text,True)
	return response
@app.route('/getJson', methods=['POST', 'GET'])
def getJson():
	global year,term,json_data,month,day,timetable,uid
	uid="0"
	pwd="s"
	if request.method == 'POST':
		uid = request.form['uid']
		pwd = request.form['pwd']
	s = requests.Session()
	token = s.get('http://202.202.1.41/_data/index_login.aspx')
	tokenSoup = bs4.BeautifulSoup(token.text, "html.parser")
	VIEWSTATE = tokenSoup.select("[name='__VIEWSTATE']")[0]['value']
	VIEWSTATEGENERATOR = tokenSoup.select("[name='__VIEWSTATEGENERATOR']")[0]['value']
	payload = {'Sel_Type': 'STU', '__VIEWSTATE':VIEWSTATE,'__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,"txt_dsdsdsdjkjkjc": uid,'txt_dsdfdfgfouyy':"","txt_ysdsdsdskgf":"","pcInfo":"","typeName":"","aerererdsdxcxdfgfg":"","efdfdfuuyyuuckjg":chkpwd(pwd,uid)}
	print payload
	r = s.post('http://202.202.1.41/_data/index_login.aspx',data=payload)
	if("正在加载权限数据" in r.text):
		ii=0
	else:
		return "登陆失败"
	payload2 = {'Sel_XNXQ': '20170', 'rad': 'on','px':"0"}
	table =s.post('http://202.202.1.41/znpk/Pri_StuSel_rpt.aspx',data=payload2)
	all_the_text = table.text
	response = generator(all_the_text,True)
	return response
@app.route('/importGoogle', methods=['POST', 'GET'])
def importGoogle():
	uid = str(int(request.args.get('uid', '0')))
	file_object = open(uid+".json")
	try:
	     all_the_text = file_object.read( )
	finally:
	     file_object.close( )
	return render_template('google.html', text=all_the_text)
if __name__ == '__main__':
	app.run(port=5001,host="0.0.0.0")
