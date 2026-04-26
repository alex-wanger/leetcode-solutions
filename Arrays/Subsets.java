import java.util.ArrayList;
import java.util.List;

public class Subsets {
    public List<List<Integer>> subsets(int[] nums) {
        return null;
    }

    public void helper(int[] nums, int index, List<Integer> current, List<List<Integer>> sum) {

        if (index == nums.length) {
            sum.add(new ArrayList<>(current));
            return;
        }

        helper(nums, index + 1, current, sum);

        current.add(nums[index]);
        helper(nums, index + 1, current, sum);
        current.remove(current.size() - 1);

        // helper nums, 0, 0, 0
        // n, 1, 1, 1, 1
        // n, 2, 1+2, (1, 1,2)
        // n, 3, 1+2+3, (1, 1,2, 1,2,3)
        // n,

    }

}
