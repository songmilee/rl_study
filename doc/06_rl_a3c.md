[ tag : 강화학습 ]

---

### A3C
- Asynchronous Advantage Actor-Critic Agents
- <img src="https://miro.medium.com/max/875/1*YtnGhtSAMnnHSL8PvS7t_w.png" style="width : 500px; height: 450px;">
- Asynchronous
    - 효율적 학습을 위한 다양한 에이전트를 활용
    - 각 다른 agent가 자신의 환경과 상호작용하며 동시에 자신의 환경을 상호작용
        - single agent 보다 잘 작동
        - 더 다양하게 전체적인 경험 학습 가능

- Actor-Critic
    - 가치 함수 V, 정책 π 를 추정
    - 신경망 맨 위에 위치하며 각각이 분리된 fully-connected layer
    - Actor 업데이트를 위해 Critic을 사용

- Advantage
    - Action의 좋고 나쁨을 Agent에게 알리기 위해 경험 집합으로부터 할인된 보상을 이용
        - 해당 신경망은 Action을 높이거나 줄이기 위해 사용
        - Discounted Reward : R = γ(r)
    - 추정된 이득을 사용하는 것은 행동이 얼마나 좋은지 뿐만 아니라 평균보다 얼마나 더 좋은지 알 수 있음
        - Advantage : A = Q(s, a) - V(s)
    - Q-value를 직접 정의가 불가하기 때문에 Advantage Estimate를 만들기 위해 Q(s, a)의 추정치로써 할인 보상 R을 사용 가능
        - Advantage Estimate : A = R - V(s)

### A3C 장점
- 적은 Computation 요구
- 짧은 Training 시간
- 여러 Agent를 동시 학습 가능

### A3C 알고리즘
```
아래의 사항을 반복한다.
    1. Worker는 Global Network를 카피
    2. Worker는 각 환경과 상호작용
    3. value, policy loss 계산
    4. loss로부터 gradient 도출
    5. gradient를 이용해서 Worker가 Global Network 업데이트
```

### Reference
1. https://ishuca.tistory.com/400?category=730862
2. https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-8-asynchronous-actor-critic-agents-a3c-c88f72a5e9f2
3. http://openresearch.ai/t/a3c-asynchronous-methods-for-deep-reinforcement-learning/25
4. https://wonseokjung.github.io/reinforcementlearning/update/RL-a3c/