# Logs Analysis

This project is the third project at Udacity Full stack Nanodegree.
if you looked at [log-analysis.py](log-analysis.py) you will see the complex
queries that answers the following questions :-

1 - What are the most popular three articles of all time?

2 - Who are the most popular article authors of all time?

3 - On which days did more than 1% of requests lead to errors?


## Usage

* Clone or download the project

* [Download the database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) on same dictionary

* Then run the following commands to create the db and generate the report.

```sh
psql -d news -f newsdata.sql
```

* to run the script.

```sh
python3 log-analysis.py
```
