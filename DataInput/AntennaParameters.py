class AntennaParameters:
    def __init__(self, gain_tx, gain_rx, beamwidth):
        self.gain_tx = gain_tx  # Усиление антенны передатчика (dBi)
        self.gain_rx = gain_rx  # Усиление антенны приемника (dBi)
        self.beamwidth = beamwidth  # Ширина диаграммы направленности (deg)
