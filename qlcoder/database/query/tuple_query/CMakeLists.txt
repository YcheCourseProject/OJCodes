cmake_minimum_required(VERSION 3.6)
project(tuple_query)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")

set(SOURCE_FILES main.cpp prettyprint.h util.h)
add_executable(tuple_query ${SOURCE_FILES})