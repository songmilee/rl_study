[ tag : 강화학습 ]

---

### Deterministic & Stochastic

<img src="http://10.231.238.12:31111/smlee/rl-tutorial/raw/master/asset/img/deterministic.png" style="width:100%; height:250px;" alt="deterministic model">
<center>[그림 1] Deterministic Model - Agent가 주어진 명령에 따라 움직일 수 있는 환경  </center>

- Deterministic Model
    - 모델의 출력 값이 초기의 상태 값과 매개변수 값을 통해 결정됨

<img src="http://10.231.238.12:31111/smlee/rl-tutorial/raw/master/asset/img/stochastic.png" style="width:100%; height:270px;" alt="stochastic model">
<center>[그림 2] Stochastic Model - Agent가 주어진 명령에 따라 움직일 수도 있고 움직이지 못할 수도 있는 환경</center>

- Stochastic Model
    - 랜덤한 값을 가지고 있음
    - 같은 매개변수, 초기 상태라도 모델은 다른 결과를 도출해낼 수 있음
    - code 상에서 deterministic/stochastic을 결정하는 변수
        - is_slippery
            - False : Deterministic
            - True : Stochastic
    - Stochastic World에서 기존의 Q-learning을 사용하게 되면 성공율이 확연히 떨어짐
        - Q-table은 움직일 것이라 예상하고 reward를 반환하나 실제로 움직이지 않음
        - Action대로 움직일 수도 있기 때문에 완전히 Q-table 무시 불가
    - **해결책 : Q-table을 이용하되 다음 State의 Reward를 적게 반영하는 것**
    - 수식
        <center>Q(s, a) = (1 - α) * Q(s, a) + α * (r(s, a) + (γ * argmax_a Q(s', a')))</center>
        - α = learning rate


### Reference
1. https://hunkim.github.io/ml/RL/rl05.pdf
2. http://www.modulabs.co.kr/RL4RWS/18834