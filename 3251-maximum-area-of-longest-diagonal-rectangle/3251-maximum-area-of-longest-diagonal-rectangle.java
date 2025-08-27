class Solution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        double a = Math.sqrt(dimensions[0][0]*dimensions[0][0] +        dimensions[0][1]*dimensions[0][1]);
        int area = dimensions[0][0] * dimensions[0][1];
        for(int i=1;i<dimensions.length;i++){
            double b = Math.sqrt(dimensions[i][0]*dimensions[i][0] + dimensions[i][1]*dimensions[i][1]);
            if(b>a){
                a=b;
                area = dimensions[i][0] * dimensions[i][1];
            }
            else if(b==a){
                area = Math.max(area,dimensions[i][0] * dimensions[i][1]);
            }
        }
        return area;
    }
}