# All these types of plates

# You invited your family for the greatest of all dinners, and everyone enjoyed it.
# You are now doing the washing-up. Your cousin is cleaning some plates and then giving them to you. You put them in your giant pile of various plates.
# The pile is arranged so that every plate of the same type is grouped. There is no specific order between the plate groups.
# Your cousin gives you one or two plates at a time. When there are two plates, and when they belong to two different groups, it’s always two neighboring groups. Your cousin never gives you plates from unknown groups. But the two plates are not necessarily in the same order as in the pile.
# This washing-up has to be finished fast. So, each time your cousin gives you some plates, you want to insert them in the pile in only one action.
# The pile can be very high (thousands of plates, you have a big family!), so browsing through the whole stack at each insertion can be too long.
# Keep in mind that the pile changes while you add plates to it!


# Example
# Let’s say you begin with this pile of plates:
# flower-decorated plate
# light green plate
# light green plate
# big blue plate
# big blue plate


# The “flower-decorated plate” is at the index 0.
# Your cousin gives you two “light green plates”. They can be inserted at indexes 1, 2, or 3. When multiple indexes are allowed, you must answer the lowest one. You must also answer a boolean to tell if the two plates must be reversed before insertion.
# Then, your cousin gives you a “big blue plate” and a “light green plate”. They must be inserted at the transition between the two groups. It was previously at index 3, but because of the previous insertion, the correct index is now 5. The boolean must be True, because the group of light green plates is before the group of big blue plates.
# Happy washing-up!

from typing import List
def insertPlates(plates: List[int], newplates: List[int])-> (int,bool):
    firstfound = False
    for pos, plate in enumerate(plates):
        if plate != newplates[0] and not firstfound:
            continue
        elif len(newplates) ==1 or newplates[0] == newplates[1]:
            for newplate in newplates:
                plates.insert(pos, newplate)
            return pos, False
        elif pos>0 and plates[pos-1] == newplates[1]:
            plates.insert(pos, newplates[1])
            plates.insert(pos+1,newplates[0])
            return pos, True
        elif plate != newplates[1]:
            firstfound = True
            continue
        else:
            plates.insert(pos, newplates[0])
            plates.insert(pos+1, newplates[1])
            return pos, False  
    return 0, False



plates = ["flower-decorated plate","light green plate","light green plate","big blue plate","big blue plate"]
newplates = ["light green plate", "light green plate"]
print (insertPlates(plates,newplates))
print(plates)
newplates = ["big blue plate", "light green plate"]
print (insertPlates(plates,newplates))
print(plates)
newplates = ["light green plate", "big blue plate"]
print (insertPlates(plates,newplates))
print(plates)
