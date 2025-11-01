import java.util.Arrays;
import java.util.HashMap;

class ValidAnagram {
    // public boolean isAnagram(String s, String t) {
    // if (s.length() != t.length()) {
    // return false;
    // }
    // char[] sortedS = s.toCharArray();
    // char[] sortedT = t.toCharArray();
    // Arrays.sort(sortedS);
    // Arrays.sort(sortedT);
    //
    // for (int i = 0; i < s.length(); i++) {
    // if (sortedS[i] != sortedT[i]) {
    // return false;
    // }
    // }
    // return true;
    // }
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> hashmap = new HashMap<>();
        HashMap<Character, Integer> hashmapt = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (hashmap.containsKey(s.charAt(i))) {
                hashmap.put(s.charAt(i), hashmap.get(s.charAt(i)) + 1);
            } else {
                hashmap.put(s.charAt(i), 0);
            }
        }
        for (int i = 0; i < t.length(); i++) {
            if (hashmapt.containsKey(t.charAt(i))) {
                hashmapt.put(t.charAt(i), hashmapt.get(t.charAt(i)) + 1);
            } else {
                hashmapt.put(t.charAt(i), 0);
            }
        }
        return hashmap.equals(hashmapt);
    }
    // turns out this double hashmap solution is even worse than sorting!
}
