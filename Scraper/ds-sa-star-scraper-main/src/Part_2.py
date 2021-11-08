
import os
import sqlite3
from src.Part_1 import get_movie_code, get_page
 
"""
Part 2

해당 부분은 Advanced 이기 때문에 필수는 아닙니다.
init_db 는 이미 구현되어 있습니다.
"""


BASE_URL = "https://movie.naver.com/movie"
def get_db(movie_title, page_num):
    movie_code = Part_1.get_movie_code(movie_title)
    review_url = f"{BASE_URL}/point/af/list.naver?st=mcode&sword={movie_code}&target=after&page={page_num}"
    soup, page = Part_1.get_page(review_url)
    data1 = soup.find_all('td','num')
    data_list =[]
    for a in data1:
        d = a.get_text("_",strip=True).split("_")
        data_list.append(d)
    id_list = []
    for b in data_list[1::2]:
        id_list.append(b[0])

    data2 = soup.find_all('td','title')
    review_list = []
    for a,b in zip(id_list ,data2):
        review = {'id' : str(a),
                'review_text':str(b.get_text("_",strip=True).split('_')[3]),
                'review_star': float(b.get_text("_",strip=True).split('_')[2]),
                'movie_title' : str(movie_title)
                }
        review_list.append(review)
    return review_list

DATABASE_PATH = os.path.join(os.getcwd(), 'scrape_data.db')

conn = sqlite3.connect(DATABASE_PATH)



def store_by_page_num(movie_title, page_num=10, conn=conn):
    init_db(conn)

    a = get_db(movie_title,1)
    for i in range(2,page_num+1):
        a = a + get_db(movie_title, i)
    lis_t =[]
    for e in range(0,page_num*10):
        lis_t.append(tuple(a[e].values()))


    cur = conn.cursor()
    cur.executemany("INSERT INTO Review VALUES (?, ?, ?, ?)", lis_t)
    conn.commit()

    """
    store_by_page_num 함수는 영화 제목, 페이지 번호, 데이터베이스 커넥션 객체를
    받아 주어진 영화제목의 리뷰를 총 주어진 페이지 개수 만큼 스크레이핑 한 뒤에
    데이터베이스에 저장합니다.

    파라미터:
        - movie_title: 리뷰를 스크레이핑할 영화 제목이 담긴 문자열(str) 입니다.
        - page_num: 첫 번째 페이지에서부터 스크레이핑할 페이지 개수가 담긴
        숫자(int) 입니다.
        - conn: 데이터베이스와 연결되 커넥션 객체

    리턴:
        - 별도로 없습니다.
    """

def init_db(conn=conn):
    """
    init_db 함수는 Review 테이블을 초기화해주는 함수입니다.

    실행을 하게 되면 파라미터로 전해지는 conn 객체가 연결된 데이터베이스에서
    Review 테이블이 존재하면 DROP 하고 새로 생성해줍니다.

    기본적으로 Part_2.py 에 있는 conn 객체와 연결을 시도합니다.
    """

    create_table = """CREATE TABLE Review (
                        id VARCHAR(20),
                        review_text TEXT,
                        review_star FLOAT,
                        movie_title VARCHAR(128),
                        PRIMARY KEY (id)
                        );"""

    drop_table_if_exists = "DROP TABLE IF EXISTS Review;"

    cur = conn.cursor()

    cur.execute(drop_table_if_exists)
    cur.execute(create_table)
    cur.close()