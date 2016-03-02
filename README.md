## Download Global datasets

http://openstreetmapdata.com/data

- Land Polygon
- Water Polygon
- Coastlines

## Download Sub-Region / Country datasets

http://download.geofabrik.de/

- admin
- aeroways
- amenities
- barriers
- buildings
- housenumbers
- landusages
- places
- roads
- transport
- waterareas
- waterways

## Install PostGIS

https://hub.docker.com/r/kartoza/postgis/

## Install Imposm3

https://github.com/omniscale/imposm3/#installation

## Run Imposm3

```bash
./imposm3 import
    -connection postgis://docker:docker@localhost:25432/gis \
    -mapping ./mapping.json \
    -read ./estonia-latest.osm.pbf \
    -write
```

## Export as Shapefile

Single command line

```bash
pgsql2shp -f "./output/admin" \
    -h localhost \
    -p 25432 \
    -u docker \
    -P docker gis \
    "SELECT * FROM import.osm_admin"
```

Running with a python script

```python
python exportShapefile.py
```

## Preview Data

Using QGIS or ArcMap, you can connect to the PostgreSQL server or add the shapefiles directly.

## Benchmarks

Using the Poland.osm.pbf (789MB) data downloaded from GeoFabrik.

### Computer Specs

- Ubuntu 15.10
- Memory: 7.8 GiB
- Processor: Intel® Core™2 Quad CPU Q8400 @ 2.66GHz × 4 
- OS type: 64-bit

### Import

Importing OSM data (22m12s)

### Export

Exporting to Shapefiles (9m27s)
