"""
无附件邮件发送
SMTP是发送邮件的协议，Python内置对SMTP的支持，
可以发送纯文本邮件、HTML邮件以及带附件的邮件。
Python对SMTP支持有smtplib和email两个模块，
email负责构造邮件，smtplib负责发送邮件。

使用Python的smtplib发送邮件十分简单，只要掌握了各种邮件类型的构造方法，正确设置好邮件头，就可以顺利发出。

构造一个邮件对象就是一个Messag对象，如果构造一个MIMEText对象，就表示一个文本邮件对象，如果构造一个MIMEImage对象，就表示一个作为附件的图片，要把多个对象组合起来，就用MIMEMultipart对象，而MIMEBase可以表示任何对象。它们的继承关系如下：

Message
+- MIMEBase
   +- MIMEMultipart
   +- MIMENonMultipart
      +- MIMEMessage
      +- MIMEText
      +- MIMEImage
这种嵌套关系就可以构造出任意复杂的邮件。你可以通过email.mime文档查看它们所在的包以及详细的用法。


"""

from socket import *
from time import *

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

# 注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，
# 传入'plain'，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
def main():
	sender=input('From:')
	password=input('PW:')
	receiver=input('To:')
	smtper=input('smtp server:')
	message=MIMEText('用python发送邮件的示例。','plain','utf-8')
	message['From']=Header('kk的qq邮箱','utf-8')
	message['To']=Header('kk的好友','utf-8')
	message['Subject']=Header('示例代码实验邮件','utf-8')

	smtper=SMTP(smtper)
	smtper.login(sender,password)
	smtper.sendmail(sender,receiver,message.as_string())
	print('邮件发送完成！')

if __name__ == '__main__':
    main()

