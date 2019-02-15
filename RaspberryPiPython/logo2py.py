#
# Turle Graphics Examples from Measure, Topology and Fractal Geometry
# Gerald Edgar
# Ported from logo to python
#


from turtle import *
from math import sqrt

# to Koch :depth :size
#   if :depth = 0 [forward :size stop][
#      Koch :depth - 1 :size / 3
#      left 60
#      Koch :depth - 1 :size / 3
#      right 120
#      Koch :depth - 1 :size / 3
#      left 60
#      Koch :depth - 1 :size / 3]
# end

def Koch(depth, size):
    if(depth == 0):
        forward(size)
    else:
        Koch(depth-1, size/3)
        left(60)
        Koch(depth-1, size/3)
        right(120)
        Koch(depth-1, size/3)
        left(60)
        Koch(depth-1, size/3)

# make "stwo sqrt 2
# to leaf :depth :size
#   if :depth < 1 [forward 2 * :size back 2 * :size] [
#     forward :size
#     leaf :depth - 2 :size / 2
#     back :size
#     left 45
#     leaf :depth - 1 :size / :stwo
#     right 90
#     leaf :depth - 1 :size / :stwo
#     left 45]
# end

sqrt2 = sqrt(2)

def leaf(depth, size):
    if depth < 1:
        forward(2*size)
        back(2*size)
    else:
        forward(size)
        leaf(depth-2, size/2)
        back(size)
        left(45)
        leaf(depth-1, size/sqrt2)
        right(90)
        leaf(depth-1, size/sqrt2)
        left(45)

# to spiral :size
#   if :size < 1 [stop] [
#   forward :size
#   right 60
#   spiral :size * 0.8]
# end

def spiral(size):
    if (size > 1):
        forward(size)
        right(60)
        spiral(size * 0.8)


speed("fastest")
#left(90)
#leaf(11,200)
Koch(3, 200)
#spiral(200)
