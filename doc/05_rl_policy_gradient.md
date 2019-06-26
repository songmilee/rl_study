[ tag : 강화학습 ]
---
### Reinforcement Learning의 학습 방식
1. Value 기반 방식
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
#### 장점
- Value 기반의 방식에 비해 수렴이 더 잘됨
- Value 기반의 방식은 하나의 최적화된 Action으로 수렴하나, Policy Gradient는 Stochastic Policy를 배울 수 있음
- Action이 여러개이거나 고차원에서의 Action 자체가 연속적일 경우 효과적 (로봇 Control에 적합)

#### 단점
- Local Optimum에 빠질 수 있음
- Policy Evaluate 과정이 비효율적
- 분산이 높음

### Policy Objective Function
- Policy를 근사한 매개변수를 업데이트 해 나가기 위해 사용하는 함수
- 정의하는 방법
    1. State value
    2. Average value (잘 사용 안 함)
    3. Average reward per time-step 
        - 각 시간 마다 받는 reward를 근사하는데 사용
- Objective Function을 최대화 시키는 Policy Parameter Vector를 찾아내는 방법 => **Gradient Descent**

### Objective Function의 Gradient를 구하는 방법
1. Finite Difference Policy Gradient
    - 수치적인 방법. 가장 간단하게 구할 수 있음
    - Parameter Space가 작을 때는 간단하나, 클 수록 비효율적이고 노이지한 방법
    - Policy가 미분이 불가능해도 작동한다는 장점이 있음
    - 최근에는 잘 사용하지 않는 방법

2. Monte-Carlo Policy Gradient
    - Policy가 미분 가능하다 가정
    - Episode 마다 Gradient를 업데이트
    - Score Function : Policy에 log를 취한 형태

3. Actor-Critic Policy Gradient
    - Monte-Carlo에서 발생하는 분산 문제를 해결
    - Q(s, a)를 직접적으로 만들지 않고 함수로 근사해 Q-function을 만들고 policy는 학습된 Q-function을 기반으로 학습
    - Critic : Q-function을 근사하는 것
    - Actor : Policy를 근사


### Reference
1. https://hatter30.github.io/blog/describe-policy-gradient/
2. https://dnddnjs.gitbooks.io/rl/content/numerical_methods.html
3. http://www.modulabs.co.kr/RL_library/3305