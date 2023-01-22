# 파이썬과 sqlite 연결 및 데이터 입력
# 진행을 위해 sqlite3 다운로드 필요
import sqlite3

# 1. 데이터베이스에 연결
{연결자명} = sqlite3.connect("DB이름")
	          sqlite3.connect("c:/PhtyonDB/")

# 2. 커서 생성 (DB에 접속해 정보를 입,출력하는 연결고리)
{커서명} = {연결자명}.cursor()

# 3. 테이블 생성
{커서명}.execute("create ~~")

# 4. 만든 테이블에 데이터 입력, 업데이트 등
{커서명}.execute("insert into ~~")
{커서명}.execute("update [table] set ~~")
# 입력/업데이트한 데이터를 저장
{연결자명}.commit()

# 5. 데이터 검색
{커서명}.execute("select * from ~~")
while True:
	row = {커서명}.fetchone()	# 하나씩 정보 가져오기
                            # 모든 정보를 가져오는 {커서명}.fetchall() 도 있다
	if row == None: break     # 정보가 있을때까지 실행
	data = row[0]	# 각 열마다 정보 가져오기

#6. 데이터베이스 닫기
{연결자명}.close()
