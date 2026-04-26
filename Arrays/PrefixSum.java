import java.util.Arrays;

public class PrefixSum {
    public static void main(String[] args) {
        int[] initalArray = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        int[] prefixSum = new int[10];
        prefixSum[0] = initalArray[0];

        for (int i = 1; i < initalArray.length; i++) {
            prefixSum[i] = initalArray[i] + prefixSum[i - 1];
        }

        System.out.println(Arrays.toString(initalArray));
        System.out.println(Arrays.toString(prefixSum));
    }
}
