class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
      int cnt = 1;
      vector<vector<int>>maxi(nums.size()+1);
      vector<int>aa;
      sort(nums.begin(),nums.end());
      for(int i=0;i<nums.size();i++){
        if(nums[i]==nums[i+1]){
            cnt++;
        }
        else{
            maxi[cnt].push_back(nums[i]);
            cnt = 1;
        }
      }
      int n = maxi.size();
      for(int i=n-1; i>=1; i--){
       for (int num : maxi[i]) {
                aa.push_back(num);
                if (aa.size() == k) return aa; 
            }
      }
      return aa;
    }
};