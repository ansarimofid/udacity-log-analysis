import psycopg2

ques1 = "1. What are the most popular three articles of all time?"
query1 = """
select title,views from articles join (select path, count(*) as views from log group by path order by views desc) as newlog on replace(newlog.path,'/article/','') = articles.slug limit 3
"""

ques2 = "2. Who are the most popular article authors of all time?"
query2 = """
select authorstable.author, sum(views) as views from (select authors.name as author, articles.slug as slug from authors join articles on authors.id = articles.author) as authorstable join (select path, count(*) as views from log  group by path order by views) as newlog on replace(newlog.path,'/article/','') = authorstable.slug group by authorstable.author order by views desc
"""

ques3 = "3. On which days did more than 1% of requests lead to errors?"
query3 = """
select * from (select reqTable.datedata, cast(round((errTable.error * 100.00)/reqTable.request,2) as numeric) as err from (select count(*) as request,date(log.time) as datedata from log group by datedata) as reqTable join (select count(*) as error,date(log.time) as datedata from log where log.status like '404%' group by datedata) as errTable on reqTable.datedata=errTable.datedata) as res where err > 1
"""


def execute_query(conn1,query):
    cur = conn1.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def print_res(ques,res,suff='views'):
    print(ques)

    for i in range(len(res)):
        print("\t{0}. {1} -- {2} {3}".format(i+1,res[i][0],res[i][1],suff))
    print('\n')

conn = psycopg2.connect(database="news", user = "postgres", password = "fell2rise", host = "127.0.0.1", port = "5432")
print ("Opened database successfully\n\n")

# Query 1
res1 = execute_query(conn, query1)
print_res(ques1, res1)

# Query 2
res2 = execute_query(conn, query2)
print_res(ques2, res2)

# Query 3
res3 = execute_query(conn, query3)
print_res(ques3, res3,'% error')

conn.close()