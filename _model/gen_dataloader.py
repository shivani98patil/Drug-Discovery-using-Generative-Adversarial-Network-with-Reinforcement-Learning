import numpy as np





class Gen_Data_loader():

    def __init__(self, batch_size):

        self.batch_size = batch_size
        """ batch size is basically the number of training smaples per iteration.
        which is selected by estimation as in it should not be too large or too low."""



    def create_batches(self, samples):
        """ these lines of code help creating batches"""

        self.num_batch = int(len(samples) / self.batch_size)# here we calculate number of batches

        samples = samples[:self.num_batch * self.batch_size]# here put samples in list form 

        self.sequence_batch = np.split(np.array(samples), self.num_batch, 0) # here we distribute the samplesin their batch sizes

        self.pointer = 0
        



    def next_batch(self):

        ret = self.sequence_batch[self.pointer] # by the pointer value we will know which batch is suppose to go next

        self.pointer = (self.pointer + 1) % self.num_batch # we are taking remaining samples from total samples

        return ret



    def reset_pointer(self):

        self.pointer = 0