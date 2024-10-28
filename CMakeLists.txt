cmake_minimum_required(VERSION 3.4...3.18)
project(cmake_example)


set(CMAKE_CXX_STANDARD 14)
#add_subdirectory(pybind11)

set(pybind11_DIR /Users/gmet/CLionProjects/pybind11/install/share/cmake/pybind11)
find_package(pybind11 REQUIRED)
find_package(Eigen3 REQUIRED)

# *引入scancontext 头文件
include_directories(
        scancontext/include
)

# add_module: wrapper.cpp
pybind11_add_module(cmake_example
#        src/main.cpp
        python/wrapper.cpp
        scancontext/include/scancontext/Scancontext.cpp
)

# EXAMPLE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
target_compile_definitions(cmake_example
                           PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})


# targetlink: eigen3和nanoflann
target_link_libraries(cmake_example
        PRIVATE Eigen3::Eigen
#        PRIVATE nanoflann::nanoflann
)