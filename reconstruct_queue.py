def reconstructQueue(people):
    people.sort(key=lambda x:(x[0], -x[1])) # sort people as ascending by height; descending by number of people in the front
    invs_needed = [p[1] for p in people] # in this order, p[1] also means the number of inversion needed, and this list is used for mapping each people
    helper(0, len(people), people, invs_needed) # merge sort-like helper function
    # print(invs_needed) at last, invs_needed will be all zeros, which means no inversion is needed, thus, the order of people is the answer
    return people

def helper(start, end, people, invs_needed):
    if start + 1 >= end: # if the length of the list is 0 or 1, no inversion can be made, just return
        return
    mid = (start + end) // 2
    helper(start, mid, people, invs_needed)
    helper(mid, end, people, invs_needed) # post order-like function call order, from top to bottom, downwise direction
    # Then merge from bottom to top, upwide direction
    temp_people, temp_invs_needed = [], [] # extra length = start - end space for storing sorted people and remain inversions
    l, r = start, mid
    inv_count = 0 # whenever a people from right part is put to the merged list, one inversion for all remaining unmerged left is made, while the people from right itself's inversion needed is not changed
    while l < mid and r < end:
        # first merge the people needs fewer inversions
        if invs_needed[r] < invs_needed[l] - inv_count:
            inv_count += 1
            temp_people.append(people[r])
            temp_invs_needed.append(invs_needed[r])
            r += 1
            continue
        if invs_needed[l] - inv_count < invs_needed[r]:
            temp_people.append(people[l])
            temp_invs_needed.append(invs_needed[l] - inv_count)
            l += 1
            continue
        # if people from left's needed inversion(s) is the same with left's, compare people's height, choose the shorter people
        if people[l][0] < people[r][0]:
            temp_people.append(people[l])
            temp_invs_needed.append(invs_needed[l] - inv_count)
            l += 1
            continue
        inv_count += 1 # still, whenever a people from right is put to the merged list, inv_count increment by one
        temp_people.append(people[r])
        temp_invs_needed.append(invs_needed[r])
        r += 1
    while l < mid:
        temp_people.append(people[l])
        temp_invs_needed.append(invs_needed[l] - inv_count)
        l += 1
    while r < end:
        # here, inv_count += 1 can be omitted since there is no remaining people from left
        temp_people.append(people[r])
        temp_invs_needed.append(invs_needed[r])
        r += 1
    people[start:end] = temp_people
    invs_needed[start:end] = temp_invs_needed




p = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(reconstructQueue(p))