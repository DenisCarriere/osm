import subprocess

tables = [
    'admin',
    'aeroways',
    'amenities',
    'barrierpoints',
    'barrierways',
    'buildings',
    'housenumbers',
    'housenumbers_interpolated',
    'landusages',
    'landusages_gen0',
    'landusages_gen1',
    'places',
    'roads',
    'roads_gen0',
    'roads_gen1',
    'transport_areas',
    'transport_points',
    'waterareas',
    'waterareas_gen0',
    'waterareas_gen1',
    'waterways',
    'waterways_gen0',
    'waterways_gen1'
]
path = './output'

for item in tables:
    # Bash Command
    # pgsql2shp -f "./output/admin" -h localhost -p 25432 -u docker -P docker gis "SELECT * FROM import.osm_admin"

    output = "{path}/{item}".format(path=path, item=item)
    query = "SELECT * FROM import.osm_{item}".format(item=item)
    subprocess.call(['pgsql2shp', '-f', output, '-h', 'localhost', '-p', '25432', '-u', 'docker', '-P', 'docker', 'gis', query])
