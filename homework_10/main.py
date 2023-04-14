
from tools import Taiwan_AQI

def get_best(dataList) ->list:
    sorted_data = sorted(dataList,key=lambda x:x.aqi)
    for item_x in sorted_data[:3]:
        print(item_x)
    

def get_bad(dataList) ->list:
    sorted_data = sorted(dataList,key=lambda x:x.aqi,reverse=True)
    for item_y in sorted_data[:3]:
        print(item_y)


def print_site_level(datalist) -> None:
    sorted_data = sorted(datalist,key=lambda z:z.aqi)
    for item_z in sorted_data:
        print(item_z)

def print_site_name() -> str:
    pass

def main():
    try:
        aqi_list = Taiwan_AQI.download_aqi()
    except Exception as err:
        print(str(err))
        return
    '''
    for item in aqi_list:
        print(item)
    '''
    get_best(aqi_list)
    print("=========")
    get_best(aqi_list)
    print("=========")
    print_site_level(aqi_list)
    print("=========")
    print_site_name(aqi_list)



if __name__ == "__main__":
    main()