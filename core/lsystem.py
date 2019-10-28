class LSystem:
    def __init__(self, definition):
        self.definition = definition
        self.name, angles, self.axiom, *theorems = definition.strip().split('\n')
        self.angles = int(angles)
        self.theorems = dict(map(lambda s: s.split(), theorems))
        self.evolution = 0
        self.lstring = ''

    def angle(self):
        return 360 / self.angles

    def start(self):
        self.evolution = 1
        self.lstring = self.axiom

    def evolve(self):
        new_string = []
        for ch in self.lstring:
            new_string.append(self.theorems.get(ch, ch))
        self.lstring = ''.join(new_string)
        self.evolution += 1

    def evolve_to(self, steps):
        for _ in range(steps):
            self.evolve()

    def reset(self):
        self.start()
