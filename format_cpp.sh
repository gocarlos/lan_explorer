#!/bin/sh

find $(dirname "$0")/ \
    -not \( -path "*/vendor/*" -prune \) \
    -not \( -path "*/build/*" -prune \) \
    -not \( -path "*/parts/*" -prune \) \
    -not \( -path "*/stage/*" -prune \) \
    -not \( -path "*/prime/*" -prune \) \
    \( -name *.h -o -name *.hpp -o -name *.c -o -name *.cc -o -name *.cpp \) \
    | xargs clang-format -i
