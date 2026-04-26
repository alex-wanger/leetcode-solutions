from typing import List

def groupAnagrams(strs: List[str]):
    map_of_index_arrays = []
    for element in strs:
        index_array = [0] * 26 
        element = element.lower()
        for char in element:
            ascii_value = ord(char) % ord('a')
            index_array[ascii_value] += 1
        map_of_index_arrays.append(index_array)
    
    solution = dict()
    map_of_index_arrays = tuple(map_of_index_arrays)
    print(type(map_of_index_arrays))
    for index, map_of_indexesin in enumerate(map_of_index_arrays):
        map_of_indexesin = tuple(map_of_indexesin)
        if (map_of_indexesin in solution):
            solution[map_of_indexesin].append(strs[index])
        else:
            solution[map_of_indexesin] = [strs[index]]
    return list(solution.values())
        

groupAnagrams(["act","pots","tops","cat","stop","hat"])