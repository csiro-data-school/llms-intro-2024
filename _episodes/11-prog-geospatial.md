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