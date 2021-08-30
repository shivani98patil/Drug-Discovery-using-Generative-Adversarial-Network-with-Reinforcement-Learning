# Drug-Discovery-using-Generative-Adversarial-Network-with-Reinforcement-Learning

**Introduction-**
1. Drug development timelines are long and they depend upon numerous factors
2. Drug Development needs about 15-16 years and billions of dollars to launch the drug in the market. 
3. Overall failure rate is 96% and 90% of the drugs fail in first clinical trail itself. Hence it is important to come with a better and reliable approach to solve this problem
4. The problem can be solved by using sophisticated Deep Learning algorithms to ensure the drug discovery is faster and also overcomes the problem of failure in trails
5. Deep Learning approach improves discovery and decision making using abundant and high-quality data

**Survey-**
When surveyed about Artificial Intelligence used in Health Care Industry. Some of the approaches taken by the researchers were
	1. Vibrational auto encoders
	2. Adversarial auto encoders
	3. RNN with Reinforcement learning
	4. Generative Adversarial Network
In the above research paper referred, models used images as their input. 
Also, the finding showed that GAN model have different problems like
	A. Generator and Discriminator are given image data as input.
	B. When generator generates incomplete samples which are given directly to the discriminator.

Programming Language - Python
Modules - Tensorflow and Rdkit
Data - ZINC*

**Code Explanation- **
Pre- training process:
Step 1. Initially we are pre- training our generator. For first iteration after 10 epoch test new data is generated and after that for 40 epoch test new data is generated.
Step 2. Generator generates fake data based on pe-trained generator. After which that data is loaded into discriminator for training.
Step 3. Then we pre- train discriminator. It is trained for 3 epochs on generated data for 50 iterations .
Reinforcement Learning Process:
Step 1.  We train generator once and discriminator 2 times. After which we balance the generator and discriminator. 
Step 2. After generator is trained once, we calculate the reward and update the generator parameters and rollout policy.
Step 3. Then we train discriminator by loading fake data in it for 2 epochs.
Step 4. After every 1 iteration of reinforcement learning process we test the model once.



