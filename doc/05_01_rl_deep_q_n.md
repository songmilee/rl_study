[ tag : 강화학습 ]

---

### Double DQN
**DQN의 문제점 : DQN은 각 state의 잠재적 Action에 대해 Q를 과대평가하는 경향이 있음** => Agent가 이상적인 정책을 학습하는데 어려움이 있음
- Target Q-value 계산시 Neural Network가 행동을 선택하게 함
- Target Neural Network는 Action에 대한 Target Q-value 생성하는 것을 사용
- Action에 대한 과대평가 감소 및 빠른 학습 가능
- <b>수식</b>
<center>Q-Target = r + γ * Q(s', argmax(Q(s', a, Θ)), Θ')</center>

### Dueling DQN
<img src="https://t1.daumcdn.net/cfile/tistory/212DCA39589EE96A1A" style="width:500px; height:450px;">

[그림] (상) 일반적인 DQN (하) Value 함수과 Advantage 함수를 나눠서 계산하는 Dueling DQN

- Q(s, a) = V(s) + A(a)
    - 일반적으로 Q-value를 Value 함수와 Advantage 함수의 결합이라 생각할 수 있음
- Advantage 함수와 Value 함수를 분리해서 계산 후 최종 레이어에서 하나의 Q함수에 넣음
- Agent가 학습 시 동시에 Advantage와 Value에 대해 고려할 필요가 없어짐
    - 더욱 강건한 추정치를 얻을 수 있음


### Double Dueling DQN


### Reference 
1. https://parkgeonyeong.github.io/Double-DQN%EC%9D%98-%EC%9D%B4%EB%A1%A0%EC%A0%81-%EC%9B%90%EB%A6%AC/
2. https://ishuca.tistory.com/396