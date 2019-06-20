[ tag : 강화학습 ]

---

### 강화 학습이란?

!['reinforcement learning'](http://web.stanford.edu/class/cs234/images/RL.png)

- 주체(Agent)가 상황(Situation)에 대해 **보상(Reward)을 최대화** 할 수 있는 행동(Action)에 대해 학습하는 것
- 다수의 반복과 시행착오를 통해 더 나은 방향으로 학습한다는 것이 사람의 학습 방식과 유사

### 학습 방법
- 탐험(Exploration) & 이용(Exploitation)
    - 주어진 상황에서 높은 보상을 위해 적절한 행동(exploit)을 선택해야 함
    - Action의 가치를 알기 위해 사전 탐험(explore)가 필요
    - exploation-explitation dilemma
        - 탐험을 위해 당장 최선의 선택인 action을 포기할 필요가 있음

### 강화 학습의 구성요소
- Policy
    - State에 대해 Action을 결정하는 역할
    - 일반적으로 Stochastic인 경우가 많음
- Reward Signal
    - Agent가 Action을 할 때 마다 환경이 Agent에게 돌려주는 값
    - Reward Signal은 State와 Action에 대한 Stochastic Function
- Value Function
    - 어떤 State를 시작으로 Agent가 얻을 것이라 예측되는 Reward의 총합
    - 선택에 있어 value 값이 높은 것이 우선적으로 고려 대상
- Model
    - 환경의 행동을 모방하는 것
    - State, Action이 주어졌을 때 Model은 결과로 Reward와 다음 state를 반환

### Reference
1. https://hunkim.github.io/ml/RL/rl01.pdf
2. https://www.slideshare.net/CurtPark1/dqn-reinforcement-learning-from-basics-to-dqn
3. https://m.blog.naver.com/linegamedev/221117991251
4. http://web.stanford.edu/class/cs234/index.html