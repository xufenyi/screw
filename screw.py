import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Direction:
    CLOCKWISE = 1
    ANTICLOCKWISE = -1


class Region:
    UP = 1
    DOWN = -1


class HalfCircle:
    def __init__(self, start: float, r: float, direction: int, region: int):
        self.start, self.r, self.direction, self.region = start, r, direction, region
        self.c = self.start + self.r * self.direction * self.region
        self.end = 2 * self.c - self.start

    def get_points(self, step: float) -> np.array:
        if step > self.r:
            raise ValueError('Step is too large.')
        step_angle = step / self.r
        step_count = int(np.floor(np.pi * self.r / step))
        result = np.zeros((step_count+1, 2))
        angle = 0
        for i in range(step_count+1):
            result[i, 0] = self.c + self.r * np.cos(angle)
            result[i, 1] = self.r * np.sin(angle) * self.region
            angle += step_angle
        return result if self.direction*self.region == -1 else np.flipud(result)


def create_screw(margin=0.06, x_world=0, y_world=0, save_filename='output.csv'):
    half_circle_list = [
        HalfCircle(
            start=0, r = margin/2, direction=Direction.ANTICLOCKWISE, region=Region.UP
        )
    ]
    # Forward
    for i in range(9):
        last = half_circle_list[-1]
        half_circle_list.append(HalfCircle(
            start=last.end, r = last.r+margin/2, direction=last.direction, region=-last.region
        ))


    all_points = np.vstack(
        [half_circle.get_points(0.25*margin) for half_circle in half_circle_list]
    )
    all_points[:, 0] += x_world
    all_points[:, 1] += y_world

    unique = []
    for i in range(len(all_points) - 1):
        if not np.array_equal(all_points[i], all_points[i + 1]):
            unique.append(all_points[i])
    unique.append(all_points[-1])
    all_points = np.array(unique)

    # pd.DataFrame(
    #     np.round(all_points, decimals=6)
    # ).to_csv(save_filename, index=False, header=False)

    plt.plot(all_points[:, 0], all_points[:, 1])
    plt.show()


create_screw(x_world=30.0, y_world=28.0, save_filename='c1.csv')
# create_screw(x_world=39.9, y_world=23.9, save_filename='c2.csv')
# create_screw(x_world=44.0, y_world=14.0, save_filename='c3.csv')
# create_screw(x_world=39.9, y_world=04.1, save_filename='c4.csv')
# create_screw(x_world=30.0, y_world=00.0, save_filename='c5.csv')
# create_screw(x_world=20.1, y_world=04.1, save_filename='c6.csv')
# create_screw(x_world=16.0, y_world=14.0, save_filename='c7.csv')
# create_screw(x_world=20.1, y_world=23.9, save_filename='c8.csv')
