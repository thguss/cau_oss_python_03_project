# %%
"""
파일과 관련된 함수를 구현해놓은 모듈
"""

import chardet
import os
import sys

def print_listdir(path='./', depth=0):
    """
    path 경로부터 존재하는 모든 하위 폴더/파일의 목록을 출력하는 함수
    Args:
        path  (string): 출력하고자 하는 경로의 시작 위치
        depth (int)   : 파일의 단계 (사용시 0으로 고정)
    Examples:
        >>> print_listdir('../') # 상위 폴더부터 존재하는 모든 폴더/파일의 목록을 출력
    """
    # 시작의 depth는 0으로 고정
    if sys._getframe(1).f_code.co_name != 'print_listdir': depth=0

    # 파일의 목록
    dirs = os.listdir(path)
    for d in dirs:
        # depth가 1이상일 경우 depth만큼 들여쓰기
        if depth > 0 :
            for _ in range(depth):
                print('  ', end='')
            print('|-', end='')
        print(f'[{d}]')
        d = path + '/' + d
        # 폴더일 경우 재귀호출로 하위 목록 출력
        if os.path.isdir(d):
            print_listdir(d, depth+1)

def read_file(path):
    """
    파일의 첫번째 줄을 읽어 인코딩을 확인한 뒤,
    인코딩에 맞게 파일을 읽어 리스트로 반환하는 함수
    Args:
        path (string): 파일 경로
    Returns:
        list of string: 라인(\n)단위로 분리된 문자열
    Examples:
        >>> list_str = read_file('./input.txt')
    """
    # encoding 확인
    enc = 'utf-8'
    with open(path, 'rb') as f:
        tmp = f.readline()
        enc = chardet.detect(tmp)['encoding']

    # file 객체 생성
    list_str = list()
    with open(file=path, mode='r', encoding=enc) as f:
        for line in f:
            list_str.append(line.strip())   # 공백(\n) 제거하여 리스트에 추가
    del list_str[0]

    return list_str


if __name__ == '__main__':
    # 경로의 파일/폴더 목록 출력
    print_listdir('./')
    
    # 파일 열기
    strs = read_file("./input/free_parking_spot_seoul.csv")

    # 출력
    for s in strs:
        print(s)