import requests
import csv
from io import StringIO

class Site(object):
    def __init__(self,name,county,aqi) -> None:
        super().__init__()
        self.site_name = name
        self.county = county
        try:
            self.aqi = int(aqi)
        except:
            self.aqi = 999
    
    @property
    def level(self) -> str:
        if self.aqi <=50:
            return "良好:綠"
        elif 50 < self.aqi <=100:
            return "普通:黃"
        elif 100< self.aqi <=150:
            return "對敏感族群不良 橘"
        elif 150 <self.aqi <=200:
            return "對所有族群不良 紅"
        elif 200 <self.aqi <=300:
            return "非常不良、紫"
        elif 300 <self.aqi <=500:
            return "有害、褐紅色"
        else:
            return "無法估計"

    def __repr__(self) -> str:
        return f"站點:{self.site_name},城市:{self.county},aqi:{self.aqi}"


class Taiwan_AQI():
    API_KEY = "ec3d37d4-25c4-449f-b12b-632e0cc9a3e1"
    @classmethod
    def download_aqi(cls) ->list:
        response=requests.get(f"https://data.epa.gov.tw/api/v2/aqx_p_432?api_key={cls.API_KEY}&limit=1000&sort=ImportDate desc&format=CSV")

        if response.ok:
            #print(response.text)
            #file = open("./lesson17/aqi.csv",mode="w",encoding="utf -8")
            #file.write(response.text)
            #file.close()
            file = StringIO(response.text,newline="")
            csvReader = csv.reader(file)
            next(csvReader)
            dataList =[]
            for item in csvReader:
                site = Site(item[0],item[1],item[2])
                dataList.append(site)
            return dataList

            

            '''
            for item in csvReader:
                print(item[0])
            '''
            
            
        else:
            raise Exception("下載失敗")