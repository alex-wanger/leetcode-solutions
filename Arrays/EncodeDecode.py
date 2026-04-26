from typing import List


delimintator = chr(31)

def encode(strs: List[str]) -> str:
    total = ""
    for element in strs:
        total += (element + delimintator)
    return total
    
def decode(s: str) -> List[str]:
    list_of_all_elements = []
    last_deliminator_index = 0;
    for i in range(len(s)):
        if (s[i] == delimintator):
            list_of_all_elements.append(
                s[last_deliminator_index:i])
            last_deliminator_index = i + 1;
    return list_of_all_elements

print(type(["Hello", "World"]))
decode(encode(strs=["Hello", "World"]))
