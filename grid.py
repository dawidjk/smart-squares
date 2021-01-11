from directions import Direction
from block import Block
from typing import List
import random
import pygame
import colors

dir_vals = [(0, 1), (0,-1), (-1,0), (1,0)]

class Grid:
    def __init__(self):
        self.grid_size = 4
        self.blocks: List[List[Block]] = [
            [None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.alive = True
        self.score = 0
        self.add_random()
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, colors.FRAME, (Block.BLOCK_SIZE, Block.BLOCK_SIZE,
                                                self.grid_size * Block.BLOCK_SIZE, 
                                                self.grid_size * Block.BLOCK_SIZE))
        
        empty = Block(0)

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.blocks[i][j]:
                    x = Block.BLOCK_SIZE + Block.BLOCK_SIZE * j + Block.MARGIN
                    y = Block.BLOCK_SIZE + Block.BLOCK_SIZE * i + Block.MARGIN
                    self.blocks[i][j].draw(screen, x, y)

    def move(self, direction: Direction) -> bool:
        if not self.can_move():
            self.alive = False
            return False

        if direction == Direction.UP:
            i = 0
            while i < self.grid_size - 1:
                j = 0
                while j < self.grid_size:
                    for k in range(i + 1, self.grid_size):
                        if self.blocks[k][j]:
                            if self.blocks[i][j]:
                                if self.blocks[i][j].val == self.blocks[k][j].val \
                                        and not self.blocks[k][j].merged \
                                        and not self.blocks[i][j].merged:
                                    self.score += 2 * self.blocks[i][j].val
                                    self.blocks[i][j].merge()
                                    self.blocks[k][j] = None
                                elif i + 1 != k:
                                    self.blocks[i + 1][j] = self.blocks[k][j]
                                    self.blocks[k][j] = None
                            else:
                                self.blocks[i][j] = self.blocks[k][j]
                                self.blocks[k][j] = None
                                i = 0
                                j = self.grid_size
                            break

                    j += 1
                i += 1
        
        elif direction == Direction.DOWN:
            i = self.grid_size - 1
            while i >= 0:
                j = 0
                while j < self.grid_size:
                    for k in range(max(i - 1, 0), -1, -1):
                        if self.blocks[k][j]:
                            if self.blocks[i][j]:
                                if self.blocks[i][j].val == self.blocks[k][j].val \
                                        and not self.blocks[k][j].merged \
                                        and not self.blocks[i][j].merged:
                                    self.score += 2 * self.blocks[i][j].val
                                    self.blocks[i][j].merge()
                                    self.blocks[k][j] = None
                                elif i - 1 != k:
                                    self.blocks[i - 1][j] = self.blocks[k][j]
                                    self.blocks[k][j] = None
                            else:
                                self.blocks[i][j] = self.blocks[k][j]
                                self.blocks[k][j] = None
                                i = self.grid_size - 1
                                j = self.grid_size
                            break

                    j += 1
                i -= 1
        
        elif direction == Direction.LEFT:
            for i in range(self.grid_size):
                for j in range(self.grid_size - 1):
                    for k in range(j + 1, self.grid_size):
                        if self.blocks[i][k]:
                            if self.blocks[i][j]:
                                if self.blocks[i][j].val == self.blocks[k][j].val \
                                        and not self.blocks[i][j].merged \
                                        and not self.blocks[i][k].merged:
                                    self.score += 2 * self.blocks[i][j].val
                                    self.blocks[i][j].merge()
                                    self.blocks[i][k] = None
                                elif j + 1 != k:
                                    self.blocks[i][j + 1] = self.blocks[i][k]
                                    self.blocks[i][k] = None
                            else:
                                self.blocks[i][j] = self.blocks[i][k]
                                self.blocks[i][k] = None
                            break
        
        elif direction == Direction.RIGHT:
            for i in range(self.grid_size):
                for j in range(self.grid_size - 1, 0, -1):
                    for k in range(max(j - 1, 0), -1, -1):
                        if self.blocks[k][j]:
                            if self.blocks[i][j] == self.blocks[k][j] \
                                    and not self.blocks[k][j].merged \
                                    and not self.blocks[i][j].merged:
                                self.score += 2 * self.blocks[i][j]
                                self.blocks[i][k].merge()
                                self.blocks[i][k] = None
                            else:
                                self.blocks[i][k - 1] = self.blocks[i][j]
                                self.blocks[i][j] = None
        self.add_random()
        self.reset_merged()
        return True
    
    def print_board(self) -> None:
        for row in self.blocks:
            for block in row:
                if block:
                    print(block.val, end=" ")
                else:
                    print(".", end=" ")
            print()
        print()

    def add_random(self) -> bool:
        def dfs(i, j):
            if i < 0 or j < 0 or i >= self.grid_size or j >= self.grid_size:
                return False
            
            if not self.blocks[i][j]:
                if random.randint(0, 99) < 95:
                    block = Block(2)
                else:
                    block = Block(4)
                self.blocks[i][j] = block

                return True
            
            indexes = list(range(len(dir_vals)))
            random.shuffle(indexes)

            for index in indexes:
                if dfs(i + dir_vals[index][0], j + dir_vals[index][1]):
                    return True

            return False
        dfs(random.randint(0, 3), random.randint(0, 3))
        self.print_board()
        return True

    def reset_merged(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.blocks[i][j]:
                    self.blocks[i][j].merged = False

    def can_move(self) -> bool:
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if i > 0:
                    if self.blocks[i - 1][j] is None or self.blocks[i - 1][j] == self.blocks[i][j]:
                        return True
                if i < self.grid_size - 1:
                    if self.blocks[i + 1][j] is None or self.blocks[i + 1][j] == self.blocks[i][j]:
                        return True
                if j > 0:
                    if self.blocks[i][j - 1] is None or self.blocks[i][j - 1] == self.blocks[i][j]:
                        return True
                if j < self.grid_size - 1:
                    if self.blocks[i][j + 1] is None or self.blocks[i][j + 1] == self.blocks[i][j]:
                        return True

        return False

    def is_alive(self) -> bool:
        return self.alive
