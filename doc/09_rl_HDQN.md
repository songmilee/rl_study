[ tag : 강화학습 ]

--- 


### 일반적 강화학습의 문제점
- 일반적 강화학습은 매 state마다 reward가 발생함
    - 하지만, 매 state마다 reward를 받지 못하는 경우가 발생
    - !['sparse_reward'](http://10.231.238.12:31111/smlee/rl-tutorial/raw/master/asset/img/hdqn_sparse_reward.png)
        - **sparse reward** : reward가 드물게 발생하는 현상
    - sparse reward가 발생하게 되면 DQN을 통해서 학습이 불가능

## Hierachical Deep Reinforcement Learning (HDQN)
- 여러 목표를 정해 그 목표를 해결해 나가겠다는 컨셉

### Model

!['Model'](http://10.231.238.12:31111/smlee/rl-tutorial/raw/master/asset/img/09_fig_01.PNG)

- Agents
    - 기존의 것은 효율적인 탐색을 위해 Good Control Policy에 대해 학습하는 것을 목표로 함
        - 로컬 탐색을 할 때 E-greedy 등이 유용함
        - Agent가 주 공간 이외의 영역을 탐색을 할 때 추진을 주지는 못함
    - 외부의 reward 축적을 최대화 하기 위해 agent가 setting과 연속된 골 획득에 집중하게 함
    - 각 g(goal)에 대한 정책 π_g를 정의하기 위해 Temporal Abstraction을 사용
    - π_g을 배우기 위해 agent는 critic이 있어야함
        - critic : 내부적 보상(reward)

- Temporal Abstraction
    - 계층적 단계 controller, meta-controller를 사용
    - meta-controller
        - state s_t를 받음
        - 가능한 모든 현재의 goal 중에서 g_t를 선택
    - controller
        - s_t, g_t를 이용해 action a_t를 선택
        - goal g_t는 agent가 몇 스텝 뒤에 보상을 성취하거나 state가 종료되기 전까지 값이 남아 있음
        - critic은 goal에 도달했거나 controller에 적절한 보상(r_t(g))을 제공했는지 평가
    - Objective Function
        - controller
            - 누적된 Intrinsic Reward을 극대화하기 위함
                - !['Instrisic reward'](http://10.231.238.12:31111/smlee/rl-tutorial/raw/master/asset/img/09_instrinic_reward.PNG)
        - meta-controller
            - 누적된 Extrinsic Reward을 극대화하기 위함
                - !['Extrinsic Reward'](http://10.231.238.12:31111/smlee/rl-tutorial/raw/master/asset/img/09_extrinic_reward.PNG)
                - f_t : 환경으로부터 받는 reward signal

- **Deep Reinforcement Learning with Temporal Abstraction**
    - controller, meta-controller가 policy를 배우기 위해서 Deep Q-Learning 프레임워크를 사용
    - controller Q-value function
        - !['controller estimate q value'](http://10.231.238.12:31111/smlee/rl-tutorial/raw/master/asset/img/09_controller_q_value.PNG)
        - g : state s 일 때 agent의 goal
        - π_ag = P(a|s, g) : action 정책
    - meta-controller Q-value function
        - !['meta controller estimate q value'](http://10.231.238.12:31111/smlee/rl-tutorial/raw/master/asset/img/09_meta_controller_q_value.PNG)
        - N : controller가 주어진 현재 goal에 대해 멈추기 직전 까지의 타임 스텝 수
        - g' : state s_t+N에 대한 agent의 goal
        - π_g = P(g|s) : goals에 대한 정책

    - Q2에 의해 생성된 변화값 (s_t, g_t, f_t, s_t+N)은 Q1에 의해 생성된 (s_t, a_t, g_t, r_t, s_t+1)보다 느린 시간 규모를 가짐(slower time-scale)
    - Q1, Q2는 loss function L1(Θ1), L2(Θ2)를 최소화하며 학습을 시킴
    - Q2 (s_t, g_t, f_t, s_t+N), Q1 (s_t, a_t, g_t, r_t, s_t+1)에 대해 개별적으로 D1, D2라는 Disjoint memory space를 저장함

- Learning Algorithm
    - parameter
        - stochastic gradient descent의 Time scale을 다르게 하여 parameter 설정
    - g : goal
        - e-greedy에 의해 값이 맞춰짐
    - controller
        - 매 타임 스텝 마다 탐색 확률 ε_1,g를 이용한 goal을 통해 action이 결정됨
        - 모델의 매개변수 Θ1, Θ2는 replay memory D1, D2를 기반으로 점진적으로 각각 업데이트 됨

### 알고리즘 : h-DQN
```
    1. replay memory {D1, D2}, 매개변수 {Θ1, Θ2}를 각각 초기화 (controller, meta-controller)
    2. 모든 goal에 대한 controller의 탐색 확률 ε_1,g =1로 초기화
    3. meta-controller의 탐색 확률 ε_2 = 1로 초기화

    for i in range(1, episode):
        게임 초기화
        s = 게임 시작 값

        g = EPSGREEDY(s, G, ε_2, Q_2)

        while s가 종료 상태가 아닐 때까지 :
            F = 0
            s0 = s

            while !(s가 종료 상태가 아니거나 goal g에 도달했을 때):
                a = EPSGREEDY({s, g}, A, ε_1,g, Q_2)

                a 실행
                다음 상태 s', 환경으로부터 외부 reward f 받음
                internal critic으로 부터 내부 reward r(s, a, s') 받음
                D1에 변화된 값 ({s, g}, a, r, {s', g}) 저장
                매개변수 업데이트 (L1(Θ1, i), D1)
                매개변수 업데이트 (L2(Θ2, i), D2)

                F = F + f
                s = s'
            
            D2에 (s0, g, F, s') 저장

            if s != 끝나는 상태:
                g = EPSGREEDY(s, G, ε_2, Q_2)
        

```

### 알고리즘 : EPSGREEDY(x, B, ε, Q)
'''
if random() < ε:
    return B에서 랜덤 요소 선택
else:
    return argmax_m Q(x, m) (m은 B에 포함되는 원소)
'''



### Reference
1. https://bluediary8.tistory.com/4
2. https://arxiv.org/pdf/1604.06057.pdf