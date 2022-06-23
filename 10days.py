import requests
from lxml import html
import csv


etree = html.etree


file = open("test.csv","w",encoding='utf-8', newline='')
row = ['序号','日期','最高温度','最低温度','白天湿度','夜间湿度','白天降雨概率','夜间降雨概率','白天风速','夜间风速','白天紫外线指数','日出时间','日落时间','当日简介','白天详细介绍','夜间详细介绍']
csv_writer = csv.writer(file,dialect="excel")
csv_writer.writerow(row)
file.close()

file = open("test.csv","a",encoding='utf-8', newline='')


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

url2 = '' #填入url
resp2 = requests.get(url=url2, headers=headers)

resp2.close()

html2 = etree.HTML(resp2.text)


deadline = html2.xpath("//*[@id='WxuDailyCard-main-a43097e1-49d7-4df7-9d1a-334b29628263']/section/div[1]/text()")
print(deadline)

for i in range(15):


    #获取时间
    id_data = "detailIndex" + str(i)
    parameter_time = "//*[@id='" + id_data + "']/summary/div/div/h3/text()"
    time = html2.xpath(parameter_time)




    # 获取最高温
    if i != 0 :
        id_data = "detailIndex" + str(i)
        parameter_high = "//*[@id='" + id_data + "']/div/div[1]/div/div[1]/span/text()"
        high = html2.xpath(parameter_high)
    else:
        high = "[null]"


    #获取最低温
    if i == 0:
        #parameter_low = "//*[@id='" + id_data + "']/div/div[1]/div/div[1]/span/text()"
        parameter_low = "//*[@id='detailIndex0']/div/div[1]/div/div[1]/span/text()"
    else:
        id_data = "detailIndex" + str(i)
        parameter_low = "//*[@id='" + id_data + "']/div/div[3]/div/div[1]/span/text()"
    low = html2.xpath(parameter_low)



    # 获取白天湿度
    if i != 0 :
        id_data = "detailIndex" + str(i)
        parameter_humidity_day = "//*[@id='" + id_data + "']/div/div[2]/ul/li[1]/div/span[2]/text()"
        humidity_day = html2.xpath(parameter_humidity_day)
    else:
        humidity_day = "[null]"


    #获取夜晚湿度
    if i == 0:
        parameter_humidity_night = "//*[@id='detailIndex0']/div/div[2]/ul/li[1]/div/span[2]/text()"
    else:
        id_data = "detailIndex" + str(i)
        parameter_humidity_night = "//*[@id='" + id_data + "']/div/div[4]/ul/li[1]/div/span[2]/text()"
    humidity_night = html2.xpath(parameter_humidity_night)



    # 获取白天降雨概率
    if i != 0 :
        id_data = "detailIndex" + str(i)
        parameter_rain_day = "//*[@id='" + id_data + "']/div/div[1]/div/div[3]/div[1]/span/text()"
        rain_day = html2.xpath(parameter_rain_day)
    else:
        rain_day = "[null]"



    #获取夜晚降雨概率
    if i == 0:
        parameter_rain_night = "//*[@id='detailIndex0']/div/div[1]/div/div[3]/div[1]/span/text()"
    else:
        id_data = "detailIndex" + str(i)
        parameter_rain_night = "//*[@id='" + id_data + "']/div/div[3]/div/div[3]/div[1]/span/text()"
    rain_night = html2.xpath(parameter_rain_night)



    # 获取白天风速
    if i != 0 :
        id_data = "detailIndex" + str(i)
        parameter_wind_day = "//*[@id='" + id_data + "']/div/div[1]/div/div[3]/div[2]/span/text()"
        wind_day = html2.xpath(parameter_wind_day)
    else:
        wind_day = "[null]"



    #获取夜晚风速
    if i == 0:
        parameter_wind_night = "//*[@id='detailIndex0']/div/div[1]/div/div[3]/div[2]/span/text()"
    else:
        id_data = "detailIndex" + str(i)
        parameter_wind_night = "//*[@id='" + id_data + "']/div/div[3]/div/div[3]/div[2]/span/text()"
    wind_night = html2.xpath(parameter_wind_night)



    # 获取白天紫外线指数
    if i != 0 :
        id_data = "detailIndex" + str(i)
        parameter_UV_day = "//*[@id='" + id_data + "']/div/div[2]/ul/li[2]/div/span[2]/text()"
        UV_day = html2.xpath(parameter_UV_day)
    else:
        UV_day = "[null]"



    # 获取日出时间
    if i != 0 :
        id_data = "detailIndex" + str(i)
        parameter_sunrise = "//*[@id='" + id_data + "']/div/div[2]/ul/li[3]/div/span[2]/text()"
        sunrise = html2.xpath(parameter_sunrise)
    else:
        sunrise = "[null]"


    # 获取日落时间
    if i != 0 :
        id_data = "detailIndex" + str(i)
        parameter_sunrset = "//*[@id='" + id_data + "']/div/div[2]/ul/li[4]/div/span[2]/text()"
        sunset = html2.xpath(parameter_sunrset)
    else:
        sunset = "[null]"




    #获取天气简介
    id_data = "detailIndex" + str(i)
    parameter_introduction_brief =  "//*[@id='" + id_data + "']/summary/div/div/div[2]/span/text()"
    introduction_brief = html2.xpath(parameter_introduction_brief)



    # 获取白天详细介绍
    if i != 0 :
        id_data = "detailIndex" + str(i)
        parameter_detailed_introduction_day = "//*[@id='" + id_data + "']/div/div[1]/p/text()"
        detailed_introduction_day = html2.xpath(parameter_detailed_introduction_day)
    else:
        detailed_introduction_day = "[null]"



    #获取夜晚详细介绍
    if i == 0:
        parameter_detailed_introduction_night = "//*[@id='detailIndex0']/div/div[1]/p/text()"
    else:
        id_data = "detailIndex" + str(i)
        parameter_detailed_introduction_night = "//*[@id='" + id_data + "']/div/div[3]/p/text()"
    detailed_introduction_night = html2.xpath(parameter_detailed_introduction_night)


    #print(i,high,low,humidity_day,humidity_night,rain_day,rain_night,wind_day,wind_night,UV_day,sunrise,sunset,introduction_brief,detailed_introduction_day,detailed_introduction_night)

    row2 = [i,high,low,humidity_day,humidity_night,rain_day,rain_night,wind_day,wind_night,UV_day,sunrise,sunset,introduction_brief,detailed_introduction_day,detailed_introduction_night]
    csv_writer = csv.writer(file)
    csv_writer.writerow(row2)

file.close()


