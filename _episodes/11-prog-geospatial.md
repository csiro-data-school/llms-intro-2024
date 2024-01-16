---
title: Geospatial Data Science with Python and Databases
teaching: 30
exercises: 15
questions:
- "How can I load geospatial data in a database?"
- "What processing can be done with geospatial database?"
objectives:
- "Basic familiarity with shapefiles"
- "Loading shapefiles with Geopandas"
- "Use a geospatial operational on data in DuckDB"
- "Visualise geospatial data from DuckDB"

keypoints:
- "Shapefiles are a common geospatial format that can be used in DuckDB"
- "Geospatial data can be processed in some specialized databases"
- "Visualising Geospatial Data from DuckDB is possible using GeoPandas and Folium"
---

## Geospaital Data Science with Python and Databases

Geospatial data is data about locations. Two common types of geospatial data are grids of pixels called Rasters or sets of points called Vectors. Rasters are often images, for example from a satellite. Vectors can be point data, lines, or polygons representing locations or boundaries in the world.

Geospatial databases mostly work with vector data. Common operations on vector data include finding the interscection of areas, finding data within an area, or calculating distance between locations. For example we maybe interested in finding what crop fields overlap with different soil types or which farms fall within different water catchments.

Some databases provide geospatial capability: spatialite a variant of sqlite, DuckDB-spatial a plugin for DuckDB, and PostGIS an extension of postgresql are some emerging and established technologies.

## Understanding geospatial data from a shapefile

Lets load a shapefile using geopandas and examine the data structure 

~~~
import geopandas as gpd
gdf = gpd.read_file('./ibra61_sub/ibra61_sub.shp')
gdf.columns
~~~
{: .python}


~~~
gdf.head(1)
~~~
{: .python}

This file defines georegions for describing ecosystems data. It has a tabluar structure with rows representing distinct georegions. Within each row columsn appear to provide names and codes associated with the georegion as well as a geometry. 

The geometry information is key in shapefiles. In this case the geometry defines a polygon that shows the area on earth covered by the georegion. 

We can plot this data using geopandas like


~~~
gdf.plot()
~~~
{: .python}


## Loading geospatial data in a database

DuckDB can readily load the shape file as a database.

~~~
import duckdb
duckdb.sql('INSTALL spatial; LOAD spatial;')
duckdb.sql('DESCRIBE SELECT * from "./ibra61_sub/ibra61_sub.shp"')
~~~
{: .python}

Notice that the database has typed the columns and that the geom column has a type of "GEOMETRY". This means that DuckDB has recognized the data as geospatial and so we can perform geospatial operations on it.

First lets see how to go back from spatial data in DuckDB to a geopandas dataframe so we can visualise data as we go. 

To convert the data to a regular pandas dataframe we can do:
~~~
df = duckdb.sql('SELECT ST_AsText(geom) as textgeo, SUB_NAME  from "./ibra61_sub/ibra61_sub.shp"').df()
df
~~~
{: .python}

ST_AsText is a database function that converts the geometry back to a standard text data format. The df() function converts the result to a dataframe.

To convert the dataframe to a geopandas dataframe we need to convert the text representation of the geometry back into a geometry object understood by geopandas. A shapely represenation works and to convert we call the wkt.loads function on all the data in the textgeo column using the apply function.  

~~~
from shapely import wkt

df['textgeo'] = df['textgeo'].apply(wkt.loads)
gdf = gpd.GeoDataFrame(df, geometry="textgeo", crs='4326')
gdf.plot()
~~~
{: .python}

> ## Filter the data 
>
> Extend this query to find all the records where the SUB_NAME is 'Hodgkinson Basin'  
> `duckdb.sql("SELECT * from './ibra61_sub/ibra61_sub.shp'... `
> > ## Solution
> > duckdb.sql("SELECT * from './ibra61_sub/ibra61_sub.shp' where SUB_NAME = 'Hodgkinson Basin'")
> >
> {: .solution}
{: .challenge}

## Applying a bounding box

An example of a particular geospatial operation we often want to perform is restricting data to a region. We can use a bounding box for this specifying the corners of the box.

~~~
df = duckdb.sql("""SELECT *, ST_AsText(geom) as textgeo from './ibra61_sub/ibra61_sub.shp'
WHERE ST_Contains(
   ST_MakeEnvelope(143, -45, 150, -40),
  geom
)""").df()
df['textgeo'] = df['textgeo'].apply(wkt.loads)
gdf = gpd.GeoDataFrame(df, geometry="textgeo", crs='4326')
gdf.plot()
~~~
{: .python}

Here we use ST_MakeEnvelope to make an bounding box and then ST_Contains to find all geometries within it.

Read more about DuckDB spatial functions at https://duckdb.org/docs/extensions/spatial.html

## Processing a very large dataset

Here we have another dataset that uses bioregions to describe forest age. Its from https://www.data.qld.gov.au/dataset/2020-21-slats-report, metadata is sparse. More information at https://www.data.qld.gov.au/dataset/2020-21-slats-report/resource/31c6db4e-7e29-4015-98b0-249eb2a7fcc1

~~~
duckdb.sql('DESCRIBE select * from e2021_woodytab.parquet')
~~~
{: .python}

That dataset has a woody_age column that might describe forest age and a subbioregion column that might match the bioregions described in SUB_NAME.

To list the distinct subbioregions in the data we can do

~~~
duckdb.sql('select distinct(subbioregion) from e2021_woodytab.parquet')
~~~
{: .python}

We can check to see if these subbioregions match some of our bioregions by sorting both datasets

~~~
duckdb.sql('select distinct(subbioregion) from e2021_woodytab.parquet ORDER BY subbioregion')
~~~
{: .python}

~~~
duckdb.sql("select distinct(SUB_NAME) from './ibra61_sub/ibra61_sub.shp' ORDER BY SUB_NAME")
~~~
{: .python}

We can see a couple of candidate matches. If we look at the results for one likely match we can understand the data better.

~~~
duckdb.sql("SELECT count(*) from e2021_woodytab.parquet where subbioregion = 'Alice Tableland'")
~~~
{: .python}

~~~
duckdb.sql("SELECT * from e2021_woodytab.parquet where subbioregion = 'Alice Tableland'")
~~~
{: .python}

There are a > 300,000 records matching the 'Alice Tableland' biosubregion and it looks as if each record might be at a  small perhaps plot or paddock scale. It's not clear what woody_age means possibly it is time since disturbance in years. 

Lets try to plot the mean woody_age for each subbioregion. First lets create a new table (in DuckDBs temporary in memory database) called mean_age.

~~~
duckdb.sql('create table mean_age as select mean(woody_age) as mage, subbioregion from e2021_woodytab.parquet group by subbioregion')
~~~
{: .python}

~~~
duckdb.sql('select * from mean_age')
~~~
{: .python}

Now we need to associate each of the "subbioregion" codes in each row of mean_age with a geometry. We can do this by joining the new mean_age table with the ibra61_sub.shp SUB_NAME data. 

~~~
df = duckdb.query("""
SELECT 
    ST_AsText(ibra.geom) as textgeo, 
    ibra.SUB_NAME, 
    mean_age.mage 
FROM "./ibra61_sub/ibra61_sub.shp" as ibra 
INNER JOIN mean_age 
ON ibra.SUB_NAME = mean_age.subbioregion
""")
~~~
{: .python}

In the query we join the shape file to the mean_age table using match between SUB_NAME and subbioregion. INNER JOIN finds the interesection as we are only interested in records that have a match across the tables. We also follow the previous pattern of converting the resulting ibra geometry to text in a new colulmn called textgeo to help us plot the data.

~~~
df['textgeo'] = df['textgeo'].apply(wkt.loads)
gdf = gpd.GeoDataFrame(df, geometry="textgeo", crs='4326')
gdf.plot(column='mage', legend=True)
""")
~~~
{: .python}

Why might mean age not be a good measure of the actual mean age across each bioregion? We aren't considering the area of each row in the slats dataset. Some rows represent ages for larger areas. Also we don't know that the slats data completely covers the bioregion. 

~~~
duckdb.sql("DROP TABLE mean_age") 

duckdb.sql('create table mean_age as select sum(woody_age * areaha)  / sum(areaha) as mage, subbioregion from e2021_woodytab.parquet group by subbioregion')

df = duckdb.query("""
SELECT 
    ST_AsText(ibra.geom) as textgeo, 
    ibra.SUB_NAME, 
    mean_age.mage
FROM "./ibra61_sub/ibra61_sub.shp" as ibra 
INNER JOIN mean_age 
ON ibra.SUB_NAME = mean_age.subbioregion
""").df()

df['textgeo'] = df['textgeo'].apply(wkt.loads)

gdf = gpd.GeoDataFrame(df, geometry="textgeo", crs='4326')
gdf.plot(column='mage', legend=True)
~~~
{: .python}

## Incorporating Folium for Dynamic Spatial Plotting

Folium is a useful library for interactive and dynamic spatial plotting.

First lets import some of the requsite library 

~~~
import matplotlib.pyplot as plt
import matplotlib.colors
import folium
import numpy as np
~~~
{: .python}

And plot an empty interactive map

~~~
m = folium.Map(location=[-25, 135], zoom_start=4)
m
~~~
{: .python}

and some functions to normalize the ages, note that LLMs can be very useful for writing these functions

~~~
def colorize(age, min_age, max_age, exponent=0.5):
    cmap = plt.cm.plasma
    # Normalize the age value to the range [0, 1]
    normalized_age = (age - min_age) / (max_age - min_age)
    # Apply a power transformation to spread out the colors
    scaled_age = normalized_age ** exponent
    rgba = cmap(scaled_age)
    return matplotlib.colors.rgb2hex(rgba)

def style_function(feature):
    age = feature['properties']['mage']
    return {
        'fillColor': colorize(age, min_age, max_age),
        'color': 'black',
        'weight': 1,
    }
~~~
{: .python}

And finally a Geojson layer with a pop up for mean age and then replot the map

~~~
folium.GeoJson(
    gdf[['mage', 'textgeo', 'SUB_NAME']].to_json(),
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(fields=['SUB_NAME',  'mage'])
).add_to(m)

m
~~~
{: .python}






















































## 


## Loading a large amounts of data with duckdb

For example we can plot some of the datasets.

~~~
library(RSQLite)
connection <- dbConnect(SQLite(), "survey.db")
results <- dbGetQuery(connection, "SELECT Site.lat, Site.long FROM Site;")
print(results)
dbDisconnect(connection)
~~~
{: .r}
~~~
     lat    long
1 -49.85 -128.57
2 -47.15 -126.72
3 -48.87 -123.40
~~~
{: .output}

The program starts by importing the `RSQLite` library.
If we were connecting to MySQL, DB2, or some other database,
we would import a different library,
but all of them provide the same functions,
so that the rest of our program does not have to change
(at least, not much)
if we switch from one database to another.

Line 2 establishes a connection to the database.
Since we're using SQLite,
all we need to specify is the name of the database file.
Other systems may require us to provide a username and password as well.

On line 3, we retrieve the results from an SQL query.
It's our job to make sure that SQL is properly formatted;
if it isn't,
or if something goes wrong when it is being executed,
the database will report an error.
This result is a dataframe with one row for each entry and one column for each column in the database.

Finally, the last line closes our connection,
since the database can only keep a limited number of these open at one time.
Since establishing a connection takes time,
though,
we shouldn't open a connection,
do one operation,
then close the connection,
only to reopen it a few microseconds later to do another operation.
Instead,
it's normal to create one connection that stays open for the lifetime of the program.

Queries in real applications will often depend on values provided by users.
For example,
this function takes a user's ID as a parameter and returns their name:

~~~
full name for dyer: William Dyer
~~~
{: .output}

We use string concatenation on the first line of this function
to construct a query containing the user ID we have been given.
This seems simple enough,
but what happens if someone gives us this string as input?

~~~
dyer'; DROP TABLE Survey; SELECT '
~~~
{: .sql}

It looks like there's garbage after the user's ID,
but it is very carefully chosen garbage.
If we insert this string into our query,
the result is:

~~~
SELECT personal || ' ' || family FROM Person WHERE id='dyer'; DROP TABLE Survey; SELECT '';
~~~
{: .sql}

If we execute this,
it will erase one of the tables in our database.

This is called an [SQL injection attack]({{ site.github.url }}/reference.html#sql-injection-attack),
and it has been used to attack thousands of programs over the years.
In particular,
many web sites that take data from users insert values directly into queries
without checking them carefully first.
A very [relevant XKCD](https://xkcd.com/327/) that explains the
dangers of using raw input in queries a little more succinctly:

![relevant XKCD](https://imgs.xkcd.com/comics/exploits_of_a_mom.png)

Since an unscrupulous parent might try to smuggle commands into our queries in many different ways,
the safest way to deal with this threat is
to replace characters like quotes with their escaped equivalents,
so that we can safely put whatever the user gives us inside a string.
We can do this by using a [prepared statement]({{ site.github.url }}/reference.html#prepared-statement)
instead of formatting our statements as strings.
Here's what our example program looks like if we do this:

~~~
library(RSQLite)
connection <- dbConnect(SQLite(), "survey.db")

getName <- function(personID) {
  query <- "SELECT personal || ' ' || family FROM Person WHERE id == ?"
  return(dbGetPreparedQuery(connection, query, data.frame(personID)))
}

print(paste("full name for dyer:", getName('dyer')))

dbDisconnect(connection)
~~~
{: .r}
~~~
full name for dyer: William Dyer
~~~
{: .output}

The key changes are in the query string and the `dbGetQuery` call (we use dbGetPreparedQuery instead).
Instead of formatting the query ourselves,
we put question marks in the query template where we want to insert values.
When we call `dbGetPreparedQuery`,
we provide a dataframe
that contains as many values as there are question marks in the query.
The library matches values to question marks in order,
and translates any special characters in the values
into their escaped equivalents
so that they are safe to use.

> ## Filling a Table vs. Printing Values
>
> Write an R program that creates a new database in a file called
> `original.db` containing a single table called `Pressure`, with a
> single field called `reading`, and inserts 100,000 random numbers
> between 10.0 and 25.0.  How long does it take this program to run?
> How long does it take to run a program that simply writes those
> random numbers to a file?
{: .challenge}

> ## Filtering in SQL vs. Filtering in R
>
> Write an R program that creates a new database called
> `backup.db` with the same structure as `original.db` and copies all
> the values greater than 20.0 from `original.db` to `backup.db`.
> Which is faster: filtering values in the query, or reading
> everything into memory and filtering in R?
{: .challenge}

## Database helper functions in R

R's database interface packages (like `RSQLite`) all share
a common set of helper functions useful for exploring databases and
reading/writing entire tables at once.

To view all tables in a database, we can use `dbListTables()`:

~~~
connection <- dbConnect(SQLite(), "survey.db")
dbListTables(connection)
~~~
{: .r}
~~~
"Person"  "Site"    "Survey"  "Visit"
~~~
{: .output}


To view all column names of a table, use `dbListFields()`:

~~~
dbListFields(connection, "Survey")
~~~
{: .r}
~~~
"taken"   "person"  "quant"   "reading"
~~~
{: .output}


To read an entire table as a dataframe, use `dbReadTable()`:

~~~
dbReadTable(connection, "Person")
~~~
{: .r}
~~~
        id  personal   family
1     dyer   William     Dyer
2       pb     Frank  Pabodie
3     lake  Anderson     Lake
4      roe Valentina  Roerich
5 danforth     Frank Danforth
~~~
{: .output}


Finally to write an entire table to a database, you can use `dbWriteTable()`.
Note that we will always want to use the `row.names = FALSE` argument or R
will write the row names as a separate column.
In this example we will write R's built-in `iris` dataset as a table in `survey.db`.

~~~
dbWriteTable(connection, "iris", iris, row.names = FALSE)
head(dbReadTable(connection, "iris"))
~~~
{: .r}
~~~
  Sepal.Length Sepal.Width Petal.Length Petal.Width Species
1          5.1         3.5          1.4         0.2  setosa
2          4.9         3.0          1.4         0.2  setosa
3          4.7         3.2          1.3         0.2  setosa
4          4.6         3.1          1.5         0.2  setosa
5          5.0         3.6          1.4         0.2  setosa
6          5.4         3.9          1.7         0.4  setosa
~~~
{: .output}

And as always, remember to close the database connection when done!

~~~
dbDisconnect(connection)
~~~
{: .r}

