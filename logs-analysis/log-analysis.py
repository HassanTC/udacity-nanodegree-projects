import psycopg2

DBNAME = "news"

# most viewed article query and question
most_viewed_articles = (
                        "select articles.title, count(*) as views "
                        "from articles, log "
                        "where log.path LIKE concat('%', articles.slug, '%') "
                        "AND status LIKE '%200%' "
                        "group by title order by views desc limit 3;"
                        )

question1 = "1. What are the most popular three articles of all time?"

# most viewed author query and question
most_viewed_authors = (
                        "select authors.name, count(*) as views "
                        "from articles, log, authors "
                        "where log.path LIKE concat('%', articles.slug, '%') "
                        "AND authors.id = articles.author "
                        "AND status LIKE '%200%' "
                        "group by authors.name "
                        "order by views desc"
                      )
question2 = "2. Who are the most popular article authors of all time?"

# error more than 1% query and question
errors_query = (
                "select day, percentage from "
                "(select a.day, round(cast((100*b.requests) as numeric) / "
                "cast(a.requests as numeric), 2) as percentage "
                "from (select date(time) as day, "
                "count(*) as requests from log group by day) as a, "
                "(select date(time) as day, count(*) as requests from "
                "log where status not like '%200%' group by day) as b "
                "where a.day = b.day) as perc "
                "where percentage > 1.0;"
               )
question3 = "3. On which days did more than 1% of requests lead to errors?"


class LogAnalysis():
    """a class for generating reports for a givin database"""
    def __init__(self, database_name):
        """Initialize new object with database name"""
        try:
            self.db = psycopg2.connect("dbname={}".format(database_name))
            self.cursor = self.db.cursor()
        except Exception as ex:
            print(ex)

    def do_query(self, query):
        """convert query to one line query, execute it and return result"""
        query = query.replace('\n', ' ')
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def print_result(self, header, result, suffix="views"):
        """print header and the result on the screen"""
        print(header)
        for i in range(len(result)):
            print('   ', i + 1, '.', result[i][0], '--', result[i][1], suffix)
        print("\n")

    def close(self):
        self.db.close()


if __name__ == '__main__':
    print("Database Loading..\n")

    log_analysis = LogAnalysis(DBNAME)

    result1 = log_analysis.do_query(most_viewed_articles)
    result2 = log_analysis.do_query(most_viewed_authors)
    result3 = log_analysis.do_query(errors_query)

    log_analysis.print_result(question1, result1)
    log_analysis.print_result(question2, result2)
    log_analysis.print_result(question3, result3, "% errors")
    log_analysis.close()
