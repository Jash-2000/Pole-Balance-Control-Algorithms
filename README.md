# Beam-balance-using-Boltzman-Policy-Reward-in-Deep-Reinforcement-Learning

## To run the files
  * Clone the repo or download it and extract the files.
  * Import Open AI Gym using the following commmand
  ```cmd
    pip intall gym
  ```
  Gym contains a collection of pre-defined environments, where we can run our algorithms. 
  * It may take up some amount of time while training the network. So it is better to comment out **env.render()** before starting the training. 
  * The final saved video files, weights and other logs would get saved in your working directory.

---

## Other Details

  * Random sampling based mehtod initiates the action space with completely random values. It is clearly observant the the average episode length is no longer than 7.
  * The Naive weight allocation method used a brute force algorithm to get the best weights. The average episode length was found to be around 200.
Developed a simple Deep Q-Learning Network(dqn) based system for balancing a beam imported from OpenAI gym, using a policy based (Boltzmann policy) rewqrding strategy
