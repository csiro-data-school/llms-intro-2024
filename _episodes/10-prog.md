---
title: "Programming with Databases - Python"
teaching: 20
exercises: 15
questions:
- "How can I access databases from programs written in Python?"
objectives:
- "Use common and emerging Python libraries to query databases"
- "Use sqlite and DuckDB to update and create databases"
keypoints:
- "General-purpose languages have libraries for accessing databases."
- "These libraries use a connection-and-cursor model."
- "Programs can read query results in batches or all at once."
- "Queries should be written using parameter substitution, not string formatting."
---

## Interfacing Programming Lanaguages and Databases

There are lots of ways to interface from programming languages to databases. Some are focused on mapping business records managed in a GUI  and perhaps in an Object Oriented data structure to database tables. In science we often are  interested in OLAP online analytical processing databases for observational or other kinds of scientific data.

## Opening Data with Pandas

Pandas is very powerful and already functions similar to a database. It has helper functions to directly read and write to compatible databases 


~~~
import pandas as pd
import sqlite3

# Connect to the database
conn = sqlite3.connect('survey.db')
# Read the data with sql into a dataframe
people = pd.read_sql_query('SELECT * from Person LIMIT 1', conn)
~~~
{: .python}
~~~
	id	    personal	family
0	dyer	William	    Dyer
~~~
{: .output}

Pandas can also write to a database

~~~
new_data = pd.DataFrame({"id": ['leighton'], "personal": ['Ben'], "family": ['Leighton']})
new_data.to_sql('Person', conn, if_exists='append', index=False)
~~~
{: .python}

## Duck DB

DuckDB provides many options for working with views of existing data, in memory databases, or creating a database.

We can create a database with DuckDB like

~~~
conn = duckdb.connect('survey3.duckdb')
~~~
{: .python}

If the file 'survey3.duckdb' doesn't exist this will create a new empty duckdb database.

We can then create tables in the database like

~~~
conn.execute("CREATE TABLE Person(id VARCHAR, personal VARCHAR, family VARCHAR)")
conn.execute("CREATE TABLE Site(name VARCHAR, lat VARCHAR, lon VARCHAR)")
conn.execute("CREATE TABLE Survey(taken VARCHAR, person VARCHAR, quant VARCHAR, reading VARCHAR)")
conn.execute("CREATE TABLE Visit(id VARCHAR, site VARCHAR, dated VARCHAR )")
~~~
{: .python}

These tables are empty to begin with. Duckdb can easily load many formats of data. Here we load csv data into each table. 

~~~
conn.execute("INSERT INTO Person SELECT * FROM read_csv_auto('person.csv')")
conn.execute("INSERT INTO Site SELECT * FROM read_csv_auto('site.csv')")
conn.execute("INSERT INTO Survey SELECT * FROM read_csv_auto('survey.csv')")
conn.execute("INSERT INTO Visit SELECT * FROM read_csv_auto('visit.csv')")
~~~
{: .python}

Here we haven't preserved exactly the same types as the original survey.db but we can still perform some queries

~~~
conn.execute("SELECT * FROM Survey as y JOIN Person as p ON p.id = y.person JOIN Visit as v ON v.id = y.taken JOIN Site as s ON s.name = v.site").fetchone()
~~~
{: .python}

## User facing databases

Building applications is different to performing analytics in a database. In python for this use case it is worth looking at SQLAlchemy, ORMs, and Pydantic.

It is also important to santize user input to databases especially in public facing applications. This avoids neafarious users  or bots building special strings that misuse SQL to execute unauthorized commands.

