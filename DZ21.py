n = [-2, 3, 8, -11, -4, 6]

def count_items(items_list):
    if len(items_list) == 0:
        return 0
    else:
        if items_list[0] < 0:
            return 1 + count_items(items_list[1:])
        else:
            return count_items(items_list[1:])

print("n =", count_items(n))
