# There are N warriors, the ith of which has a health of H_i units and can deal 
# D_i units of damage per second. They are confronting a boss who has unlimited health and can deal 
# B units of damage per second. Both the warriors and the boss deal damage continuously 
# − for example, in half a second, the boss deals B/2
# The warriors feel it would be unfair for many of them to fight the boss at once, so they'll select just two representatives to go into battle. One warrior 
# i will be the front line, and a different warrior j will back them up. During the battle, the boss will attack warrior 
# i until that warrior is defeated (that is, until the boss has dealt H_i units of damage to them), and will then attack warrior 
# j until that warrior is also defeated, at which point the battle will end. Along the way, each of the two warriors will do damage to the boss as long as they are undefeated.
# Of course, the warriors will never prevail, but they'd like to determine the maximum amount of damage they could deal to the boss for any choice of warriors 
# i and j before the battle ends.

from typing import List
# Write any import statements here

def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
  # Write your code here

  maxdamage = 0
  combos = [(H[i] * D[i], H[i], D[i], i) for i in range(N)]
  combos.sort(reverse=True)
  for i in range(min(N, 100)):
    hd_i, h_i, d_i, idx_i = combos[i]
    for j in range(i+1,min(N,100)):
      hd_j, h_j, d_j, idx_j = combos[j]
      best = hd_i + hd_j + max(h_j * d_i, h_i *d_j)
      if maxdamage < best:
        maxdamage = best 
  return maxdamage/B 


import unittest
N = 3
H = [2, 1, 4]
D = [3, 1, 2]
B = 4
print("Expected Value: 6.5")
print(f"Actual Value: {getMaxDamageDealt(N, H, D, B)}")
