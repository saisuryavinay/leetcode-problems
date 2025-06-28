class Solution {
    public int singleNumber(int[] nums) {
        int n = nums.length;
       int asn = 0;
       for(int i=0;i<n;i++){
         asn ^=nums[i];
       }
       return asn;
    }
}