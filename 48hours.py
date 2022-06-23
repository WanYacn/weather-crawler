import requests
from lxml import html
import csv


etree = html.etree


file = open("test.csv","w",encoding='utf-8', newline='')
row = ['序号','时间','温度','简介','降雨概率','风速','体感温度','紫外线指数','湿度','云量','降雨量']
csv_writer = csv.writer(file,dialect="excel")
csv_writer.writerow(row)
file.close()

file = open("test.csv","a",encoding='utf-8', newline='')




list = []

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

url3 = '' #填入url
resp3 = requests.get(url=url3, headers=headers)

resp3.close()

html3 = etree.HTML(resp3.text)


deadline = html3.xpath("//*[@id='WxuHourlyCard-main-74f43669-10ed-4577-a8c4-85ad9d041036']/section/div[1]/text()")
print(deadline)



for i in range(72):
    id_data = "detailIndex" + str(i)


    #获取时间
    parameter_time = "//*[@id='" + id_data + "']/summary/div/div/h3/text()"
    time = html3.xpath(parameter_time)

    #获取温度
    parameter_temperature = "//*[@id='" + id_data + "']/summary/div/div/div[1]/span/text()"
    temperature = html3.xpath(parameter_temperature)

    #获取简介
    parameter_introduction = "//*[@id='" + id_data + "']/summary/div/div/div[2]/span/text()"
    introduction = html3.xpath(parameter_introduction)

    #获取降雨概率
    parameter_rain = "//*[@id='" + id_data + "']/summary/div/div/div[3]/span/text()"
    rain = html3.xpath(parameter_rain)

    #获取风速
    parameter_wind = "//*[@id='" + id_data + "']/summary/div/div/div[4]/span/text()"
    wind = html3.xpath(parameter_wind)

    #获取体感温度
    parameter_body_temperature = "//*[@id='" + id_data + "']/div/div[2]/ul/li[1]/div/span[2]/text()"
    body_temperature = html3.xpath(parameter_body_temperature)

    #获取紫外线指数
    parameter_UV = "//*[@id='" + id_data + "']/div/div[2]/ul/li[4]/div/span[2]/text()"
    UV = html3.xpath(parameter_UV)

    #获取湿度
    parameter_humidity = "//*[@id='" + id_data + "']/div/div[2]/ul/li[3]/div/span[2]/text()"
    humidity = html3.xpath(parameter_humidity)

    #获取云量
    parameter_cloud = "//*[@id='" + id_data + "']/div/div[2]/ul/li[5]/div/span[2]/text()"
    cloud = html3.xpath(parameter_cloud)

    #获取降雨量
    parameter_accumulation = "//*[@id='" + id_data + "']/div/div[2]/ul/li[6]/div/span[2]/text()"
    accumulation = html3.xpath(parameter_accumulation)

    if time != list:
        #print(time,temperature,introduction,rain,wind,body_temperature,UV,humidity,cloud,accumulation)
        row2 = [i,time,temperature,introduction,rain,wind,body_temperature,UV,humidity,cloud,accumulation]
        csv_writer = csv.writer(file)
        csv_writer.writerow(row2)

file.close()