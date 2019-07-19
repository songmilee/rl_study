[ tag : 강화학습 ]

---

## Monte-Carlo
- 경험을 통해 value를 측정
- Transition/Reward에 대한 정보를 모르는 상태에서 시작
- Episode가 완료되어 최종적으로 받게 되는 Reward를 통해 평균적으로 학습
- Episode 종료 후 받는 Reward의 평균값을 value로 사용

### State evaluate 방법
1. First Visit MC
    - 하나의 state를 여러 번 방문 시 첫번째 방문했을 때 value를 사용
    - 각 에피소드에 대한 평균으로 value를 추정
    - 에피소드가 무한으로 진행하면 최적화된 value와 같아지게 됨 => policy 업데이트 시 최적의 정책을 찾을 수 있음

```
 - s : 측정하기 위한 상태
 - t : 상태 s가 Episode 상에서 방문하는 첫번째 스텝
 - N(s) : 증가 카운터 ex) N(s) = N(s) + 1
 - G_t : Discount된 Reward의 전체 값
 - S(s) : 전체 증가 값 ex) S(s) = S(s) + G_t
 - 평균에 의해서 값이 측정됨 ex) V(s) = S(s) / N(s)
 - 큰 수로 값을 보내게 되면 V(s) -> v_π(s)가 됨
```

2. Every Visit MC
    - 하나의 state를 2번 이상 지나갔을 때, 모든 value를 사용해 평균내어 추정하는 방식

=> 일반적으로 First Visit MC 많이 사용

### Incremental Mean
- 하나씩 더해가며 평균을 계산하는 방법
- 수식
    - !['mc equation'](http://10.231.238.12:31111/smlee/rl-tutorial/raw/master/asset/img/mc_equation.PNG)
    - First Visit MC에 적용
        - !['first visit monte carlo'](http://10.231.238.12:31111/smlee/rl-tutorial/raw/master/asset/img/inc_mean_after_fmc.PNG)
        - N(s)를 무한대로 보내 놓은 값을 α로 고정
        - 맨 처음 정보들에 대해 가중치를 덜 주는 형태
        - episode 마다 새로운 policy를 사용하기 때문에 업데이트 상수를 일정하게 고정


### Reference
1. https://daeson.tistory.com/327
2. https://dnddnjs.gitbooks.io/rl/content/mc_prediction.html

