import re
def solution(files):
    lst = []
    answer = []
    for i in range(len(files)):
        input = files[i].lower()
        # str = re.findall('[a-z]+', input)[0]으로 할때 Head가 F-가 아닌 F가 되므로 오류 발생했다.
        str = re.split('\d+', input)[0]
        num = int(re.findall('\d+', files[i])[0])
        lst.append((str,num,i))
    sortedLst = sorted(lst)

    for i in range(len(sortedLst)):
        idx = sortedLst[i][2]
        answer.append(files[idx])
    return answer

f = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

print(solution(f))

