import numpy as np


class ReflectionCalculator:
    def __init__(self, scene):
        self.scene = scene

    def calculate_reflections(self, pulse, tx_position):
        reflections = []
        for obj in self.scene.objects:
            distance = np.linalg.norm(obj.position - tx_position)
            reflected_pulse = pulse * obj.rcs / (distance ** 2)
            reflections.append((distance, reflected_pulse))
        return reflections
