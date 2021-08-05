import pymysql

def create(datas):
    #mysql과 연결
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    # 스트림 안의 데이터를 다룰 수 있는 부품인 cursor를 획득
    cur = con.cursor()
    print(cur)

    #sql문 만들어서 전송
    sql = 'insert into movie values (%s, %s)'
    #sql = 'update movie set score = %s where title = %s'
    result = cur.executemany(sql,datas)
    print('처리결과',result,'개')

    #수동으로 반영 후 (auto commit 안됨) close
    con.commit()
    con.close()


def read(score):
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'select * from movie where score = %s'
    cur.execute(sql,score)

    row = cur.fetchone()
    print(row)
    print(row)
    print(type(row))
    print('제목:',row[0],'평점:',row[1])

    con.close()

s = [('홍길동','90'),('홍남주','90')]
create(s)
read('90')
