# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
#open 163
driver.get("https://http://10.125.1.101:8080/login")
driver.maximize_window()
#<input id="__input0-inner" placeholder="Enter Company ID" value="" aria-labelledby="__input0-labelledby" type="text" class="sapMInputBaseInner" accesskey="1">
driver.find_element_by_id("__input0-inner").send_keys("ACNSFQA1")



elem_user = driver.find_element_by_name("email")
elem_user.send_keys("li130428")
#insert password
#<input data-placeholder="密码" name="password" maxlength="50" data-required="true" class="j-inputtext dlpwd" type="password" autocomplete="new-password" data-max-length="50" tabindex="2" spellcheck="false" id="auto-id-1525857138027" placeholder="密码">
elem_passwd = driver.find_element_by_name("password")
elem_passwd.send_keys("##li3718")
driver.switch_to.default_content()
#<a id="styleConf" href="javascript:void(0);">默认版本 <b class="ico ico-arr ico-arr-d"></b></a>
#driver.find_element_by_id("styleConf").click()
driver.find_elements_by_class_name("ico-arr-d")[0].click()
#<span class="fontWeight">6.0</span>
driver.find_elements_by_class_name("fontWeight")[0].click()
#click login
#<a href="javascript:void(0);" id="dologin" data-action="dologin" class="u-loginbtn btncolor tabfocus btndisabled" tabindex="8">登&nbsp;&nbsp;录</a>
driver.switch_to.frame("x-URS-iframe")
driver.find_element_by_id("dologin").click()
time.sleep(5)
#switch back
driver.switch_to.default_content()
#<div class="gWel-mailInfo-ico"><b class="nui-ico gWel-ico gWel-ico-unread-top"></b><b class="nui-ico gWel-ico gWel-ico-unread-letter"></b><b class="nui-ico gWel-ico gWel-ico-unread-bottom"></b></div>
driver.find_element_by_id("_mail_component_67_67").click()

#handles = driver.window_handles  #获取所有打开窗口的句柄
#print(handles)
#<li id="_mail_component_69_69" class="js-component-component ra0 mD0" tabindex="0" role="button" hidefocus="hidefocus"><span class="om0"><b class="nui-ico fn-bg ga0"></b></span><span class="oz0">写 信</span></li>
driver.find_element_by_id("_mail_component_69_69").click()
#<input class="nui-editableAddr-ipt" type="text" role="combobox" tabindex="1" aria-label="收件人地址输入框，请输入邮件地址，多人时地址请以分号隔开">
driver.find_element_by_class_name("nui-editableAddr-ipt").send_keys("li130428@163.com")
#<input id="1526019971548_subjectInput" class="nui-ipt-input" type="text" x-webkit-speech="" tabindex="1" maxlength="256">
driver.find_elements_by_class_name("nui-ipt-input")[2].send_keys("hello python")




time.sleep(5)

