from MRover import Plateau
from MRover import Position
from MRover import Rover

def main():
    plateau = Plateau(5, 5)
    position = Position(1, 2)
    
    rover = Rover(plateau, position, Rover.DIRECTIONS.get('N'))
    rover.process("LMLMLMLMM")
    print(rover)

    rover.set_position(3, 3, Rover.DIRECTIONS.get('E'))
    rover.process("MMRMMRMRRM")
    print(rover)


if __name__ == "__main__":
    main()