# Logs Analysis project
Source code for reporting tool that will use information from the database to discover what kind of articles the site's readers like.
This tool will show top articles by views, top authors by views and also if in any day there is a requests lead to error more than 1%.


### Getting started

1- Install [Python](https://www.python.org/)
2- Open the command-line (command-prompt for windows and terminal for MacBook and Linux systems)
3- Go to the project directory and then type :
for windows users `python log_analysis.py`
for linux users `./log_analysis.py`

### Views used
I've created two views to support this version of reporting tool.

1- first view helps getting top articles with their views.
`create view Top_Articles as select SUBSTRING(path, 10) AS extractArticle,
count(*) as views from log
where path like '%article%' and status='200 OK'
group by extractArticle order by views desc;`

2- second view helps getting the total and error requests count per day.
`create view Error_And_Total as select DATE(time) as day,
sum(case when status = '404 NOT FOUND' then 1 end) as error,
sum(case when method = 'GET' then 1 end) as total
from log group by DATE(time);`
