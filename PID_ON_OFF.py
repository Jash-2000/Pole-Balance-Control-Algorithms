import numpy as np
import gym
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

env = gym.make('CartPole-v1')
desired_state = np.array([0, 0, 0, 0])
desired_mask = np.array([0, 0, 1, 0])

P, I, D = 0.1, 0.01, 0.5

for i_episode in range(20):
    ans = input("Show the next episode ??")
    state = env.reset()
    integral = 0
    derivative = 0
    prev_error = 0
	err = []
    time = []

    for t in range(500):
        env.render()
        error = state - desired_state

        integral += error
        derivative = error - prev_error
        prev_error = error

        pid = np.dot(P * error + I * integral + D * derivative, desired_mask)
        action = sigmoid(pid)
        action = np.round(action).astype(np.int32)
        err.append(error[2])
        time.append(t)
        
        state, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
	plt.plot(time,err)
    plt.ylabel('Error Log')
    plt.show()
    del err
    del time
	
env.close()

