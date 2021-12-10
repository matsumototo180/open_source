import folium
import pandas as pd

electric_stations = pd.read_csv("data/pt5/電気自動車充電スタンド.csv", encoding="cp932", header=1)
kinki_prefs = pd.read_csv("data/pt5/kinki_pop.csv")

electric_stations.columns

electric_map = folium.Map(location=[electric_stations["緯度"].mean(), electric_stations["経度"].mean()],
                          zoom_start=11,
                          min_zoom=8)

for row in electric_stations.itertuples():
    popup = '<span style="white-space: nowrap;">' + row.スタンド名 + '</span>'
    folium.Marker(location=[row.緯度, row.経度], popup=popup).add_to(electric_map)

electric_map.save('electric_stations.html')


kinki_prefs.columns

kinki_prefs["人口"] = kinki_prefs["人口"].str.replace(",", "").astype("int")
kinki_prefs["人口比"] = kinki_prefs["人口"]/kinki_prefs["人口"].sum()

kinki_map = folium.Map(location=[kinki_prefs["緯度"].mean(), kinki_prefs["経度"].mean()],
                        zoom_start=10,
                        min_zoom=8)

for row in kinki_prefs.itertuples():
    popup = '<span style="white-space: nowrap;">' + row.府県庁所在地 + '</span>'
    folium.CircleMarker(location=[row.緯度, row.経度], radius=row.人口比*500, popup=popup).add_to(kinki_map)

kinki_map.save('kinki_prefs.html')
