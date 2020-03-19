# import sqlite3

# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# cursor.execute('create table user(id varchar(20) primary key, name varchar(32)) ')
# cursor.execute('insert into user (id, name) values (\'2\', \'michael\')')
# rowcount = cursor.rowcount
# print(rowcount)
# cursor.close()
# conn.commit()
# conn.close()

# cursor.execute('select * from user')
# values = cursor.fetchall()

# for user in values:
#     print(user)
# cursor.close()
# conn.close()

# msg = "ST 60DYYJ0121 TT 12051450 Z01 99774 SQ01 0 FQ01 0 BV 126 SI1 28 DC 27 " #bd
# msg = "ST 60DYYJ0121 TT 12041610 Z01 99893 BV 126 SI1 24 DC 25 " #bf
# msg = "ST 60DYYJ0121 TT 12041620 Z01 99770 BV 125 SI1 23 DC 25 " #bm
# msg = "ST 60DYYJ0121 TT 12041630 Z01 99770 BV 124 SI1 24 DC 25 " #bl
msg = "ST 60DYYJ0121 TT 12041535 Z01 99761 BV 126 SI1 26 DC 22 " #bg

def check() :
    sum = 0
    for c in msg:
        sum += ord(c)
    sum = sum & 0xff
    sum = (~sum + 1 ) & 0xff
    low = sum & 0x0f
    high = (sum & 0xff) >> 4
    sum = (high << 8 & 0xff00) +low
    checkCode = (sum + 0x6161 ) & 0xffff
    print(chr(checkCode >> 8 & 0xff)+chr(checkCode & 0xff))


if __name__ == '__main__':
    check()
