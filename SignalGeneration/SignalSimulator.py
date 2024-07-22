import numpy as np


class SignalSimulator:
    def __init__(self, signal_params):
        self.signal_params = signal_params
    
    def generate_pulse(self, duration):
        t = np.linspace(0, duration, int(self.signal_params.frequency * duration))
        pulse = np.sin(2 * np.pi * self.signal_params.frequency * t) * np.hanning(len(t))
        return t, pulse
