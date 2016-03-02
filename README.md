## Download Global datasets

### OpenStreetMap Data (Shapefiles WGS84)

- Land Polygon - http://openstreetmapdata.com/data/land-polygons
- Water Polygon - http://openstreetmapdata.com/data/water-polygons
- Coastlines - http://openstreetmapdata.com/data/coastlines

### ESRI World (Layer Packages)

**World**

- [World Regions](http://www.arcgis.com/home/item.html?id=84dbc97915244e35808e87a881133d09)
- [World Elevation Conours](http://www.arcgis.com/home/item.html?id=40285e34dd3a453db84ab3acbd81b37d)
- [World Regions](http://www.arcgis.com/home/item.html?id=84dbc97915244e35808e87a881133d09)
- [World Cities](http://www.arcgis.com/home/item.html?id=dfab3b294ab24961899b2a98e9e8cd3d)
- [World Administrative Divisions](https://www.arcgis.com/home/item.html?id=d86e32ea12a64727b9e94d6f820123a2)
- [World Time Zones](http://www.arcgis.com/home/item.html?id=1d14b1662a3c4375aa2e31008beb103b)
- [World Water Bodies](http://www.arcgis.com/home/item.html?id=e750071279bf450cbd510454a80f2e63)
- [World Major Rivers](https://www.arcgis.com/home/item.html?id=44e8358cf83a4b43bc863646cd695945)
- [World Roads](http://www.arcgis.com/home/item.html?id=83535020ce154bd5a498957c159e3a99)
- [World Topography and Bathymetry](http://www.arcgis.com/home/item.html?id=88a7995ddb0b4f21a9497f3dcf6f9aec)

**North America**

- [North America Interstate Highways](https://www.arcgis.com/home/item.html?id=00b5b0d2a6f548e6813bcf9536249a03)
- [North America Major Roads](http://www.arcgis.com/home/item.html?id=06e71cbbefab401fb99b6c2bb5139487)
- [World Continents](https://www.arcgis.com/home/item.html?id=a3cb207855b348a297ab85261743351d)
- [North America Water Polygons](http://www.arcgis.com/home/item.html?id=1630b19fafbe4c9589306d967e418088)
- [North America States Provinces](http://www.arcgis.com/home/item.html?id=0549fcf91a47426ab423ea0f36ccc3d4)
- [North America Cities](http://www.arcgis.com/home/item.html?id=f56a057acfc44356aa54b2818ac5700f)
- [North America Streetscarto](http://www.arcgis.com/home/item.html?id=642bcf6a1dc347769c555f694d4e4d9a)
- [North America Rivers](https://www.arcgis.com/home/item.html?id=a06189262e694834b5d68e1a84030969)
- [North America Coastal Water Bodies](http://www.arcgis.com/home/item.html?id=e74122bd34384b85938772fc45fabcf6)


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
