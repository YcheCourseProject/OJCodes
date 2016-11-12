cmake_minimum_required(VERSION 3.4)
project(cpp_timeline)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -g -O1")

set(MD5_FILES md5.h md5.cpp)
set(TIME_LINE_FILES timeline.h timeline.cpp)
set(SOURCE_FILES main.cpp ${MD5_FILES} ${TIME_LINE_FILES})
add_executable(cpp_timeline ${SOURCE_FILES})