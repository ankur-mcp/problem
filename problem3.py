def combine_lists(list1, list2):
    combined = sorted(list1 + list2, key=lambda x: x['positions'][0])
    result = []
    for item in combined:
        if not result:
            result.append(item)
            continue
        prev = result[-1]
        l1, r1 = prev['positions']
        l2, r2 = item['positions']
        overlap = min(r1, r2) - max(l1, l2)
        if overlap > 0 and overlap >= (r2 - l2) / 2:
            prev['values'].extend(item['values'])
        else:
            result.append(item)
    return result

# Example usage
list1 = [{"positions": [0, 5], "values": [1, 2]}]
list2 = [{"positions": [3, 7], "values": [3, 4]}]
print(combine_lists(list1, list2))
