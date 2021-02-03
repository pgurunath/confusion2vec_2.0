#
# Copyright (c) 2016-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

cmake_minimum_required(VERSION 2.8.9)
project(c2v_fasttext)

# The version number.
set (c2v_fasttext_VERSION_MAJOR 0)
set (c2v_fasttext_VERSION_MINOR 1)

include_directories(c2v_fasttext)

set(CMAKE_CXX_FLAGS " -pthread -std=c++11 -funroll-loops -O3 -march=native")

set(HEADER_FILES
    src/args.h
    src/autotune.h
    src/densematrix.h
    src/dictionary.h
    src/c2v_fasttext.h
    src/loss.h
    src/matrix.h
    src/meter.h
    src/model.h
    src/productquantizer.h
    src/quantmatrix.h
    src/real.h
    src/utils.h
    src/vector.h)

set(SOURCE_FILES
    src/args.cc
    src/autotune.cc
    src/densematrix.cc
    src/dictionary.cc
    src/c2v_fasttext.cc
    src/loss.cc
    src/main.cc
    src/matrix.cc
    src/meter.cc
    src/model.cc
    src/productquantizer.cc
    src/quantmatrix.cc
    src/utils.cc
    src/vector.cc)


if (NOT MSVC)
  include(GNUInstallDirs)
  configure_file("c2v_fasttext.pc.in" "c2v_fasttext.pc" @ONLY)
  install(FILES "${CMAKE_BINARY_DIR}/c2v_fasttext.pc" DESTINATION ${CMAKE_INSTALL_LIBDIR}/pkgconfig)
endif()

add_library(c2v_fasttext-shared SHARED ${SOURCE_FILES} ${HEADER_FILES})
add_library(c2v_fasttext-static STATIC ${SOURCE_FILES} ${HEADER_FILES})
add_library(c2v_fasttext-static_pic STATIC ${SOURCE_FILES} ${HEADER_FILES})
set_target_properties(c2v_fasttext-shared PROPERTIES OUTPUT_NAME c2v_fasttext
  SOVERSION "${c2v_fasttext_VERSION_MAJOR}")
set_target_properties(c2v_fasttext-static PROPERTIES OUTPUT_NAME c2v_fasttext)
set_target_properties(c2v_fasttext-static_pic PROPERTIES OUTPUT_NAME c2v_fasttext_pic
  POSITION_INDEPENDENT_CODE True)
add_executable(c2v_fasttext-bin src/main.cc)
target_link_libraries(c2v_fasttext-bin pthread c2v_fasttext-static)
set_target_properties(c2v_fasttext-bin PROPERTIES PUBLIC_HEADER "${HEADER_FILES}" OUTPUT_NAME c2v_fasttext)
install (TARGETS c2v_fasttext-shared
    LIBRARY DESTINATION lib)
install (TARGETS c2v_fasttext-static
    ARCHIVE DESTINATION lib)
install (TARGETS c2v_fasttext-static_pic
    ARCHIVE DESTINATION lib)
install (TARGETS c2v_fasttext-bin
    RUNTIME DESTINATION bin
 PUBLIC_HEADER DESTINATION include/c2v_fasttext)
