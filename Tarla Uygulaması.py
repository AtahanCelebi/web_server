import folium,os
from folium.features import CustomIcon
from folium.plugins import MeasureControl

m = folium.Map(location=[38.3375,31.4000],control_scale=True,zoom_start=16)

"""
kw = {
    'prefix': 'fa',
    'color': 'green',          #Markerlara yeşil veya herhangi bir renk ve açı sembolu eklenebilir
}
angle = 180
icon = folium.Icon(angle=angle, **kw)
folium.Marker(location=[38.3375, 31.4010], icon=icon, tooltip=str('yesil')).add_to(m)
"""

tooltip = 'Tarla Gözlem Uygulaması'
folium.Marker([38.3375, 31.4010], popup='<i>Node 1</i>', tooltip=tooltip).add_to(m) #Dikey,yatay
folium.Marker([38.3375, 31.4050], popup='<i>Node 2</i>', tooltip=tooltip).add_to(m)
folium.Marker([38.3420, 31.4010], popup='<i>Node 4</i>', tooltip=tooltip).add_to(m)
folium.Marker([38.3420, 31.4050], popup='<i>Node 3</i>', tooltip=tooltip).add_to(m)

folium.Marker(
    location=[38.3400, 31.4030],
    popup='Hava Durumu',
    icon=folium.Icon(color='blue', icon='cloud')
).add_to(m)


coordinates = [
    [38.3375, 31.4010],
    [38.3420, 31.4010],
    [38.3420, 31.4050],
    [38.3375, 31.4050],
    [38.3375, 31.4010],
    ]
folium.PolyLine(
    smooth_factor=50,
    locations=coordinates,
    color='green',
    tooltip='Şeker Pancarı Tarlası',
    weight=5
).add_to(m)




url = 'https://img.icons8.com/color/48/000000/{}'.format   #Belli bir koordinata resim ekle
icon_image = url('')
shadow_image = url('beet.png')
icon = CustomIcon(
    icon_image,
    icon_size=(38, 95),
    icon_anchor=(22, 94),
    shadow_image=shadow_image,
    shadow_size=(50, 64),
    shadow_anchor=(4, 62),
    popup_anchor=(-3, -76)
)
marker = folium.Marker(
    location=[38.3390, 31.4026],
    icon=icon,
    popup='Şeker Pancarı Tarlası'
)
m.add_child(marker)



""""
url = ('https://raw.githubusercontent.com/SECOORA/static_assets/'  #Kuzey Yıldızı
       'master/maps/img/rose.png')
FloatImage(url, bottom=0, left=0).add_to(m)
"""


folium.raster_layers.TileLayer(     # Farklı tür harita desenleri
    tiles='http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
    attr='google',
    name='google maps',
    max_zoom=20,
    subdomains=['mt0', 'mt1', 'mt2', 'mt3'],
    overlay=False,
    control=True,
).add_to(m)
folium.raster_layers.TileLayer(
    tiles='http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
    attr='google',
    name='google street view',
    max_zoom=20,
    subdomains=['mt0', 'mt1', 'mt2', 'mt3'],
    overlay=False,
    control=True,
).add_to(m)
folium.raster_layers.WmsTileLayer(
    url='https://demo.boundlessgeo.com/geoserver/ows?',
    layers='nasa:bluemarble',
    name='bluemarble',
    fmt='image/png',
    overlay=False,
    control=True,
).add_to(m)
folium.raster_layers.WmsTileLayer(
    url='http://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0r.cgi',
    name='test',
    fmt='image/png',
    layers='nexrad-n0r-900913',
    attr=u'Weather data © 2012 IEM Nexrad',
    transparent=True,
    overlay=True,
    control=True,
).add_to(m)
folium.LayerControl().add_to(m)




m.add_child(MeasureControl())
m.add_child(folium.LatLngPopup())
m.save('index.html')
os.startfile("index.html")
