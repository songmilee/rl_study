[ tag : 강화학습 ]

---

### Reinforcement Learning의 학습 방식
1. Value 기반 방식
    - !['value based rl'](../asset/img/value_based_rl.png)
    - Q-value 값이 가장 클 것이라 예상되는 Action을 선택하는 방식
2. Policy 기반 방식
    - Value 학습이 아닌 Policy를 학습 시키는 것
    - Policy 자체를 변수화 하는 것 (cf. evolutionary 알고리즘)

### Value Gradient 단점
1. Unstable
- Value Function을 기반으로 Policy를 계산함 -> **Value Function이 달라지면 Policy가 변경됨**
- Policy가 크게 변화하는 건 알고리즘 수렴에 불안정성을 추가

2. Stochastic Policy
- 가위, 바위, 보의 경우 각 1/3 씩 사용하는게 Optimal Policy
- Value 기반의 RL은 하나의 최적화된 Action을 선택해야만 함

### Policy Gradeint 장단점
<center>
<img src="../asset/img/policy_math.png">

[그림 ] Policy의 수식
</center>

#### 장점
- Value 기반의 방식에 비해 수렴이 더 잘됨
- Value 기반의 방식은 하나의 최적화된 Action으로 수렴하나, Policy Gradient는 Stochastic Policy를 배울 수 있음
- Action이 여러개이거나 고차원에서의 Action 자체가 연속적일 경우 효과적 (로봇 Control에 적합)

#### 단점
- Local Optimum에 빠질 수 있음
- Policy Evaluate 과정이 비효율적
- 분산이 높음

### Policy Objective Function

<center>
<img src="../asset/img/policy_objective_math.png">

[그림 ] Policy Objective Function의 수식
</center>

- Policy를 근사한 매개변수를 업데이트 해 나가기 위해 사용하는 함수
- 정의하는 방법
    1. State value
    2. Average value (잘 사용 안 함)
    3. Average reward per time-step 
        - 각 시간 마다 받는 reward를 근사하는데 사용
- Objective Function을 최대화 시키는 Policy Parameter Vector를 찾아내는 방법 => **Gradient Descent**

### 필요한 사전 지식
- Score Function : Policy에 log를 취한 형태
    - !['score function'](../asset/img/score_function.png)
    - 정책이 0이 아닌 값을 갖고 있어도 미분이된다고 가정
    - 우도함수비율에(Likelihood Ratio) 따라 score function을 도출
- Policy Gradient Theorem
    - !['policy gradient theorem'](../asset/img/policy_gradient_theorem.png)
    - Multi-step MDP에 대해 우도비율 접근법(Likelihood ratio approach)를 일반화한 것
    - 순간 발생하는 reward r을 long-term value Q^π(s,a)로 치환
    - 시작 상태, 평균 reward, 평균 값의 objective function에 적용됨
- Stochastic Policy
    - Stochastic Policy를 표현하기 위해 Sigmoid 함수와 Softmax 함수를 활용
    - Sigmoid Function
        - !['Sigmoid Function'](https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Logistic-curve.svg/480px-Logistic-curve.svg.png)
        - 확률을 나타내기 좋은 함수
        - output : [0, 1]
    - Softmax Function
        - Action(Discrete Action Space 내라 가정)이 3개 이상이 되면 Sigmoid를 사용하기 어려움
        - Action이 1 ~ n이 있을 때 Action 확률을 표현할 수 있음
        - Action 확률의 총합은 1임

### Objective Function의 Gradient를 구하는 방법
1. Finite Difference Policy Gradient
    - 수치적인 방법. 가장 간단하게 구할 수 있음
    - Parameter Space가 작을 때는 간단하나, 클 수록 비효율적이고 노이지한 방법
    - Policy가 미분이 불가능해도 작동한다는 장점이 있음
    - 최근에는 잘 사용하지 않는 방법

2. Monte-Carlo Policy Gradient
    - 모든 State에 대해 Action value 함수를 알기 어려움
        - Approximation을 통해 policy 업데이트가 필요 => 기준이 필요
        - 기준으로 Action value 함수를 사용해야 하나 값을 알기 어려움
    - Episode에서 있던 reward를 기억하고 Episode가 끝난 다음 각 state에 대한 reward를 반환
    - 인자를 Stochastic Gradient Descent 방식으로 업데이트
    - Policy Gradient Theorem을 사용
    - Q^π(s, a)의 편향되지 않은 샘플을 V_t로 반환
    - 알고리즘
        ```
        function Reinforcement:
            Θ 초기화
            for (s, a) in episode:
                for t in (1, t-1):
                    Θ = Θ + α*∇_Θlog π_Θ(s_t, a_t) * v_t

            return Θ
        ```


3. Actor-Critic Policy Gradient
    - Monte-Carlo에서 발생하는 분산 문제를 해결
    - Q(s, a)를 직접적으로 만들지 않고 함수로 근사해 Q-function을 만들고 policy는 학습된 Q-function을 기반으로 학습
    - Critic : Q-function을 근사하는 것
    - Actor : Policy를 근사
    - 알고리즘
        ```
        function QAC:
            s, Θ 초기화
            π 샘플링

            for i in episdoe:
                reward r을 샘플링
                state 변화 s' 샘플링
                action a' 샘플링

                δ = r + γ*Q_w(s', a') - Q_w(s, a)
                Θ = Θ + α*∇_Θlog π_Θ(s, a) * Q_w(s, a)
                w = w + βδφ(s, a)
                a = a'
                s = s'
        ```

### Baseline
- Variance 문제를 해결하기 위해 사용
- State value function을 일종의 평균으로 사용
- 현재의 행동이 평균적으로 얻을 수 있는 value보다 얼마나 더 좋은지를 계산해 variance를 줄여감 => **Advantage 함수라 명명*
- 지금보다 좋으면 해당 방향으로, 반대면 반대 방향으로 업데이트



### Reference
1. https://hatter30.github.io/blog/describe-policy-gradient/
2. https://dnddnjs.gitbooks.io/rl/content/numerical_methods.html
3. http://www.modulabs.co.kr/RL_library/3305
4. https://en.wikipedia.org/wiki/Sigmoid_function
5. https://en.wikipedia.org/wiki/Softmax_function
6. https://www.slideshare.net/WoongwonLee/rlcode-a3c
