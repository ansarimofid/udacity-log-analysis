#!/usr/bin/env python2
# Question 1
ques1 = "1. What are the most popular three articles of all time?"  # noqa

# Query 1 Based on Ques
query1 = """
select title,views from articles join (select path, count(*) as views from log group by path order by views desc) as newlog on replace(newlog.path,'/article/','') = articles.slug limit 3
"""  # noqa

# Question 2
ques2 = "2. Who are the most popular article authors of all time?"  # noqa

# Query 2 Based on Ques
query2 = """
select authorstable.author, sum(views) as views from (select authors.name as author, articles.slug as slug from authors join articles on authors.id = articles.author) as authorstable join (select path, count(*) as views from log  group by path order by views) as newlog on replace(newlog.path,'/article/','') = authorstable.slug group by authorstable.author order by views desc
"""  # noqa

# Question 3
ques3 = "3. On which days did more than 1% of requests lead to errors?"  # noqa

# Query 3 Based on Ques
query3 = """
select * from (select reqTable.datedata, cast(round((errTable.error * 100.00)/reqTable.request,2) as numeric) as err from (select count(*) as request,date(log.time) as datedata from log group by datedata) as reqTable join (select count(*) as error,date(log.time) as datedata from log where log.status like '404%' group by datedata) as errTable on reqTable.datedata=errTable.datedata) as res where err > 1
"""  # noqa

ques = [ques1, ques2, ques3]
queries = [query1, query2, query3]
