[ tag : 강화학습]

---

* cf) Q-learning이 학습되는 걸 시각적으로 보여주는 사이트
    - http://computingkoreanlab.com/app/jAI/jQLearning/

* Q-table의 한계
    - state, action이 많아지면 Q-table이 커지게 되고 계산양이 엄청나게 많아짐
    - 확장성의 제약이 많음
    - 다양한 문제를 해결하기 위해 **Q-Network를 사용**

### Q-Network
!['Q-network_1'](https://t1.daumcdn.net/cfile/tistory/99B0E7375B4845E917)
!['Q-network_2'](https://t1.daumcdn.net/cfile/tistory/99C6FC4F5B48466020)
- Input (x) : state, Ouput (y) : 해당 state에서 각 action을 취할 때 reward 값 (Q-value)
- 본 네트워크를 통해 Optimal한 Q-value를 알아내는 것이 목표
- 현재의 Weight와 Bias 값을 토대로 Q 값을 업데이트에 사용

### Deep Q-Network
- DQN?
    - Convolution Networks를 이용해 learning 하는 방법을 의미
    - 아타리 게임의 raw pixel을 인풋으로 하여 value function을 출력으로 내고 있음


- DQN 모델 아키텍쳐
!['DQN Architecture'](https://t1.daumcdn.net/cfile/tistory/99FE4F485B98F7C432)
    - CNN을 이용한 구조를 갖음
        - 고차원 데이터를 쉽게 표현할 수 있음
    - CNN과 달리 pooling layer 단계가 없음
        - pooling 하게 되면 데이터를 잃게 되기 때문에 데이터가 중요한 DQN에서 pooling 단계가 없음

- DQN 알고리즘
```
1. replay 메모리 생성
2. 신경망 매개변수를 랜덤으로 초기화
3. 초기 상태 s에서 시작
4. 다음의 과정을 반복
    1) 일정 확률 이상인 경우 액션을 랜덤 선택
    2) 이하일 경우 높은 Q 값을 가지는 액션 선택
5. 액션에 따른 reward와 변경된 state 확인
6. 경험(s, a, r, s')을 replay 메모리에 저장
7. replay memory에서 experience replay 기법에 따라 전이들의 mini-batch를 랜덤 선택
8. mini-batch의 각 전이에 대해 목표 Q 값 계산
    1) 변경 상태가 종료 상태, 전이의 보상을 목표 Q 값으로 할당
    2) 변경 상태가 종료가 아닐 경우, Bellman Equation을 따라 목표 Q값을 할당
9. squared error를 신경망의 손실함수로 사용해 Q-network를 학습
10. 학습 상태 변경
```

- DQN 이슈
    - 샘플 데이터가 다양하지 않고 서로 연관성이 있음
    - Target이 변화함

- DQN 솔루션
    1. Go Deep        
        - 네트워크를 깊게 구성
    2. Capture and Replay
        - Action의 state 값을 buffer에 저장 후 사용
        - buffer에서 랜덤하게 가져오면 샘플 데이터간 연관성을 해결 가능
    3. Seperate Networks
        - 타겟에 대한 네트워크를 따로 분리해 구성





### Reference
1. https://hunkim.github.io/ml/RL/rl06.pdf
2. http://www.modulabs.co.kr/RL4RWS/18868
3. https://mobicon.tistory.com/539
4. https://www.nextobe.com/single-post/2017/05/17/Deep-Q-Network-DQN
5. https://hunkim.github.io/ml/RL/rl07.pdf
6. https://sumniya.tistory.com/18
7. https://www.popit.kr/torch-dqn-%EA%B0%95%ED%99%94%ED%95%99%EC%8A%B5-%EC%86%8C%EA%B0%9C/