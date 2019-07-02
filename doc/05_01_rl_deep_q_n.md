[ tag : 강화학습 ]

---

### Double DQN
**DQN의 문제점 : DQN은 각 state의 잠재적 Action에 대해 Q를 과대평가하는 경향이 있음**

=> 최적화 되지 않은 액션으로 학습을 하게 되면 Agent가 이상적인 정책을 학습하는데 어려움이 있음

- **Action 선택과 Target Q 생성을 분리**
- Target Q 계산시 Neural Network가 행동을 선택하게 함
- Target Neural Network는 Action에 대한 Target Q-value 생성하는 것을 사용
- Action에 대한 과대평가 감소 및 빠른 학습 가능
- 기존 DQN 수식

<center>Q(s, a) = r(s, a) + γ * argmax_a Q(s', a')</center>

- <b>Double DQN 수식</b>

<center>Q-Target = r + γ * Q(s', argmax(Q(s', a, Θ)), Θ')</center>


cf) Double DQN을 이용한 로봇 시뮬레이션
- http://blog.naver.com/PostView.nhn?blogId=einsbon&logNo=221312079887&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView&userTopListOpen=true&userTopListCount=10&userTopListManageOpen=false&userTopListCurrentPage=1


### Dueling DQN
<img src="https://t1.daumcdn.net/cfile/tistory/212DCA39589EE96A1A" style="width:500px; height:450px;">

[그림] (상) 일반적인 DQN (하) Value 함수과 Advantage 함수를 나눠서 계산하는 Dueling DQN

- Q(s, a) = V(s) + A(a)
    - 일반적으로 Q-value를 Value 함수와 Advantage 함수의 결합이라 생각할 수 있음
    - V(s) : state가 얼마나 좋은지를 수치화한 것
    - A(a) : action 취하는 것이 얼마나 좋은지 수치화 한 것
- Advantage 함수와 Value 함수를 분리해서 계산 후 최종 레이어에서 하나의 Q함수에 넣음
- Agent가 학습 시 동시에 Advantage와 Value에 대해 고려할 필요가 없어짐
    - 더욱 강건한 추정치를 얻을 수 있음

### 부분 관찰성
- MDP : 주어진 state에서 최적의 action을 취하는데 필요한 모든 정보를 제공하는 환경
    - 실제 환경은 MDP를 따르지 않음
- **부분 관찰 마르코프 결정과정(POMDP)** : Agent에게 제한된 방식으로 정보를 제공하는 환경을 의미
    - 주어진 정보는 공간적 제약 및 시간적 제약이 있음

### DRQN(Deep Recurrent Q-Network)
- 부분 관찰성을 풀기 위해서는 Neural Network Agent는 state에 대해 시간적 통합 능력이 필요
    - RNN은 시간적 의존관계를 학습하는 능력이 있음
- Recurrent 블럭을 이용함으로써 환경에서 1개의 프레임을 agent로 보낼 수 있게 됨
    - Neural Net은 시간적 패턴에 의존해 출력을 변경할 수 있음
    - 각 시간 단계마다 Hidden State를 계산하고 유지하기 때문에 가능
- Recurrent 블럭이 Hidden State를 피드함으로써 네트워크를 Augmentation 역할을 하게 함
- !['DRQN 접근법'](https://t1.daumcdn.net/cfile/tistory/2259213758A06BDC18)

[그림] Deep Mind에서 DRQN 접근법

- !['DRQN Architecture'](https://jaydottechdotblog.files.wordpress.com/2017/02/drqn-architecture.png?w=411&h=459)

[그림] DQRN 모델 아키텍쳐
- 일반 DQN과 다르게 마지막단이 LSTM 레이어



### Reference 
1. https://parkgeonyeong.github.io/Double-DQN%EC%9D%98-%EC%9D%B4%EB%A1%A0%EC%A0%81-%EC%9B%90%EB%A6%AC/
2. https://ishuca.tistory.com/396
3. https://www.slideshare.net/ssuserbd7730/pyconkr-2018-rladventureto-the-rainbow
4. https://www.slideshare.net/ShinwooPark3/rl-from-scratch-part5
5. https://ishuca.tistory.com/398
6. https://jay.tech.blog/2017/02/06/deep-recurrent-q-learning/