import os

#import platform

print(os.getcwd()) # 현재 작업 디렉토리를 반환한다. current working directory
# os.chdir("..") # 현재 작업 디렉토리를 상위 디렉토리로 변경한다. change directory
#print(os.mkdir("Hello")) # 현재 작업 디렉토리에 "Hello"라는 이름의 디렉토리를 생성한다. make directory
#print(os.rmdir("Hello")) # 현재 작업 디렉토리에 "Hello"라는 이름의 디렉토리를 제거한다. remove directory
os.chdir("C:/src/SPC2026") # 현재 작업 디렉토리를 "C:/src/SPC2026"으로 변경한다. change directory
cwd = os.getcwd() # 현재 작업 디렉토리를 반환한다. current working directory
print(cwd)
print(os.listdir(cwd)) # 현재 작업 디렉토리의 파일과 디렉토리 목록

# print(os.listdir()) # 현재 작업 디렉토리의 파일과 디렉토리 목록
# print(os.name) # 운영체제의 이름을 반환한다. posix, nt,
#print(platform.system()) # 운영체제의 이름을 반환한다. Windows, Linux, Darwin(MacOS)
#print(platform.uname()) # 운영체제의 이름, 버전, 머신 등의 정보를 반환한다.