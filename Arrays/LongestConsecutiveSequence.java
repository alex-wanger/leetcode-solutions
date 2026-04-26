import java.util.HashMap;

public class LongestConsecutiveSequence {

    public static void main(String[] args) {
        HashMap<Integer, Integer> hashmap = new HashMap<>();
        int[] nums = new int[100];
        for (int i = 0; i < nums.length; i++) {
            if (!hashmap.containsKey(nums[i])) {
                hashmap.put(nums[i], 1);
            } else {
                int currentValue = hashmap.get(nums[i]);
                hashmap.put(nums[i], currentValue + 1);
            }
        }

    }
}
