# You are creating a special painting on a canvas which may be represented as a 2D Cartesian plane. You start by placing a thin brush at the origin (0,0) and then make 
# N axis-aligned strokes without lifting the brush off of the canvas. For the ith stroke, you'll move your brush L_i units from its current position in a direction indicated by the character D_i, which is either U (up), D (down), L (left), or R (right), while leaving behind a line segment of paint between the brush's current and new positions. For example, if 
# L1 = 5 and D1 = L, you'll draw a stroke between coordinates (0,0) and (−5,0), with your brush ending up at coordinates (−5,0). Note that each stroke is either horizontal or vertical, and that each stroke (after the first) begins where the previous stroke ended.

# This painting is being marketed as a work of mathematical art, and its value is based on the number of times a certain mathematical symbol appears in it specifically, the plus sign. A plus sign is considered to be present at a certain position if and only if, for each of the 4 cardinal directions (up, down, left, and right), there's paint leading from the point in that direction (or, vice versa, leading to that point from that direction). Note that the paint from arbitrarily many strokes of your brush might come together to form any given plus sign, and that at most one plus sign may be considered to exist at any given position.

# Determine the number of positions in the painting at which a plus sign is present.

# Constraints
# 2 ≤ N ≤ 2,000,000
# 1 ≤ L_i ≤ 1,000,000,000
# D_i in {U, D, L, R}

from typing import List
# Write any import statements here

def add_line(lines, lineval, ends):
  p1, p2 = ends
  if p1 > p2:
    p1, p2 = p2, p1
  if lineval not in lines:
    lines[lineval] = [set(range(p1,p2+1))]
  else:
    curset = set(range(p1, p2+1))
    points =lines[lineval]
    added = False
    i = 0
    while i<len(points):
      pset = points[i]
      if pset.intersection(curset):
        if not added:
          prev_i = i
          points[i] = pset.union(curset)
          added = True
          i +=1
        else:
          points[prev_i] = points[prev_i].union(pset)
          del points[i]
      else:
        i+=1
    if not added:
      points.append(curset)


def get_crossing_line(in_lines, lineval):
    res = []
    for line, points in in_lines.items():
        for pset in points:
            if lineval in pset \
            and lineval-1 in pset \
            and lineval+1 in pset:
                res.append(line)
    return res
  
  
def getPlusSignCount(N: int, L: List[int], D: str) -> int:
  # Write your code here
  x_lines = {}
  y_lines = {}
  x = 0
  y = 0
  for path, length in zip(D,L):
    if path in ('U','D'):
      prev_y = y
      if path == 'U':
        y += length
      else:
        y -= length
      add_line(x_lines, x, (prev_y, y))
    else:
      prev_x = x
      if path == 'R':
        x += length
      else:
        x -= length
      add_line(y_lines, y,(prev_x, x))

  print(x_lines)
  print(y_lines)
  total_crosses = 0
  for x_val in x_lines:
    res = get_crossing_line(y_lines, x_val)
    for y_val in res:
        for pset in x_lines[x_val]:
            if y_val in pset \
            and y_val-1 in pset \
            and y_val+1 in pset:
                total_crosses += 1
  return total_crosses


N = 9
L = [6, 3, 4, 5, 1, 6, 3, 3, 4]
D = "ULDRULURD"
res  =getPlusSignCount(N, L, D)
print("Expected result: 4")
print("Actual result: ",res)
