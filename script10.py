import random
import folium
import pandas as pd

class Dice:
    def __init__(self, start=0, end=88):
        self.start = start
        self.end = end
        self.progress = start
    
    def __show_result(self, result):
        print(f'サイコロ：{result} {self.progress}マス目' + (' ゴール！' if self.progress == self.end else ''))
    
    def __is_finished(self):
        return True if self.progress == self.end else False
    
    def roll(self):
        result = random.randint(1, 6)
        self.progress = min([self.progress + result, self.end])
        self.__show_result(result)
        if self.__is_finished():
            self.progress = 0

def create_map(df):
    map = folium.Map(location=[df["緯度"].mean() - 0.3, df["経度"].mean() - 0.3], zoom_start=8, min_zoom=6)
    folium.PolyLine(locations=df[["緯度", "経度"]]).add_to(map)
    return map

def add_progress_marker(map, label, lat, lon):
    popup = folium.Popup('<span style="white-space: nowrap;">' + label + '</span>', show=True)
    folium.Marker(location=[lat, lon], popup=popup, icon=folium.Icon(color='red')).add_to(map)

temples = pd.read_csv("./data/pt10/ohenro.csv", encoding="cp932")

dice = Dice()

dice.roll()
map = create_map(temples)
temple = temples.iloc[dice.progress - 1]
add_progress_marker(map, temple["札所"], temple["緯度"], temple["経度"])
map
