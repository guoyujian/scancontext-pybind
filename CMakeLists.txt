cmake_minimum_required(VERSION 3.4...3.18)
project(cmake_example)


set(CMAKE_CXX_STANDARD 14)
#add_subdirectory(pybind11)

if (${CMAKE_SYSTEM_NAME} STREQUAL "Windows")
    set(pybind11_DIR D:/gyj-projects/pybind11_test/pybind11-install/share/cmake/pybind11)
elseif(${CMAKE_SYSTEM_NAME} STREQUAL "Darwin")
    set(pybind11_DIR /Users/gmet/CLionProjects/pybind11/install/share/cmake/pybind11)
endif ()

find_package(pybind11 REQUIRED)
find_package(Eigen3 REQUIRED)


# add_module: wrapper.cpp
pybind11_add_module(cmake_example
#        src/main.cpp
        python/wrapper.cpp
        scancontext/include/scancontext/Scancontext.cpp
)

# *引入scancontext 头文件
target_include_directories(cmake_example
        PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/scancontext/include
)

# EXAMPLE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
if (${CMAKE_SYSTEM_NAME} STREQUAL "Windows")
    target_compile_definitions(cmake_example
            PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO}
            PRIVATE _USE_MATH_DEFINES
    )
elseif(${CMAKE_SYSTEM_NAME} STREQUAL "Darwin")
    target_compile_definitions(cmake_example
            PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO}
    )
endif ()


# targetlink: eigen3
target_link_libraries(cmake_example
        PRIVATE Eigen3::Eigen
#        PRIVATE nanoflann::nanoflann
)