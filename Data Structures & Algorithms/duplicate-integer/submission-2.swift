class Solution {
    func hasDuplicate(_ nums: [Int]) -> Bool {
        var nums = nums.sorted()
        guard nums.isEmpty == false, nums.count > 1 else { return false }
        var index = 1
        while (index < nums.count) {
            if nums[index] == nums[index - 1] { return true }
            index += 1
        }
        return false
    }
}
