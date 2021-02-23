# Balancing a pole on a dynamically moving cart.

![Control_System_Representation](https://www.google.com/imgres?imgurl=https%3A%2F%2Fctms.engin.umich.edu%2FCTMS%2FContent%2FInvertedPendulum%2FSystem%2FModeling%2Ffigures%2Fpendulum.png&imgrefurl=https%3A%2F%2Fctms.engin.umich.edu%2FCTMS%2Findex.php%3Fexample%3DInvertedPendulum%26section%3DSystemModeling&tbnid=bRWgqm5FVQr38M&vet=12ahUKEwj18K7yp4DvAhXKPCsKHbT4CHQQMygOegUIARDHAQ..i&docid=kdVY0bMgcIQLoM&w=321&h=307&q=balancing%20pole%20ona%20cart%20control%20system&ved=2ahUKEwj18K7yp4DvAhXKPCsKHbT4CHQQMygOegUIARDHAQ)

The task of balaning a beam on a cart is a classic problem in Control Engineering. The original model deals with a variety of constraints including physical parameters like friction and centre of mass, but for the purpose of simulation, we have to work with certain assumptions. We have assumed that a pole is attached by an un-actuated joint to a cart, which moves along a frictionless track. The system is controlled by applying a force of +1 or -1 to the cart. The pendulum starts upright, and the goal is to prevent it from falling over. A reward of +1 is provided for every timestep that the pole remains upright. The episode ends when the pole is more than 15 degrees from vertical, or the cart moves more than 2.4 units from the center. The state space is represented by four values: cart position, cart velocity, pole angle, and the velocity of the tip of the pole. The action space consists of two actions: moving left or moving right. A reward of +1 is provided for every timestep that the pole remains upright.

In this repository, I have implemented this problem using various **model based** and **model free** algorithms. The simulation environment used in OpenAI Gym which provides the data for **feedback loop**. It also aids in obaining a rendered animation output. 
Diifferent algorithms used can be summarized below.

  * Random sampling based mehtod initiates the action space with completely random values. It is clearly observant the the average episode length is no longer than 7. 
  * The Naive weight allocation method used a brute force algorithm to get the best weights. The average episode length was found to be around 200. This approach iterates through 100 random weigths which decide the update steps and saves the best obtained weights. It is basically a single layer Neural Network without backpropogation, hence **Naive**.

  * Developed a simple Deep Q-Learning Network(dqn) based system for balancing a beam imported from OpenAI gym, using a policy based (Boltzmann policy) rewqrding strategy

---

## To run the files
  * Clone the repo or download it and extract the files.
  * Import Open AI Gym using the following commmand
  ```cmd
    pip intall gym
  ```
  Gym contains a collection of pre-defined environments, where we can run our algorithms. 
  * It may take up some amount of time while training the network. So it is better to comment out **env.render()** before starting the training. 
  * Gym also allows you to save the final rendered output files using its wrapper functions. The final saved video files, weights and other logs would get saved in your working directory. To work with gym wrappers and save the output files in, 
   ```python
    from gym import wrappers
    env = wrappers.Monitor(env, '..\Desktop\RL\MovieFiles', force = True)
   ```
