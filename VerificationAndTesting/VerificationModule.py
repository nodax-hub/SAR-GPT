import numpy as np


class VerificationModule:
    def __init__(self):
        pass
    
    def compare_with_real_data(self, simulated_data, real_data):
        error = np.mean((simulated_data - real_data) ** 2)
        return error
