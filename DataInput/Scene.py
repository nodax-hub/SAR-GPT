import numpy as np


class SceneObject:
    def __init__(self, position, rcs):
        self.position = np.array(position)  # Позиция объекта в 3D-пространстве (x, y, z)
        self.rcs = rcs  # Эффективная поверхность рассеяния (m^2)


class Scene:
    def __init__(self):
        self.objects = []
    
    def add_object(self, scene_object):
        self.objects.append(scene_object)
