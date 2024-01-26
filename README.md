## 백준 알고리즘 By Python
- 단계별로 풀어보기 ing...
---
- 입출력 빠르게 하는 방법
```
# 빠른 입력
import sys
input = sys.stdin.readline

# 더 빠른 입력
import os, io, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

# 빠른 출력
import sys
print = sys.stdout.write
```
* set = 중복되지 않은 값 저장
* enumerate = 인덱스와 값을 동시에 반환
* print(*list) = 언패킹하여 출력
