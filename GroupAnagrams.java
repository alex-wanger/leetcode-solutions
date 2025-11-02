import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> hashmap = new HashMap<>();
        for (int i = 0; i < strs.length; i++) {
            char[] sortedChars = strs[i].toCharArray();
            Arrays.sort(sortedChars);
            String sortedStrings = new String(sortedChars);
            if (hashmap.containsKey(sortedStrings)) {
                hashmap.get(sortedStrings).add(strs[i]);
            } else {
                ArrayList<String> arrayList = new ArrayList<>();
                arrayList.add(strs[i]);
                hashmap.put(sortedStrings, arrayList);
            }
        }
        List<List<String>> answer = new ArrayList<>(hashmap.values());
        return answer;
    }

}
