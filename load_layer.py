import folium
import pickle

m = folium.Map([45.35, -121.6972], zoom_start=12)

layer = pickle.load(open("layer1.pickle", "rb"))
layer.add_to(m)

folium.LayerControl().add_to(m)

m.save("test_with_loaded_layer.html")
