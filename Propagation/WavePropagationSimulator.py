import numpy as np


class WavePropagationSimulator:
    def __init__(self, signal_params):
        self.signal_params = signal_params
    
    def propagate(self, pulse, distance):
        # Учет затухания на расстоянии
        attenuation = np.exp(-distance / (2 * self.signal_params.wavelength))
        return pulse * attenuation
