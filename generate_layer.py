import folium
import pickle


datalake_path = "standardized/ProductData/VIA/layers/"

layer_name = "layer1"

fg = folium.FeatureGroup(name=layer_name, show=True)

folium.Marker(
    location=[45.3288, -121.6625],
    tooltip="Click me!",
    popup="Mt. Hood Meadows",
    icon=folium.Icon(icon="cloud"),
).add_to(fg)

folium.Marker(
    location=[45.3311, -121.7113],
    tooltip="Click me!",
    popup="Timberline Lodge",
    icon=folium.Icon(color="green"),
).add_to(fg)

layer = pickle.dumps(fg)
with open(f"{layer_name}.pickle", "wb") as f:
    f.write(layer)
