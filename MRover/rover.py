from .position import Position


class Rover(object):

    AVAILABLE_COMMANDS = {
        'M': 'mover',
        'L': 'virar_esquerda',
        'R': 'virar_direita',
    }

    DIRECTIONS = {
        'N': 1,
        'E': 2,
        'S': 3,
        'W': 4,
    }

    heading = DIRECTIONS['N']

    def __init__(self, plateau, position, heading):
        """
        Initializing mars rover with below params
        :param plateau:
        :param position:
        :param heading:
        """
        self.plateau = plateau
        self.position = position
        self.heading = heading

    def __str__(self):
        return self.current_position

    def set_position(self, x, y, heading):
        if not isinstance(self.position, Position):
            self.position = Position(x, y)
        else:
            self.position.x = x
            self.position.y = y

        self.heading = heading

    @property
    def current_position(self):
        return '{} {} {}'.format(self.position.x, self.position.y, self.get_heading)

    @property
    def get_heading(self):
        directions = list(self.DIRECTIONS.keys())

        try:
            direction = directions[self.heading - 1]
        except IndexError:
            direction = 'N'
            print('Erro, direção inválida..')

        return direction

    def process(self, commands):
        for i in range(len(commands)):
            self.comando_andar(commands[i])

    def comando_andar(self, command):
        if 'L' == command:
            self.virar_esquerda()
        elif 'R' == command:
            self.virar_direita()
        elif 'M' == command:
            if not self.mover():
                print("Não dá pra ir praí amigo")
        else:
            print("Acho que você digitou algo errado")

    def mover(self):
        if not self.plateau.move_available(self.position):
            return False
        if self.DIRECTIONS['N'] == self.heading:
            self.position.y += 1
        elif self.DIRECTIONS['E'] == self.heading:
            self.position.x += 1
        elif self.DIRECTIONS['S'] == self.heading:
            self.position.y -= 1
        elif self.DIRECTIONS['W'] == self.heading:
            self.position.x -= 1

        return True

    def virar_esquerda(self):
        self.heading = self.DIRECTIONS['W'] if (self.heading - 1) < self.DIRECTIONS['N'] else self.heading - 1

    def virar_direita(self):
        self.heading = self.DIRECTIONS['N'] if (self.heading + 1) > self.DIRECTIONS['W'] else self.heading + 1