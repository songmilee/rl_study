import gym
env = gym.make("FrozenLake-v0") # 사용할 환경, 본 코드는 FrozenLake-v0 환경을 사용
observation = env.reset() # 초기의 observation 값을 리턴

for _ in range(1000):
    env.render() #출력
    action = env.action_space.sample() #랜덤 action을 선택
    observation, reward, done, info = env.step(action)