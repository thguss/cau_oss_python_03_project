class parking_spot:
    # you have to implement 'constructor(생성자)' and 'get' method

    def __init__(self, name, city, district, ptype, longitude, latitude): # 생성자
        self.__item = dict() # 객체 참조 공유를 막기 위해 생성자 내에 변수 선언
        self.__item['name'] = name # 문자열
        self.__item['city'] = city # 문자열
        self.__item['district'] = district # 문자열
        self.__item['ptype'] = ptype # 문자열
        self.__item['longitude'] = float(longitude) # 실수형
        self.__item['latitude'] = float(latitude) # 실수형

    def get_item(self, keyword = 'name'): # __item[keyword] 값 반환
        return self.__item[keyword]

    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

def str_list_to_class_list(str_list): # 문자열 리스트에서 각 문자열을 parking_spot 객체로 변환하여 리스트 삽입 및 객체 리스트 반환
    spots = list() # 객체 리스트 선언

    for str in str_list:
        spot_info = str.split(',') # 파싱
        name = spot_info[1]
        city = spot_info[2]
        district = spot_info[3]
        ptype = spot_info[4]
        longitude = spot_info[5]
        latitude = spot_info[6]
        spot = parking_spot(name, city, district, ptype, longitude, latitude) # 객체 변환
        spots.append(spot) # 리스트 삽입

    return spots # 객체 리스트 반환

def print_spots(spots):
    print(f"---print elements({len(spots)})---") # 리스트 길이 출력
    for spot in spots: # 객체 리스트에서 객체 하나씩 출력 (__str__)
        print(spot)

def filter_by_name(spots, name): # 이름 필터링
    spots = [x for x in spots if name in x.get_item('name')] # keyword(name) 문자열을 포함한 __item['name'] 값을 가진 객체 필터링하여 리스트 함축
    return spots # 필터링한 리스트 반환

def filter_by_city(spots, city): # 시도 필터링
    spots = [x for x in spots if city in x.get_item('city')] # keyword(city) 문자열을 포함한 __item['city'] 값을 가진 객체 필터링하여 리스트 함축
    return spots # 필터링한 리스트 반환

def filter_by_district(spots, district): # 시군구 필터링
    spots = [x for x in spots if district in x.get_item('district')] # keyword(district) 문자열을 포함한 __item['district'] 값을 가진 객체 필터링하여 리스트 함축
    return spots # 필터링한 리스트 반환

def filter_by_ptype(spots, ptype): # 주차장유형 필터링
    spots = [x for x in spots if ptype in x.get_item('ptype')] # keyword(ptype) 문자열을 포함한 __item['ptype'] 값을 가진 객체 필터링하여 리스트 함축
    return spots # 필터링한 리스트 반환

def filter_by_location(spots, locations): # 위치 필터링
    # min_lat 이상이고 max_lat 이하의 __item['latitude'] 값을 가지고, min_long 이상이고 max_long 이하의 __item['longitude'] 값을 가지는 객체 필터링하여 리스트 함축
    spots = [x for x in spots if locations[0] <= x.get_item('latitude') <= locations[1] and locations[2] <= x.get_item('longitude') <= locations[3]]
    return spots # 필터링한 리스트 반환


# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    import file_manager
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    spots = filter_by_district(spots, '동작')
    print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)