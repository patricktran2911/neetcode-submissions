class Solution {
    func hasDuplicate(_ nums: [Int]) -> Bool {
        var nums = nums.sorted()
        guard nums.isEmpty == false, nums.count > 1 else { return false }
        var left = 0
        var right = left + 1
        repeat {
            if nums[left] == nums[right] { return true }
            left += 1
            right += 1
        } while right < nums.count
        return false
    }
}
