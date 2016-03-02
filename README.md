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