using System;
using System.Collections;

namespace leetcode
{
    public class Solution
    {
        public static int[] TwoSum(int[] nums, int target)
        {
            Hashtable indices = new Hashtable();
            for (int i = 0; i < nums.Length; i++)
            {
                // check if target - value is in hashtable, if so, return
                if (indices.ContainsKey(target - nums[i]))
                {
                    return new int[] { (int)indices[target - nums[i]], i };
                }
                // if value isn't in hashtable, add it's value and index
                if (!indices.ContainsKey(nums[i]))
                {
                    indices.Add(nums[i], i);
                }
            }
            return new int[] { 0, 0 };
        }

        public static void Main(string[] args)
        {
            Console.WriteLine("{" + String.Join(",", TwoSum(new int[] { 0, 1, 1 }, 2)) + "}");
            Console.WriteLine("{" + String.Join(",", TwoSum(new int[] { 2, 7, 11, 15 }, 9)) + "}");
            Console.WriteLine("{" + String.Join(",", TwoSum(new int[] { 3, 2, 4 }, 6)) + "}");
            Console.WriteLine("{" + String.Join(",", TwoSum(new int[] { 3, 3 }, 6)) + "}");
        }
    }
}