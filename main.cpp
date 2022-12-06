string findEquation(vector <int> nums, int target) {
    //rec(0, 0, "", target); 3 4 5 2
    for (int mask = 0; mask < (1 << nums.size()) ~ 2^(nums.size()); mask++) { mask = 0, 1, 2, 3, 4 .. 7
        for (int i = 0; i < n; i++) {          mask = 5  = 
                                                           010 > 0
                                                           00 > 0
            if ((1 << i) ~ 2^i & mask > 0) {
                sum += nums[i];     
                str += "+";            0000
            } else {                            1000
                sum -= nums[i];
                str += "-";
            }
        }
        if (sum == target) 
            return str;
        000 - 0
        010 - 0
        001 - 1
         
        010
        011
        100
        111
    }
}

void rec(int position, int sum, string expression, int target) { //2  +, ++, ++-
    if (position == nums.size()) { // 3, 3
        if (sum == target) ans = expression; //2 == 2 ans = ++-
        return;
    }
    rec(position + 1, sum + nums[position], expression + "+", target); // 3, 12, +++, 2
    rec(position + 1, sum - nums[position], expression + "-", target); // 3, 2, ++-,
}
    0 - + - +
          - -
      - - - +
          - -