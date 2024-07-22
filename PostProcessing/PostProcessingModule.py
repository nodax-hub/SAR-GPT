import matplotlib.pyplot as plt


class PostProcessingModule:
    def __init__(self):
        pass
    
    def noise_reduction(self, signal):
        from scipy.signal import wiener
        return wiener(signal)
    
    def visualize(self, signal, title="Signal"):
        plt.figure(figsize=(10, 4))
        plt.plot(signal)
        plt.title(title)
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.grid()
        plt.show()
