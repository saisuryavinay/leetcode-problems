class Solution {
    public boolean checkPerfectNumber(int num) {
        int sum=0;
        for(int i=1;i<num;i++){
            if(num%i==0){
                sum+=i;
                //System.out.println(sum);
            }
        }
        if(sum==num){
            return true;
        }
        return false;
    }
}