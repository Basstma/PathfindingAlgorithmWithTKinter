from config import *
import pygame as pg
from maze import Maze


class Display:
    def __init__(self, maze: Maze, scale:int=10):
        self.maze = maze

        self.scale = scale
        self.window_size = (self.maze.size[0] * scale, self.maze.size[1] * scale)

        self.running = True

        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(self.window_size)
        self.FPS = 60

    def run(self):
        while self.running:
            pg.display.flip()
            self.display()
            self.clock.tick(self.FPS)

    def display(self):
        def draw_rectangle(pos: list, color: str):
            pg.draw.rect(self.screen, colors[color],
                         (pos[0] * self.scale, (pos[1] * self.scale), self.scale, self.scale))

        for i in range(0, self.maze.size[0]):
            for j in range(0, self.maze.size[1]):
                if self.maze.maze[j][i] == 1:
                    draw_rectangle((i, j), color="white")
                elif self.maze.maze[j][i] == 2:
                    draw_rectangle((i, j), color="blue")


if __name__ == '__main__':
    maze = Maze(size=(1000, 1000))
    d = Display(maze, scale=1)