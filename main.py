import psycopg2
from queries_ques import queries, ques  # import ques and queries data

# Creates Connection
conn = psycopg2.connect(database="news", user="postgres", password="fell2rise", host="127.0.0.1", port="5432")
print ("Opened database successfully\n\n")


def execute_query(conn1, query):
    """Executes Database Query

        Args:
            conn1(psycopg2.connect object): Database connection obeject
            query(string):Query to be executed by database
        And so on...
    """
    cur = conn1.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows


def print_res(ques, res, suff='views'):
    """Print Formatted Output

            Args:
                ques(string): Question
                res(object):Query result Object
                suff()string:suffix for output
            And so on...
        """
    print(ques)  # Print Question

    for i in range(len(res)):
        print("\t{0}. {1} -- {2} {3}".format(i + 1, res[i][0], res[i][1], suff))
    print('\n')  # Print Result


# Query 1
res1 = execute_query(conn, queries[0])
print_res(ques[0], res1)

# Query 2
res1 = execute_query(conn, queries[1])
print_res(ques[1], res1)

# Query 3
res1 = execute_query(conn, queries[2])
print_res(ques[2], res1)

# Close Connction
conn.close()
