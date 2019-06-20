import gym
import numpy as np
import matplotlib.pyplot as plt
from gym.envs.registration import register
import random as pr

def rargmax(vector):
    m = np.amax(vector)
    indices = np.nonzero(vector == m)[0]
    return pr.choice(indices)

#FrozenLake 4x4 map을 만듦
register(
    id='FrozenLake-v3',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name':'4x4',
            'is_slippery':False
    }
)

env = gym.make('FrozenLake-v3')

Q = np.zeros([env.observation_space.n, env.action_space.n]) #테이블 초기화
num_episodes = 2000

rList = [] # episode 마다 보상을 리스트화
for i in range(num_episodes):
    state = env.reset()
    rAll = 0
    done = False

    #Q-learning Algorithm
    while not done:
        action = rargmax(Q[state, :])
        new_state, reward, done, _ = env.step(action)
        Q[state, action] = reward + np.max(Q[new_state, :])

        rAll += reward
        state = new_state
    
    rList.append(rAll)

print("Success rate : " + str(sum(rList)/num_episodes))
print("Final Q-table Values")
print("Left Down Right Up")
print(Q)

plt.bar(range(len(rList)), rList, color="blue")
plt.show()
