# 파일의 open, close가 필요없다.
import linecache
line = linecache.getline('test1.txt', 3)
print(type(line), line)

in_file = open('test1.txt', 'r', encoding='UTF-8')
# 줄 단위로 읽는다.
for i in range(4):
    line = in_file.readline()
print(line)
# 파일의 처음으로 되돌린다. (seek(n) -> n번째 문자를 읽는다.)
in_file.seek(0)
# 줄 단위로 전체를 읽어 리스트 형태로 반환한다.
lines = in_file.readlines()
print(lines)
print(lines[3])
# 파일의 처음으로 되돌린다. (seek(n) -> n번째 문자를 읽는다.)
in_file.seek(0)
# enumerate(list): list의 인덱스와 리스트의 값을 모두 추출하는 함수이다.
# linenum에 인덱스가 들어가고, line에 리스트(입력라인)의 값이 들어간다.
for linenum, line in enumerate(in_file):
    if linenum == 3:
        print(line)
in_file.close()

# with open('파일명') as 객체명:
# 들여쓰기 한 구문이 끝나면 자동으로 파일을 닫아준다.
with open('chicken.txt', 'r', encoding='utf-8') as f:
    print(f.readlines()[3])
