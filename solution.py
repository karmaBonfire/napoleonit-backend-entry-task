class Solution:
    digits = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        total = 0

        for i in range(len(s)):
            value = self.digits[s[i]]  # значение текущего символа

            # если справа есть символ и его значение больше текущего, то вычитаем значение текущего
            if i + 1 < len(s) and value < self.digits[s[i + 1]]:
                total -= value
            else:
                total += value
        
        return total

if __name__ == "__main__":
    print(Solution().romanToInt(input()))
