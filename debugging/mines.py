#!/usr/bin/env python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = mines
        self.board = [['.' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.place_mines()

    def place_mines(self):
        placed = 0
        while placed < self.mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.board[y][x] != 'X':
                self.board[y][x] = 'X'
                placed += 1

    def print_board(self):
        clear_screen()
        print("   " + " ".join([str(i) for i in range(self.width)]))
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if self.revealed[y][x]:
                    row += self.board[y][x] + " "
                else:
                    row += ". "
            print(f"{y:2} {row}")

    def count_adjacent_mines(self, x, y):
        count = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if self.board[ny][nx] == 'X':
                        count += 1
        return count

    def reveal(self, x, y):
        if self.revealed[y][x]:
            return True

        self.revealed[y][x] = True

        if self.board[y][x] == 'X':
            return False

        adj = self.count_adjacent_mines(x, y)
        if adj > 0:
            self.board[y][x] = str(adj)
            return True

        self.board[y][x] = '0'

        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                nx = x + dx
                ny = y + dy
                if (
                    0 <= nx < self.width
                    and 0 <= ny < self.height
                    and not self.revealed[ny][nx]
                ):
                    self.reveal(nx, ny)

        return True

    def has_won(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] != 'X' and not self.revealed[y][x]:
                    return False
        return True

    def play(self):
        while True:
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if x < 0 or x >= self.width or y < 0 or y >= self.height:
                    print("Invalid coordinate. Please try again.")
                    continue

                safe = self.reveal(x, y)
                self.print_board()

                if not safe:
                    print("Game Over! You hit a mine.")
                    break

                if self.has_won():
                    print("Congratulations! you won the game.")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()

