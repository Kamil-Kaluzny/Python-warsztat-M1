import random

POSSIBLE_DICES = (
    "D100",
    "D20",
    "D12",
    "D10",
    "D8",
    "D6",
    "D4",
    "D3"
)


def roll_the_dice(dice_code):
    """
    Calculate dice roll from dice pattern.

    :param str dice_code: dice pattern ex. `7D12-5`

    :rtype: int, str
    :return: dice roll value for proper dice pattern, `Wrong Input` text elsewhere
    """
    for dice in POSSIBLE_DICES:
        if dice in dice_code:
            try:
                multiply, modifier = dice_code.split(dice)
            except ValueError:
                return "Wrong Input"
            dice_value = int(dice[1:])
            break
    else:
        return "Wrong Input"

    try:
        multiply = int(multiply) if multiply else 1
    except ValueError:
        return "Wrong Input"

    try:
        modifier = int(modifier) if modifier else 0
    except ValueError:
        return "Wrong Input"

    return sum([random.randint(1, dice_value) for _ in range(multiply)]) + modifier


if __name__ == '__main__':
    print(roll_the_dice("2D10+10"))
    print(roll_the_dice("D6"))
    print(roll_the_dice("2D3"))
    print(roll_the_dice("D12-1"))
    print(roll_the_dice("DD34"))
    print(roll_the_dice("4-3D6"))

    '''
    import random, re

DICE_PATTERN = re.compile(r"^(\d*)D(\d+)([+-]\d+)?$")


POSSIBLE_DICES = (
    "100",
    "20",
    "12",
    "10",
    "8",
    "6",
    "4",
    "3"
)


def roll_the_dice(dice_code):
    """
    Calculate dice roll from dice pattern.

    :param str dice_code: dice pattern ex. `7D12-5`

    :rtype: int, str
    :return: dice roll value for proper dice pattern, `Wrong Input` text elsewhere
    """
    match = DICE_PATTERN.search(dice_code)
    if not match:
        return "Wrong Input"

    multiply, dice, modifier = match.groups()
    if dice not in POSSIBLE_DICES:
        return "Wrong Input"

    multiply = int(multiply) if multiply else 1
    dice = int(dice)
    modifier = int(modifier) if modifier else 0

    return sum([random.randint(1, dice) for _ in range(multiply)]) + modifier


if __name__ == '__main__':
    print(roll_the_dice("2D10+10"))
    print(roll_the_dice("D6"))
    print(roll_the_dice("2D3"))
    print(roll_the_dice("D12-1"))
    print(roll_the_dice("DD34"))
    print(roll_the_dice("4-3D6"))
    '''