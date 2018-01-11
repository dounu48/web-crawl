import requests
from bs4 import BeautifulSoup as bs
import chardet

LOGIN_INFO = {
  'userId': 'username',
  'userPassword': 'password'
}

# HTTP GET Request
# Session and remain inside of with
# with requests.Session() as sess :
#   first_page = sess.get('https://www.clien.net/service')
#   html = first_page.text
#   soup = bs(html, 'html.parser')
#   csrf = soup.find('input', {'name': '_csrf'})
#   print(csrf['value'])
#
#   # get csrf
#   #LOGIN_INFO = {**LOGIN_INFO, **{'_csrf': csrf['value']}}
#   LOGIN_INFO = dict(LOGIN_INFO, **{'_csrf': csrf['value']})
#   print(LOGIN_INFO)
#
#   # login request
#   login_req = sess.post('https//www.clien.net/service/login', data=LOGIN_INFO)
#   print(login_req.status_code)
#
#   if login_req != 200 :
#     raise Exception('failed to login, please check ID and password')

post_one = requests.get('https://www.clien.net/service/board/rule/10707408')
# sess.get('https://www.clien.net/service/board/rule/10707408')
html_post = post_one.text

soup = bs(html_post, 'html.parser') #, from_encoding='ascii')
title = soup.select('#div_content > div.post_title.symph_row > h3.post_subject > span')
print(title[0].text)

# print(chardet.detect('\ud68c\uc6d0\uc911\uace0\uc7a5\ud130 \uac8c\uc2dc\ud310 \uc774\uc6a9\uaddc\uce59'))
content = soup.select('#div_content > div.post_view > div.post_content article > div.post_article.fr-view')

print(content[0].text)