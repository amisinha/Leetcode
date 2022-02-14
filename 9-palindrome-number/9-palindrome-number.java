class Solution {
    public boolean isPalindrome(int x) {
        int num =x;
        int rev =0;
        if(x < 0){
            return false;
        }
        else{
        while (x !=0){
            int z = x%10;
            rev = rev*10 +z;
            x = x/10;
            
        }
       return (rev == num);
        
        }
    }
    
    
    
}