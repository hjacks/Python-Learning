#-*- coding:utf-8 -*-
#!/usr/bin/python
import smtplib
import datetime
import pymysql
#import chardet
from email.mime.text import MIMEText
import sys
type1 = sys.getfilesystemencoding()



mailto_list=['']

mail_host=""  #设置服务器
mail_user=""  #用户名
mail_pass=""   #口令

mail_cc = ['']


#当前时间
day_now=datetime.date.today()-datetime.timedelta(days=1)
# 当前日期-7
day_1 = datetime.date.today()-datetime.timedelta(days=5)
day = datetime.date.today()-datetime.timedelta(days=1)

# 月初
day_from = datetime.date(day.year, day.month, 1)
# 上月最后一天
day_tmp = datetime.date(day.year, day.month, 1) - datetime.timedelta(days=8)
# 上月的今天
try:
    last_month_day = datetime.date(day_tmp.year, day_tmp.month, day.day)
except:
    last_month_day = datetime.date(day_tmp.year, day_tmp.month, day.day-1)
    pass
# 上月的月初
last_month_day_from = datetime.date(day_tmp.year, day_tmp.month, 1)
# 当前日期往前推 31 天
day_pre = datetime.date.today()-datetime.timedelta(days=31)



#发送邮件
def send_mail(to_list,sub,content,cc):  #to_list：收件人；sub：主题；content：邮件内容
    me=""
    
    msg = MIMEText(content,_subtype='html',_charset='utf8')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me
    msg['To'] = ";".join(mailto_list)
    msg['CC'] = ";".join(cc)
    
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)  #连接smtp服务器
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, to_list, msg.as_string())  #发送邮件
        s.close()
        return True
    except smtplib.SMTPException:
        print (smtplib.SMTPException)
        return False

def make_html_table(content_list):
    content = '<table border="1" align="center" cellpadding="4" cellspacing="0" bordercolor="#000000"> \n'
    for l in content_list:
        content += '<tr>'
        for data in l:
            if l.index(data) in (1,3,4,5,6,7):
                content += '<td align="center" width="60">' + str(data) + '</td>'
            elif l.index(data) == 2:
                content += '<td align="center" width="60">' + str(data) + '</td>'
            else:
                content += '<td align="center" width="60">' + str(data) + '</td>'
        content += '</tr> \n'
    content += '</table> \n\n'
    return content

def make_html_table_2(content_list,table_name):
    content = '<table border="1" align="center" cellpadding="4" cellspacing="0" bordercolor="#000000"> \n'
    content += '<tr align="center"><td colspan="' + str(len(content_list[0])) + '">'+ table_name +'</td></tr>'
    for l in content_list:
        content += '<tr>'
        for data in l:
            if l.index(data) in (8,10):
                content += '<td width="90"><font size="2px">' + str(data) + '</td>'
            elif l.index(data) == 9:
                content += '<td width="90"><font size="2px">' + str(data) + '</td>'
            else:
                content += '<td width="90"><font size="2px">' + str(data) + '</td>'
        content += '</tr> \n'
    content += '</table> \n\n'
    return content


def getdata(i,j,table_name):
    content_list = []

    head_1 = ['审核日期\t', '审核订单数', '通过订单数', '拒绝订单数','通过率'];
    content_list.append(head_1)

    # link=['月环比','0', '0', '0', '0', '0'] #月环比
    # content_list.append(link)

    # 日期  审核通过率
    sql1 = "select audit_day as day_key ,count(t1.id) as  examine_cnt\
    ,count(case when status IN(2,3,5,6,7,8,9,10,11) then t1.id else null end) as sunc_examine_cnt\
    ,count(case when status=4 then t1.id else null end) as fail_examine_cnt\
    ,count(case when status IN(2,3,5,6,7,8,9,10,11) then t1.id else null end)*1.0/count(t1.id) from\
    (select date(audit_time) as audit_day,id,uid,manager_name,status from bmdb.tb_credit_record \
    where manager_name IS NOT NULL and  manager_name!='' and status IN(2,3,4,5,6,7,8,9,10,11)\
    and DATE(audit_time) >=date('%s') and  DATE(audit_time) <= date('%s') and task_status in('%s','%s') \
    group by id,manager_name,status,date(audit_time),uid \
    )t1 group by 1 ORDER BY 1 desc " %(day_from,day_now,i,j)

    cursor.execute(sql1)
    result1 = cursor.fetchall()

    for data in result1:
        d = str(data[0])
        line = [d, '0', '0', '0', '0']
        if not data[1] == None:
            line[1] = str(data[1])
        if not data[2] == None:
            line[2] = str(data[2])
        if not data[3] == None:
            line[3] = str(data[3])
        if not data[4] == None:
            #line[6] = str(round(float(data[6]),4)*100) + '%'
            line[4] = str(round(data[4]*100,2))+'%'
        content_list.append(line)

    # 生成html
    content_1 = make_html_table_2(content_list,table_name)
    return content_1

def getdata_1(table_name):
    content_list = []

    head_1 = ['审核日期\t', '审核人员','审核订单数', '通过订单数', '拒绝订单数','通过率'];
    content_list.append(head_1)

    # link=['月环比','0', '0', '0', '0', '0'] #月环比
    # content_list.append(link)

    # 日期  审核通过率
    sql1 = "select audit_day as day_key,manager_name ,count(t1.id) as  examine_cnt\
    ,count(case when status IN(2,3,5,6,7,8,9,10,11) then t1.id else null end) as sunc_examine_cnt\
    ,count(case when status=4 then t1.id else null end) as fail_examine_cnt\
    ,count(case when status IN(2,3,5,6,7,8,9,10,11) then t1.id else null end)*1.0/count(t1.id) from\
    (select date(audit_time) as audit_day,id,uid,manager_name,status from bmdb.tb_credit_record \
    where manager_name IS NOT NULL and  manager_name!='' and status IN(2,3,4,5,6,7,8,9,10,11)\
    and DATE(audit_time) >=date('%s') and  DATE(audit_time) <= date('%s') \
    group by id,manager_name,status,date(audit_time),uid \
    )t1 group by 1,2 ORDER BY 1 desc " %(day_1,day_now)

    cursor.execute(sql1)
    result1 = cursor.fetchall()

    for data in result1:
        d = str(data[0])
        name=data[1]
        #print(type)
        #print(name.encode('utf-8').decode('utf-8'))
        #print(type(name))
        #print(name.decode('utf-8').encode("utf-8"))
        #print (name.encode('gbk'))
        #.decode("gb2312")   .encode('gb2312')
        line = [d, name,'0', '0', '0', '0']
        #if not data[1] == None:
         #   line[1] = str(data[1].encode('utf-8'))
        if not data[2] == None:
            line[2] = str(data[2])
        if not data[3] == None:
            line[3] = str(data[3])
        if not data[4] == None:
            line[4] = str(data[4])
        if not data[5] == None:
            #line[6] = str(round(float(data[6]),4)*100) + '%'
            line[5] = str(round(data[5]*100,2))+'%'
        content_list.append(line)

    # 生成html
    content_1 = make_html_table_2(content_list,table_name)
    return content_1



if __name__ == '__main__':
    # 连接mysql
    conn = pymysql.connect(db="", user="", passwd="", host="", port=)
    cursor = conn.cursor()

    neirong1=u'<ul style="padding:0 65px"><meta charset="UTF-8"> hi all,相关数据如下:<br/></ul>'
    # print(1)
    content = '<html lang="en"><head><meta charset="UTF-8"><title>title</title></head><body>\n'
    # print(3)
    #报表头部
    content += '<h1 align="center">人工审核日报</h1>'

    content += neirong1.encode('utf-8')
    #getdata表格
    content += getdata(3,5,'1.审核通过率-新客')
    content += '<h1 <br/> </h1>'

    content += getdata(4,5,'2.审核通过率-老客')
    content += '<h1 <br/> </h1>'

    content += getdata(1,5,'3.审核通过率-白良')
    content += '<h1 <br/> </h1>'

    content += getdata(2,5,'4.审核通过率-白优')
    content += '<h1 <br/> </h1>'

    content += getdata_1('5.个人审核通过率')


    content += '</html>\n\n'

    if send_mail(mailto_list,u"人工审核日报",content,mail_cc):
        print ('send mail succeed!')
    else:
        send_mail('',"邮件报表发送失败","邮件报表发送失败",'')

    cursor.close()
    conn.close()
