#!/usr/bin/env python3.5
# Importing needed modules
import psycopg2

# Connection to the database
db = psycopg2.connect("dbname=news")

# Creating a cursor
with db.cursor() as c:
    # Looping over the output
    def loop_over_output(output):
        for line in output:
            print("{}: {}".format(line[0], line[1]))
        print("\n")

    # Get top three articles of all time
    c.execute("select * from Top_Articles limit 3;")

    print("The most popular three articles of all time by reviews:")
    print("=======================================================")
    loop_over_output(c.fetchall())

    # Get top article authors of all time
    c.execute("select name, sum(views) as views from articles, Top_Articles,"
              " authors where articles.slug = Top_Articles.extractarticle "
              "and articles.author = authors.id group by name order by views desc;")  # NOQA

    print("The most popular article authors of all time by reviews:")
    print("========================================================")
    loop_over_output(c.fetchall())

    # Get days that have more than 1% of requests lead to errors
    c.execute("select day, (error * 100.0 / total)  as percentage "
              "from Error_And_Total where (error * 100.0 / total) > 1;")

    print("Days that have more than 1% of requests lead to errors:")
    print("=======================================================")
    loop_over_output(c.fetchall())
