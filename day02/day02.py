# part 1
with open("input.txt") as f:
    gamesum = 0
    for line in f:
        countgame = True
        game, cubes = line.split(":")
        _, game = game.split()
        for sample in cubes.split(";"):
            for cube in sample.split(","):
                count, color = cube.split()
                count = int(count)
                if "red" in color and count > 12:
                    countgame = False
                if "blue" in color and count > 14:
                    countgame = False
                if "green" in color and count > 13:
                    countgame = False
        if countgame:
            gamesum += int(game)
        
print(gamesum)


# part 2
with open("input.txt") as f:
    gamesum = 0
    for line in f:
        countgame = True
        game, cubes = line.split(":")
        _, game = game.split()
        rmax, gmax, bmax = 1, 1, 1
        for sample in cubes.split(";"):
            for cube in sample.split(","):
                count, color = cube.split()
                count = int(count)
                if "red" in color and count > rmax:
                    rmax = count
                if "blue" in color and count > bmax:
                    bmax = count
                if "green" in color and count > gmax:
                    gmax = count
        
        gamesum += (rmax * bmax * gmax)
        
print(gamesum)
