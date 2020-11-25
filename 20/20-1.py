from functools import partial, wraps
import inspect
import re
from math import copysign
from collections import Counter
import math


def autoinit(f):
    @wraps(f)
    def auto_constructor(self, *args, **kwargs):
        for index, arg in enumerate(args, 1):
            setattr(self, inspect.getargs(f.__code__).args[index], arg)
        f(self, *args, **kwargs)

    return auto_constructor


class Triple:
    @autoinit
    def __init__(self, x, y, z):
        self.loop = [self.x, self.y, self.z]
        self.counter = -1

    def __str__(self):
        return f"{self.x},{self.y},{self.z}"

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter <= len(self.loop):
            return self.loop[self.counter]
        else:
            self.counter = -1
            raise StopIteration

    def __lt__(self, other):
        return (self.x + self.y + self.z) < (other.x + other.y + other.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z


class Particle:
    @autoinit
    def __init__(self, num, pos, vel, acc):
        pass

    def taxi_distance(self, point):
        return (point.z - self.z) + (point.x - self.x) + (point.y - self.y)

    def __str__(self):
        return f"*|particle no. {self.num}, position - ({self.pos}), velocity - ({self.vel}), acceleration - ({self.acc})|*\n"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.num == other.num

    def __hash__(self):
        return self.num

    def equivalent(self, other):
        return self.pos == other.pos and self.vel == other.vel and self.acc == other.vel

    def collides(self, other):
        return self.pos == other.pos

    # using determinant of quadratic to estimate if collission possible
    def __one_d_collision_chance__(self, other, dim):
        if getattr(self.pos, dim) == getattr(other.pos, dim):
            return True
        a = (getattr(self.acc, dim) - getattr(other.acc, dim))
        b = (getattr(self.vel, dim) - getattr(other.vel, dim))
        c = (getattr(self.pos, dim) - getattr(other.pos, dim))
        if a != 0:
            determinant = (b ** 2) - (4 * a * c)
            if determinant < 0:
                return False
            root1 = ((-b) + math.sqrt(determinant)) / (2 * a)
            root2 = ((-b) - math.sqrt(determinant)) / (2 * a)
            return root1 >= 0 or root2 >= 0
        elif b != 0:
            return -c / b > 0

        return False

    # assumes not already under collision
    def collision_chance(self, other):
        if self.__one_d_collision_chance__(other, 'x') and \
                self.__one_d_collision_chance__(other, 'y') and \
                self.__one_d_collision_chance__(other, 'z'):
            return True
        else:
            return False


def sim(ptcle):
    for dim in ['x', 'y', 'z']:
        setattr(ptcle.vel, dim, getattr(ptcle.vel, dim) + getattr(ptcle.acc, dim))
        setattr(ptcle.pos, dim, getattr(ptcle.pos, dim) + getattr(ptcle.vel, dim))


particles = []
pattern = re.compile(r'^p=<(-?\d+,-?\d+,-?\d+)>, v=<(-?\d+,-?\d+,-?\d+)>, a=<(-?\d+,-?\d+,-?\d+)>$')
with open('input.txt') as file:
    for index, line in enumerate(file):
        position, velocity, acceleration = [Triple(*map(int, x.split(','))) for x in re.match(pattern, line).groups()]
        particles.append(Particle(index, position, velocity, acceleration))

# particles.sort(key=lambda x: abs(x.pos.x) ** 2 + abs(x.pos.y) ** 2 + abs(x.pos.z) ** 2)
# particles.sort(key=lambda x: abs(x.vel.x) ** 2 + abs(x.vel.y) ** 2 + abs(x.vel.z) ** 2)
# particles.sort(key=lambda x: abs(x.acc.x) ** 2 + abs(x.acc.y) ** 2 + abs(x.acc.z) ** 2)
print(len(particles))
while True:
    particles_to_remove = set()
    collision_chance = False
    for i, p in enumerate(particles[:-1]):
        for j, q in enumerate(particles[i + 1:]):
            if p.collides(q):
                collision_chance = True
                particles_to_remove.add(p)
                particles_to_remove.add(q)
            elif collision_chance is True or p.collision_chance(q):
                collision_chance = True
    particles = [p for p in particles if p not in particles_to_remove]
    for p in particles:
        sim(p)
    if collision_chance is False:
        break
    # print(len(particles))

print(len(particles))
# p1 = Particle(1, Triple(2, 0, 0), Triple(1, 0, 0), Triple(1, 0, 0))
# p2 = Particle(2, Triple(-1, 0, 0), Triple(1, -1, 0), Triple(0, 0, 0))
# print(p1.collision_chance(p2))
