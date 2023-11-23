---
title: LLMs for SQL
teaching: 10
exercises: 10
questions:
- "How can I use LLMs to help with databases and SQL?"
objectives:
- "Learn to use LLMs flexibly not just for one kind of task"
- "Understand the pitfalls of LLMs"

keypoints:
- "LLMs can be used for tasks including tutoring, debugging, writing code, fixing errors, and search"
- "LLMs can generate incorrect or unexpected responses"
- "Testing is essential and this too can be in collaboration with an LLM"
---
## LLMs 

Large Language Models or LLMs are a class of AI that are powerful general purpose tools. The best known
LLM is ChatGPT but there are many closed and open source LLMs in use and development.

LLMs can be engaged with through natural language chat, in many ways they are like talking to an expert
human but have the advantages of being tireless, deeply knowleagble and fast. LLMs can also be wrong while
convincingly appearing to be right.

As people become familiar with LLMs there is a perception that LLMs are useful for only one or two tasks.
Actually LLMs are very flexible. Here we will learn how to use LLMs to assist us with working with Data
through Databases, SQL and related tools.

## LLMs for Understanding

LLMs should support learning not replace it at least not completely. We can use LLMs to help us understand and
work with databases. 

For example the process of ensuring data in a database isn't duplicated and is distributed across interlinked tables is called normalization. Lets ask the LLM about it
~~~
What does database normalization mean?
~~~
{: .txt}

The LLM may respond with a comprehensive description of Normal Forms. That might be too much to begin with so lets rephrase

~~~
Very simply what is database normalization?
~~~
{: .txt}

This should provide a better response. 

Returning to the first response we may not understand what is meant by the LLM description of  second nomral form 

> Second Normal Form (2NF): This builds on the first normal form by ensuring that all non-key attributes are fully functionally dependent on the primary key.


~~~
For database second normal form what are some examples of when attributes meeting the definition of fully functionally dependent on the primary key and some examples where they don't?
~~~
{: .txt}

The LLM should respond with some examples of database tables that do and do not conform to second normal form and explain why

## LLMs for writing SQL

Returning to survey.db we can directly ask the LLM to build a query to find the total number of 
surveys person. There are multiple ways to do this but in all cases the LLM needs some understanding of the database structure.

One way to do this is to ask the LLM for a query to get a succinct description of the tables

~~~
In duckdb I need a succint description of all the columns and column types across a whole schema write an sql query to do this
~~~
{: .txt}

We may have to modify the result a bit but a query like gives us a good result

~~~
duckdb.sql("""SELECT table_name, column_name, data_type
FROM temp.information_schema.columns
ORDER BY table_name, ordinal_position;""").df()
~~~
{: .py}

Now it's possible to ask the LLM like

~~~
Given the following schema write a query that gets the total number of surveys performed by each person and orders it high to low

0 Person id VARCHAR  
1 Person personal VARCHAR  
2 Person family VARCHAR  
3 Site name VARCHAR  
4 Site lat DOUBLE  
5 Site long DOUBLE  
6 Survey taken BIGINT  
7 Survey person VARCHAR  
8 Survey quant VARCHAR  
9 Survey reading DOUBLE  
10 Visit id BIGINT  
11 Visit site VARCHAR  
12 Visit dated VARCHAR  
~~~
{: .py}

LLMs aren't too fussy about things like spelling and formatting. They may perfom better with careful prompting but are often highly robust to poor spelling, incomplete requests, and bad formatting. In this case the query to the LLM doesn't actually ask for SQL but the LLM guesses this is the most likely meaning. Notice also for this query the LLM also correctly infered the primary / foreign key relationship between survey person and person id

The result was

~~~
SELECT 
    p.id, 
    p.personal, 
    p.family, 
    COUNT(s.person) AS total_surveys
FROM 
    Person p
JOIN 
    Survey s ON p.id = s.person
GROUP BY 
    p.id, p.personal, p.family
ORDER BY 
    total_surveys DESC;
~~~
{: .txt}

In this case we may have sufficient knowledge to know that this is right. However it is possible for the LLM to make mistakes or produce an unexpected but accurate interpretation of the question leading to unexpected behaviour.

## Testing LLM responses

Ascertaining whether an LLM response is fit for purpose is difficult because we use LLMs to supplement and extend our knowledge and thus don't always know what the right answer is.

Some strategies for testing LLM responses

1. Spot test from a collection of results. Iin the survey example above `Anderson Lake` peformed 7 total surveys. This is a small number and by listing the contents of the Survey table we can manually confirm this is right.
2. Sanity Check results. In the survey example the results range between 7 and 3 surveys. This looks sane there are no negative numbers, the numbers look feasible for the number of surveys a human could perform and there are no outliers. 
3. Ask a follow up question. We know that the sum of the surveys per person shouldn't exceed the total number of surveys.

> ## Asking follow up questions for QA 
>
> Ask the LLM to generate a query that will get the total number of surveys. 
> > ## Solution
> >  
> >
> >  
> > Given the following schema write a query that gets the total number of surveys
> > 
> > 0 Person id VARCHAR  
> > 1 Person personal VARCHAR  
> > 2 Person family VARCHAR  
> > 3 Site name VARCHAR  
> > 4 Site lat DOUBLE  
> > 5 Site long DOUBLE  
> > 6 Survey taken BIGINT  
> > 7 Survey person VARCHAR  
> > 8 Survey quant VARCHAR  
> > 9 Survey reading DOUBLE  
> > 10 Visit id BIGINT  
> > 11 Visit site VARCHAR  
> > 12 Visit dated VARCHAR  
> {: .solution}
{: .challenge}

