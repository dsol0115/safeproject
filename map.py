import folium
import csv
import json

# Create map object
m = folium.Map(location=[37.533157, 127.075434], zoom_start=16)

data = open('gis_data.csv', 'r', encoding='utf-8')
rdr = csv.reader(data)
next(rdr)

for line in rdr:
    location_tmp_list = []
    location_tmp_list.append(line)
    
    folium.CircleMarker(
        location=[location_tmp_list[0][1], location_tmp_list[0][2]],
        radius=120,
        color='#428bca',
        fill=True,
        fill_color='#428bca'
).add_to(m)
##파랑색 지하철역


data2 = open('girl.csv', 'r', encoding='utf-8')
rdr2 = csv.reader(data2)
next(rdr2)

for line in rdr2:
    location_tmp_list2 = []
    location_tmp_list2.append(line)
    
    folium.CircleMarker(
        location=[location_tmp_list2[0][1], location_tmp_list2[0][2]],
        radius=100,
        color='#d9534f',
        fill=True,
        fill_color='#d9534f'
).add_to(m)
##빨강색안심지킴이집



data3 = open('delivery.csv', 'r', encoding='utf-8')
rdr3 = csv.reader(data3)
next(rdr3)


for line in rdr3:
    location_tmp_list3 = []
    location_tmp_list3.append(line)
    
    folium.CircleMarker(
        location=[location_tmp_list3[0][1], location_tmp_list3[0][2]],
        radius=100,
        color='#fcba03',
        fill=True,
        fill_color='#fcba03'
).add_to(m)
##노랑색 안심택배

data4 = open('police.csv', 'r', encoding='utf-8')
rdr4 = csv.reader(data4)
next(rdr4)

for line in rdr4:
    location_tmp_list4 = []
    location_tmp_list4.append(line)
    
    folium.CircleMarker(
        location=[location_tmp_list4[0][1], location_tmp_list4[0][2]],
        radius=150,
        color='#5cb85c',
        fill=True,
        fill_color='#5cb85c'
).add_to(m)
##초록색 경찰서

folium.Marker(location=[37.533401,127.065842],
            icon=folium.Icon(color='red', icon='star')
            ).add_to(m)

folium.Marker(location=[37.533109, 127.072994],
            icon=folium.Icon(color='red', icon='star')
            ).add_to(m)
folium.Marker(location=[37.533959, 127.076661],
            icon=folium.Icon(color='red', icon='star')
            ).add_to(m)

# Generate map
m.save('map.html')