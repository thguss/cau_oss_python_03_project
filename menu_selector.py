import file_manager
import parking_spot_manager

def start_process(path):
    str_list = file_manager.read_file(path) # file에서 문자열 리스트 읽어오기
    spots = parking_spot_manager.str_list_to_class_list(str_list) # 문자열 리스트 객체 변환 및 객체 리스트(spots) 반환

    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            parking_spot_manager.print_spots(spots) # 객체 리스트 출력
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                spots = parking_spot_manager.filter_by_name(spots, keyword) # 필터 수행 및 반환되는 새로운 리스트로 기존 리스트 대체
            elif select == 2:
                keyword = input('type city:')
                spots = parking_spot_manager.filter_by_city(spots, keyword) # 필터 수행 및 반환되는 새로운 리스트로 기존 리스트 대체
            elif select == 3:
                keyword = input('type district:')
                spots = parking_spot_manager.filter_by_district(spots, keyword) # 필터 수행 및 반환되는 새로운 리스트로 기존 리스트 대체
            elif select == 4:
                keyword = input('type ptype:')
                spots = parking_spot_manager.filter_by_ptype(spots, keyword) # 필터 수행 및 반환되는 새로운 리스트로 기존 리스트 대체
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                location = (min_lat, max_lat, min_lon, max_lon) # 위치 필터링 조건을 튜플로 저장
                spots = parking_spot_manager.filter_by_location(spots, location) # 필터 수행 및 반환되는 새로운 리스트로 기존 리스트 대체
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                spots = parking_spot_manager.sort_by_keyword(spots, keyword) # 정렬 수행 및 반환되는 새로운 리스트로 기존 리스트 대체
            else: print("invalid input")
        elif select == 4:
            print("Exit") # Exit 출력
            break # 반복문 종료 (반복문 종료 후 프로그램 종료)
        else:
            print("invalid input")