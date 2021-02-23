import gym
import numpy as np

env = gym.make('CartPole-v0')

done = False
cnt = 0

observation = env.reset()

while not done:
	env.render()
	#time.sleep(10)
	cnt +=1

	action = env.action_space.sample()
	observation,reward,done,_ = env.step(action)
	if done:
		break
print("Game laste for ", cnt)