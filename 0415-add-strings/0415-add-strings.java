import java.math.BigInteger;
class Solution {
    public String addStrings(String num1, String num2) {
       BigInteger ans1 = new BigInteger(num1); 
       BigInteger ans2 = new BigInteger(num2);
        return ans2.add(ans1).toString();
    }
}