import collections
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:

    # collections.defaultdict는 딕셔너리(dictionary)와 거의 비슷하지만 key값이 없을 경우 미리 지정해 놓은 초기(default)값을 반환하는 dictionary이다.
    anagrams = collections.defaultdict(list)

    # sort 함수는 리스트명.sort( ) 형식으로 "리스트형의 메소드이며 리스트 원본 값을 직접 수정합니다.
    # sorted 함수는 sorted( 리스트명 ) 형식으로 "내장 함수"이며 리스트 원본 값은 그대로이고 정렬 값을 반환합니다.
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())
