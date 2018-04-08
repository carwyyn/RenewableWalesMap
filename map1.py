import folium
import pandas
map = folium.Map(location=[52.45,-3.56], zoom_start=8, tiles="Mapbox Bright")

data=pandas.read_csv("juneRenewableDatabase.csv", encoding="ISO-8859-1")
lat = list(data["lat"])
lng = list(data["lng"])
technology = list(data["Technology-Type"])
status = list(data["Development Status (short)"])
name = list(data["Site Name"])


def color_decider(t):
    if t =="Solar Photovoltaics":
        return "yellow"
    elif t == "Wind Onshore":
        return "white"
    elif t == "Large Hydro" or t=="Small Hydro":
        return "blue"
    else:
        return "black"

#folium.Popup(nom, parse_html=True)
def html(nom, tech, stat):
    return nom + " - " + tech + " - " + stat


fg = folium.FeatureGroup(name="Operational")
non = folium.FeatureGroup(name="Not Operational")

for lt, lon, stat, tech, nom in zip(lat, lng, status, technology, name):
    if stat == "Operational":
        fg.add_child(folium.CircleMarker(location=[lt, lon], radius=5, fill_color=color_decider(tech), fill=True, color="grey", fill_opacity=1, popup=folium.Popup(html(nom, tech, stat), parse_html=True)))
    else:
        non.add_child(folium.CircleMarker(location=[lt, lon], radius=5, fill_color=color_decider(tech), fill=True, color="black", fill_opacity=0.5, popup=folium.Popup(html(nom, tech, stat), parse_html=True)))

#fg.add_child(folium.Marker(location=[52.45,-3.56], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
f = folium.Div()
f.add_child = "Hello"

map.add_child(f)
map.add_child(fg)
map.add_child(non)
map.add_child(folium.LayerControl(collapsed=False))

map.save("Map1.html")
