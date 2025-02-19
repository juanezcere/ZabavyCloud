"""
Data generation utils.
"""
from .datetime_utils import fromtimestamp
from .random_utils import randbool, randint, random, uniform


def generate_random(state: bool = True, minimum: float = 0.1, maximum: float = 0.5) -> float:
    return uniform(-minimum, maximum) if state else uniform(-maximum, minimum)


def generate_battery(numbers: list, timestamps: list, is_connected: bool = True, min_value: float = 3.2, max_value: float = 4.2, min_step: float = 0.1, max_step: float = 0.1):
    state: bool = is_connected
    for ts in timestamps[1:]:
        rand: float = generate_random(state, min_step, max_step)
        number: float = numbers[0] + rand
        numbers.append(round(number, 2))


def generate_temperature(numbers: list, timestamps: list, min_value: float = 17.3, max_value: float = 26.1, min_step: float = 0.1, max_step: float = 0.5):
    state: bool = randbool()
    for ts in timestamps[1:]:
        rand: float = generate_random(state, min_step, max_step)
        number: float = numbers[-1] + rand
        numbers.append(round(number, 2))
        timestamp = fromtimestamp(ts)
        if number >= max_value:
            state = False
        if timestamp.hour > 19 or timestamp.hour < 6:
            state = False
        if number <= min_value:
            state = True
        if random() > 0.8:
            state = not state


def generate_humidity(numbers: list, timestamps: list, min_value: float = 71.0, max_value: float = 83.0, min_step: float = 0.7, max_step: float = 1.1):
    state: bool = randint(0, 2) == 1
    for ts in timestamps[1:]:
        rand: float = generate_random(state, min_step, max_step)
        rand = rand/2 if state else rand
        number: float = numbers[-1] + rand
        numbers.append(int(number))
        if number >= max_value:
            state = False
        if number <= min_value:
            state = True


def generate_cold(numbers: list, timestamps: list, min_value: float = 2.1, max_value: float = 3.1, min_step: float = 0.1, max_step: float = 0.5):
    state: bool = randint(0, 2) == 1
    for ts in timestamps[1:]:
        rand: float = generate_random(state, min_step, max_step)
        number: float = numbers[-1] + rand
        numbers.append(round(number, 2))
        if number >= max_value:
            state = False
        if number <= min_value:
            state = True


def generate_freezer(numbers: list, timestamps: list, min_value: float = -19.7, max_value: float = -17.1, min_step: float = 0.1, max_step: float = 0.5):
    state: bool = randint(0, 2) == 1
    for ts in timestamps[1:]:
        rand: float = generate_random(state, min_step, max_step)
        number: float = numbers[-1] + rand
        numbers.append(round(number, 2))
        if number >= max_value:
            state = False
        if number <= min_value:
            state = True


def generate_ultrafreezer(numbers: list, timestamps: list, min_value: float = -81.1, max_value: float = -77.9, min_step: float = 0.1, max_step: float = 0.5):
    state: bool = randint(0, 2) == 1
    for ts in timestamps[1:]:
        rand: float = generate_random(state, min_step, max_step)
        number: float = numbers[-1] + rand
        numbers.append(round(number, 2))
        if number >= max_value:
            state = False
        if number <= min_value:
            state = True


def generate_data(values: dict, start_date: int, end_date: int) -> None:
    """
    Generate data.
    """
    print('Generating data.')
    values['timestamp'] = [ts+randint(-10, 10)
                           for ts in range(start_date, end_date, 100)]
    if 'battery' in values:
        generate_battery(numbers=values['battery'],
                         timestamps=values['timestamp'])
    if 'temperature' in values:
        generate_temperature(
            numbers=values['temperature'], timestamps=values['timestamp'])
    if 'humidity' in values:
        generate_humidity(
            numbers=values['humidity'], timestamps=values['timestamp'])
    if 'cold' in values:
        generate_cold(numbers=values['cold'], timestamps=values['timestamp'])
    if 'freezer' in values:
        generate_freezer(numbers=values['freezer'],
                         timestamps=values['timestamp'])
    if 'ultrafreezer' in values:
        generate_ultrafreezer(
            numbers=values['ultrafreezer'], timestamps=values['timestamp'])
    print('Data generated.')
