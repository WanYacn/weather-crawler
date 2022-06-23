import requests
from lxml import html

etree = html.etree

url = '' #填入url
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
resp = requests.get(url=url, headers=headers)
# print(resp.text)
resp.close()

html = etree.HTML(resp.text)

Air_quality_index = html.xpath("//*[@id='WxuAirQuality-sidebar-aa4a4fb6-4a9b-43be-9004-b14790f57d73']/div/section/div/div/div[1]/svg/text/text()")
sunrise = html.xpath("//*[@id='SunriseSunsetContainer-fd88de85-7aa1-455f-832a-eacb037c140a']/div/div/div/div[1]/p/text()")
sunset = html.xpath("//*[@id='SunriseSunsetContainer-fd88de85-7aa1-455f-832a-eacb037c140a']/div/div/div/div[2]/p/text()")
body_temperature = html.xpath("//*[@id='todayDetails']/section/div[1]/div[1]/span[1]/text()")
high = html.xpath("//*[@id='todayDetails']/section/div[2]/div[1]/div[2]/span[1]/text()")
low = html.xpath("//*[@id='todayDetails']/section/div[2]/div[1]/div[2]/span[2]/text()")
wind = html.xpath("//*[@id='todayDetails']/section/div[2]/div[2]/div[2]/span/text()")
humidity = html.xpath("//*[@id='todayDetails']/section/div[2]/div[3]/div[2]/span/text()")
dew_point = html.xpath("//*[@id='todayDetails']/section/div[2]/div[4]/div[2]/span/text()")
air_pressure = html.xpath("//*[@id='todayDetails']/section/div[2]/div[5]/div[2]/span/text()")
UV_Index = html.xpath("//*[@id='todayDetails']/section/div[2]/div[6]/div[2]/span/text()")
visibility = html.xpath("//*[@id='todayDetails']/section/div[2]/div[7]/div[2]/span/text()")
moon_phase = html.xpath("//*[@id='todayDetails']/section/div[2]/div[8]/div[2]/text() ")

print(sunrise,sunset,body_temperature,high,low,wind,humidity,dew_point,air_pressure,UV_Index,visibility,moon_phase)
