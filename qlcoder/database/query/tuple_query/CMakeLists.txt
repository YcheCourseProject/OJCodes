cmake_minimum_required(VERSION 3.4)
project(tuple_query)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14 -O3")

add_executable(tuple_query main.cpp pretty_print.h util.h tuple_info.h query_info.h)
add_executable(regex_test regex_test.cpp)