import gym
import numpy as np
from gym import wrappers

env = gym.make('CartPole-v0')

bestLength = 0
episode_lengths = []

best_weights = np.zeros(4)

for i in range(100):
	new_weights = np.random.uniform(-1,1,4)

	length = []
	for j in range(100):
		observation = env.reset()
		done = False
		cnt = 0

		while not done:
			cnt +=1
			action = 1 if np.dot(observation, new_weights) > 0 else 0

			observation, reward, done, stats = env.step(action)

			if done:
				break
		length.append(cnt)
	average_length = float(sum(length)/len(length))

	if average_length > bestLength:
		bestLength = average_length
		best_weigths = new_weights
	episode_lengths.append(average_length)
	if i % 10 == 0:
		print('Best length is ', bestLength)

done = False
cnt = 0
env = wrappers.Monitor(env, 'MovieFiles2', force = True)
observation = env.reset()

while not done:
	cnt += 1 

	action = 1 if np.dot(observation, best_weights) > 0 else 0
	observation, reward, done, _ = env.step(action)

	if done:
		break

print("With the best weights, the game lasted for : ", cnt, " moves")


