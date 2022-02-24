import folium
import pandas

map = folium.Map(location=[38.58, -99.89], zoom_start=6, tiles="Stamen Terrain")
fg_v = folium.FeatureGroup(name="Volcanoes")
fg_p = folium.FeatureGroup(name="Populations")

data = pandas.read_csv("Volcanoes.txt")
lat = data["LAT"]
lon = data["LON"]
ele = data["ELEV"]
name = data["NAME"]

html = """Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m"""

def color_producer(elevation):
    if elevation <= 2000:
        return 'green'
    elif 2000 < elevation <=3000:
        return 'orange'
    else:
        return 'red'

for lt, ln, el, name in zip(lat, lon, ele, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg_v.add_child(folium.CircleMarker(location=[lt, ln], radius=15, popup=folium.Popup(iframe), tooltip='<strong>Click here if you want</strong>', fill_color=color_producer(el), color='grey', fill_opacity=0.7))

fg_p.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

folium.Marker()

map.add_child(fg_v)
map.add_child(fg_p)
folium.TileLayer('Stamen Terrain').add_to(map)
folium.TileLayer('Stamen Toner').add_to(map)
folium.TileLayer('Stamen Water Color').add_to(map)
folium.TileLayer('cartodbpositron').add_to(map)
folium.TileLayer('cartodbdark_matter').add_to(map)
#folium.LayerControl().add_to(map)
map.add_child(folium.LayerControl())

map.save(r"C:\Users\AlyGh\Desktop\Map.html")
