# 최대값이 나오게 하려면 3 * 3 * 3 * .... 3 * 2 혹은 3* 3 * 3 * ..... *4 중 하나여야 한다.

# 이것을 증명하기 위해서는 2가지가 필요하다.
# 1.	숫자 N을 몇 등분할지
# 2.	N등분 된 숫자를 각각 몇으로 할 지
# 우선 2번의 경우 모든 숫자를 동일하게 하는 것이 좋다. 즉 N을 2등분 한다고 가정하면 (N/2) * (N/2)가 최대값이고 3등분한다고 가정하면 (N/3) * (N/3) * (N/3)이 최대값이다.
# 1번의 경우 N/e등분 하는 것이 제일 좋다. 증명은 다음그림을 참조하자.
# https://user-images.githubusercontent.com/12128784/110127984-9edcad80-7e09-11eb-8c63-bc727290b59a.png
# 따라서 우리는 N/e등분을 해야 하고 N을 N/e등분 하면 e다. 
# 그러므로 N = e+e+e+…로 나누었을 때가 가장 좋다. 
# 단 본 문제는 정수여야 하므로 e를 반올림한 값인 3이 나와야 하고 마지막은 4혹은 2로 끝나는 것이 좋다. 


class Solution:
    def integerBreak(self, n: int) -> int:
        if n > 3:
            return 3**(n//3 -1) * max(3 * (n%3), (3+n%3))
        else:
            return n-1
