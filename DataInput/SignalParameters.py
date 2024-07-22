import numpy as np

class SignalParameters:
    def __init__(self, frequency, power, pulse_width):
        self.frequency = frequency  # Частота сигнала (Hz)
        self.power = power          # Мощность передатчика (W)
        self.pulse_width = pulse_width  # Ширина импульса (s)
        self.wavelength = 3e8 / frequency  # Длина волны (m)
