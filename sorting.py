from typing import List
class Solution:
    def anagram(self, numbers: List[int], target: int) -> List[int]:
        left, right= 1, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [ left, right]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -=1

def main():
    numbers= [1, 2, 3, 4, 5]
    target= 5
    solution= Solution()
    result = solution.anagram(numbers, target)
    print(result)

if __name__ == '__main__':
    main()