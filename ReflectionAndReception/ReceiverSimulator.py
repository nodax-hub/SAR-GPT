import numpy as np


class ReceiverSimulator:
    def __init__(self, antenna_params):
        self.antenna_params = antenna_params
    
    def receive(self, reflections):
        received_signal = np.zeros_like(reflections[0][1])
        for distance, reflection in reflections:
            received_signal += reflection
        return received_signal
