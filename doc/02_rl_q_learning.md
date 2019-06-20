[ tag : 강화학습 ]

---

### Q-learning
- Q-value
    - 주어진 State에서 Action을 선택했을 때 얼마나 좋은지 측정하는 값
    - Q-value가 높다면 더 좋은 reward를 받을 수 있다고 간주
    - 강화학습에서 선택은 Action 중 Q-value가 가장 높은 것을 선택하는 것
    - Q-learning은 Q-value를 학습하게 해주는 것

- Q-learning (Dummy)
    - 수식
    <center>Q(s, a) = r(s, a) + argmax_a Q(s', a')</center>

    - s : State, a : Action, r : Reward
    - 초반은 random action을 선택하지만 많은 반복을 통해 optimum policy를 얻을 수 있게 됨
    - 알고리즘
        ```
        1. Q(s,a) 행렬을 랜덤 초기화
        2. 초기 상태 s에서 시작
        3. 아래 과정을 반복적으로 수행
            1) 행동 a를 선택해 실행
            2) 행동에 따른 보상 r과 변경된 상태 s'을 확인
            3) Q 값 갱신
            4) 현재 상태 변경
        ```
    - **단, 해당 방법은 더 최적화된 길이 있어도 보상이 큰 방향으로 움직이게 됨**

- Q-learning + discounted reward
    - 미래 보상에 대해 reward를 줄임으로써 현 상태에서 최적의 보상을 주는 Action을 선택
    - 수식
    <center>Q(s, a) = r(s, a) + γ * argmax_a Q(s', a')</center>

    - s : State, a : Action, r : Reward, **γ : Discount 계수**


### Reference
1. https://hunkim.github.io/ml/RL/rl03.pdf
2. https://bluediary8.tistory.com/18
3. https://www.popit.kr/torch-dqn-%EA%B0%95%ED%99%94%ED%95%99%EC%8A%B5-%EC%86%8C%EA%B0%9C/
4. https://hunkim.github.io/ml/RL/rl04.pdf