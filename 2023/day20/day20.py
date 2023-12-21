from enum import Enum
import math
from pathlib import Path
import queue
import regex

p = Path(__file__).with_name("input.txt")
lines = open(p).read().splitlines()

modules = {}
for line in lines:
    line_components = line.split(" -> ")
    if line_components[0][0] == 'b':
        modules[line_components[0]] = ('b', line_components[1].split(", "))
    else:
        modules[line_components[0][1:]] = (
            line_components[0][0], line_components[1].split(", "))


class FlipFlop(Enum):
    ON = 0
    OFF = 1


class Beam(Enum):
    LOW = 0
    HIGH = 1


def calculate_initial_state():
    initial_state = {
    }

    for (module_name, module_props) in modules.items():
        if module_props[0] == '%':
            initial_state[module_name] = FlipFlop.OFF
        elif module_props[0] == '&':
            inbound_modules = {}
            for (other_module_name, other_module_props) in modules.items():
                if module_name in other_module_props[1]:
                    inbound_modules[other_module_name] = Beam.LOW
            initial_state[module_name] = inbound_modules

    return initial_state


ITERATIONS = 1000


def cycle(state, sent):
    q = queue.Queue()

    q.put(('button', 'broadcaster', Beam.LOW))

    while not q.empty():
        (origin, module_name, beam) = q.get()
        sent[beam] += 1

        if module_name not in modules:
            if module_name == 'rx' and beam == Beam.LOW:
                print(iter, module_name)
            q.task_done()
            continue

        # print(module_name)

        (module_type, module_targets) = modules[module_name]
        beam_to_send = None

        if module_type == '%':
            if beam == Beam.LOW:
                was_off = state[module_name] == FlipFlop.OFF
                state[module_name] = FlipFlop.ON if was_off else FlipFlop.OFF
                beam_to_send = Beam.HIGH if was_off else Beam.LOW
            # else:
            #     print("IGNORED")
        elif module_type == '&':
            state[module_name][origin] = beam
            has_low_in_memory = list(
                state[module_name].values()).count(Beam.LOW) > 0
            beam_to_send = Beam.HIGH if has_low_in_memory else Beam.LOW
        else:
            beam_to_send = Beam.LOW

        if beam_to_send is not None:
            for target in module_targets:
                q.put((module_name, target, beam_to_send))

        q.task_done()


def part1():
    ITERATIONS = 1000
    state = calculate_initial_state()
    sent = {Beam.LOW: 0, Beam.HIGH: 0}

    for iter in range(ITERATIONS):
        cycle(state, sent)

    return sent[Beam.LOW] * sent[Beam.HIGH]


print("Part 1", part1())


# # rx receives from lv
# # lv is &, so all inputs must be high inputs
# # lv receives from st, tn, hh, dt
# # all inputs are & so at least one of their input must be low input

# def part2():
#     # nodes = ["st", "tn", "hh", "dt"]
#     nodes = ["gr", "vc", "db", "lz"]
#     cycles = []
#     for node in nodes:
#         state = calculate_initial_state()
#         iter = 0
#         while True:
#             iter += 1
#             if iter % 1000 == 0:
#                 print(iter)
#             cycle(state, {Beam.LOW: 0, Beam.HIGH: 0})

#             if list(state[node].values()).count(Beam.HIGH) == 0:
#                 break

#         cycles.append(iter)
#         print(iter)

#     return math.lcm(*cycles)


# print(part2())
