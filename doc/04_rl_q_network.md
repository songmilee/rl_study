[ tag : 강화학습 ]

---

<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>


* cf) Q-learning이 학습되는 걸 시각적으로 보여주는 사이트
    - http://computingkoreanlab.com/app/jAI/jQLearning/

* Q-table의 한계
    - state, action이 많아지면 Q-table이 커지게 되고 계산양이 엄청나게 많아짐
    - 확장성의 제약이 많음
    - 다양한 문제를 해결하기 위해 **Deep Q-Network를 사용**

## Deep Q-Network

- !['Deep Neural Network'](https://poqw.github.io/assets/images/dqn_6.png)

- 전처리
    - Input으로 Atari 게임의 이미지를 사용
        - 원본 자체는 크기가 커서 Image resize, gray scale 등의 처리가 필요
        - 연속된 상태의 이미지를 이용 = **State**

- 모델 최적화
    - State와 Action을 넣어 네트워크를 구성하게 되면 계산 비용이 상당히 커짐
    - 모델을 아래와 같이 변형
    - !['Model change'](https://poqw.github.io/assets/images/dqn_9.png)
    - State로부터 Q-value를 계산하여 Q-value가 최대가 되는 Action을 선택

- CNN
    - !['cnn model'](https://poqw.github.io/assets/images/dqn_10.png)
        - Q를 저장할 용도로 CNN을 활용
        - Input : 전처리 이미지 , Output : Q-value
    - Q Network 상에서의 CNN 구성
        - layer : convoultion 1, convolution 2, convolution 3, fully connected 1, fully connected 2


- Q Optimizer(최적화)
    - RMSProp (Deep Mind 사용)를 사용해 가중치(Θ) 업데이트
- Explotration Rate (탐험률)
    - \\(ε\\) = 기존의 정해진 방향이 아닌 새로운 방향을 랜덤으로 선택할 수 있도록 함
- Loss Function (비용함수)
    - 2개의 CNN을 사용하여 \\(Q^2\\), \\(Q\\)을 저장
        - 네트워크 가중치에 의존하는 문제를 방지하기 위해 사용
        - \\(Q^2\\) : 실제 값을 구하기 위해 사용
        - \\(Q\\) : 기대 값을 구하기 위해 사용
    - Deep Mind 기준 10000 스탭이 지날 때마다 \\(Q^2\\)의 가중치에 \\(Q\\)의 가중치를 덮어 학습을 진행
    - \\(cost = (Target(y) - Expect(y))^2\\)
        - cost를 이용해 \\(Q\\) 업데이트

- Experiance Replay
    - 새로운 경험을 곧바로 학습하지 않고 Experience Replay에 저장
    - 학습시 replay를 이용해 학습
        - Random Sampling한 Mini-batch를 구성해 학습
        - 데이터 순서를 무작위로 하여 데이터 간 상호관계를 없애는 것


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
8. https://poqw.github.io/DQN/