class SignalProcessingModule:
    def __init__(self):
        pass

    def pulse_compression(self, received_signal, reference_pulse):
        from scipy.signal import correlate
        return correlate(received_signal, reference_pulse, mode='same')
