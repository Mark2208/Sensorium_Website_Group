cmake_minimum_required(VERSION 3.10)
# Require modern C++
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project(Github_Test)

file(GLOB_RECURSE SOURCES tester.cpp)
add_executable(testBuild ${SOURCES})

