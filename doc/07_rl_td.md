[ tag : 강화학습 ]

---

## Temporal Difference
- Monte-Carlo + Dynamic Programming
- 경험을 통해 value를 측정
- Episode를 다 끝내지 않더라도 DP 처럼 time step마다 학습할 수 있는 요구에 따라 나온 알고리즘
- 한 스텝 동안 지났던 시간을 토대로 value function을 업데이트
- 매 step마다 학습할 수 있는 것이 장점

### TD(0)
- Temporal Difference learning 방법에서도 가장 간단한 방법
- TD Target
    - 전체 감소된 reward 값
    - R(t+1) + γR(t+2) + ... + γ^(T-1)R(T) =  Rt + 1 + γV(St + 1)
- TD error
    - TD Target와 현재 value function과의 차이

### 알고리즘
- V_π를 측정하기 위한 알고리즘
```
Input : 정책 π를 측정을 위해 사용
임의로 V(s) 초기화

for episode :
    S 초기화

    for each step :
        A = π을 이용해 현 상태 S로부터 선택된 action
        Action A, Reward R, 다음 상태 S'

        V(S) = V(s) + α[R + γ * V(S') - V(S)]
        S = S'
    
    (next state가 Null이 되기 전까지 반복)
    
```

### Bias/Variance Tradeoff
- TD는 bias가 높고 Monte-Carlo는 variance가 높음
- TD는 episode 내 업데이트 시 이전 상태에 영향을 받기 때문에 학습이 한 쪽으로 치우쳐짐


### Reference
1. https://dnddnjs.gitbooks.io/rl/content/td_prediction.html
2. https://ko.wikipedia.org/wiki/%EC%8B%9C%EA%B0%84%EC%B0%A8_%ED%95%99%EC%8A%B5
3. https://sumniya.tistory.com/14
4. https://jay.tech.blog/2016/12/28/temporal-difference-learning/
5. https://wonseokjung.github.io/reinforcementlearning/update/RL-TD1/