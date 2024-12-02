import sys
import numpy as np

with open(sys.argv[-1]) as f:
    image = np.array([list(row) for row in f.read().strip().split("\n")])

image_histories = np.full([1000] + list(image.shape), " ")
for _ in range(1000000000):
    for col_index, col in enumerate(image.transpose()):
        cubes = np.flatnonzero(col == "#")
        rounds = np.flatnonzero(col == "O")
        # copy of col with Os removed
        image[:, col_index] = np.where(col != "O", col, ".")
        for r in rounds:
            cube_row = np.flatnonzero(col[:r] == "#")[-1] if "#" in col[:r] else -1
            x = cube_row + np.logical_and(rounds > cube_row, rounds < r).sum() + 1
            image[x][col_index] = "O"
    # print(image, "\n")

    for row_index, row in enumerate(image):
        cubes = np.flatnonzero(row == "#")
        rounds = np.flatnonzero(row == "O")
        # copy of row with Os removed
        image[row_index] = np.where(row != "O", row, ".")
        for r in rounds:
            cube_col = np.flatnonzero(row[:r] == "#")[-1] if "#" in row[:r] else -1
            x = cube_col + np.logical_and(rounds > cube_col, rounds < r).sum() + 1
            image[row_index][x] = "O"
    # print(image, "\n")

    image = image[::-1]
    for col_index, col in enumerate(image.transpose()):
        cubes = np.flatnonzero(col == "#")
        rounds = np.flatnonzero(col == "O")
        # copy of col with Os removed
        image[:, col_index] = np.where(col != "O", col, ".")
        for r in rounds:
            cube_row = np.flatnonzero(col[:r] == "#")[-1] if "#" in col[:r] else -1
            x = cube_row + np.logical_and(rounds > cube_row, rounds < r).sum() + 1
            image[x][col_index] = "O"
    image = image[::-1]
    # print(image, "\n")

    image = image[:, ::-1]
    for row_index, row in enumerate(image):
        cubes = np.flatnonzero(row == "#")
        rounds = np.flatnonzero(row == "O")
        # copy of row with Os removed
        image[row_index] = np.where(row != "O", row, ".")
        for r in rounds:
            cube_col = np.flatnonzero(row[:r] == "#")[-1] if "#" in row[:r] else -1
            x = cube_col + np.logical_and(rounds > cube_col, rounds < r).sum() + 1
            image[row_index][x] = "O"
    image = image[:, ::-1]
    # print(image, "\n")

    # each square repeats at different intervals
    # maybe you can record that interval for each square
    # and then take the lcm of all those recorded intervals
    if not _ % 1000: print(_)
    if any((image == h).all() for h in image_histories):
        break
    image_histories = np.roll(image_histories, -1)
    image_histories[-1] = image

ans = 0
for col in image.transpose():
    cubes = np.flatnonzero(col == "#")
    rounds = np.flatnonzero(col == "O")
    for r in rounds:
        cube_row = np.flatnonzero(col[:r] == "#")[-1] if "#" in col[:r] else -1
        x = cube_row + np.logical_and(rounds > cube_row, rounds < r).sum()
        ans += image.shape[1] - x - 1
print(f"{ans=}")
