import turtle
import math
import fractions
from dataclasses import dataclass
from typing import Tuple, Any, overload
from typing_extensions import assert_never, cast
import colorsys
import random
import time


class SpirographWheel:
    def __init__(self, M: int, N: int, R_OUTER: int):
        self.M = M
        self.N = N
        self.R_OUTER = R_OUTER

        gcd = math.gcd(self.M, self.N)
        self.M //= gcd
        self.N //= gcd
        self.R_INNER = self.R_OUTER * self.N / self.M
        self.SCALE = 200
        self.go_to_next(0)

    def go_to_next(self, t: float) -> None:
        theta = math.tau * t
        RATIO = self.N / self.M
        self.x = self.SCALE * (1 - RATIO) * math.cos(self.N * theta)
        self.y = self.SCALE * (1 - RATIO) * math.sin(self.N * theta)
        # print(self)

    def __repr__(self) -> str:
        return f"SpirographWheel({vars(self)})"


class CoolerTurtle(turtle.Turtle):
    def __init__(self, hue_steps: int | float, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True):
        self.hue_steps = hue_steps
        super().__init__(shape, undobuffersize, visible)

    @overload
    def goto(self, x: tuple[float, float], y: None = ...) -> None:
        ...

    @overload
    def goto(self, x: float, y: float) -> None:
        ...

    def goto(self, x: float | tuple[float, float], y: float | None = None) -> None:
        # Change color:
        turtle.colormode(255)
        cur_color, _ = self.color()
        hls_color = colorsys.rgb_to_hls(*cur_color)
        hls_color = (hls_color[0] + 1/self.hue_steps,
                     hls_color[1], hls_color[2])
        next_color = tuple(map(int, colorsys.hls_to_rgb(*hls_color)))
        next_color_cast = cast(
            tuple[float, float, float], next_color)  # mypy thing

        self.color(next_color_cast)

        # Move the turtle normally
        match x:
            case float():
                if isinstance(y, float):
                    super().goto(x, y)
            case tuple():
                super().goto(x)
            case _ as unreachable:
                assert_never(unreachable)


class SpirographPen:
    def __init__(self, wheel: SpirographWheel,
                 radial_offset: float, angle_offset: float,
                 turt: turtle.Turtle):
        self.radial_offset = radial_offset
        self.angle_offset = math.tau * angle_offset

        self.wheel = wheel

        self.turtle = turt

        self.turtle.penup()
        self.go_to_next(0)
        self.turtle.pendown()

    def get_next(self, t: float) -> Tuple[float, float]:
        t = math.tau * t
        f = self.radial_offset
        ao = self.angle_offset
        M = self.wheel.M
        N = self.wheel.N
        RATIO = fractions.Fraction(N, M)
        x: float = self.wheel.x + self.wheel.SCALE * \
            f * RATIO * math.cos((M-N)*t + ao)
        y: float = self.wheel.y - self.wheel.SCALE * \
            f * RATIO * math.sin((M-N)*t + ao)
        return x, y

    def go_to_next(self, t: float) -> None:
        target_x, target_y = self.get_next(t)
        self.turtle.goto(target_x, target_y)

    def __repr__(self) -> str:
        return f"SpirographPen({vars(self)})"


@dataclass
class PenParams:
    turtle_pensize: int
    turtle_initial_color: Any
    turtle_speed: int
    wheel: 'SpirographWheel'
    radial_offset: float
    angle_offset: float
    turtle_hue_steps: None | float


def create_pen_from_params(pp: PenParams) -> SpirographPen:
    if pp.turtle_hue_steps is None:
        turt = turtle.Turtle()
    else:
        turt = CoolerTurtle(pp.turtle_hue_steps)
    turt.pensize(pp.turtle_pensize)
    turt.color(pp.turtle_initial_color)
    turt.speed(pp.turtle_speed)
    return SpirographPen(pp.wheel, pp.radial_offset, pp.angle_offset, turt)


def main() -> None:
    # Parameters
    SCREEN_SIZE = 800, 800
    M = 13
    N = 4
    R_OUTER = int(0.95 * min(SCREEN_SIZE) / 2)
    SCREEN_BACKGROUND_COLOR = "white"
    GRANULARITY = 500
    STEPS = GRANULARITY / math.gcd(M, N)
    INCREMENT = 1 / STEPS

    # Setup
    screen = turtle.Screen()
    screen.setup(SCREEN_SIZE[0], SCREEN_SIZE[1])
    screen.bgcolor(SCREEN_BACKGROUND_COLOR)
    screen.colormode(255)

    wheel = SpirographWheel(M, N, R_OUTER)

    DEFAULT_SPEED = 0
    DEFAULT_PENSIZE = 3
    DEFAULT_HUE_CYCLES = 2
    DEFAULT_HUE_STEPS = STEPS / DEFAULT_HUE_CYCLES

    def random_hue() -> tuple[float, float, float]:
        return cast(tuple[float, float, float],
                    tuple(map(int, colorsys.hls_to_rgb(
                        random.random(), 127.5, -1))))

    penparams: list[PenParams] = [
        PenParams(DEFAULT_PENSIZE, random_hue(), DEFAULT_SPEED,
                  wheel, 0.4, 0.25, DEFAULT_HUE_STEPS),
        PenParams(DEFAULT_PENSIZE, random_hue(), DEFAULT_SPEED,
                  wheel, 0.5, 0.75, DEFAULT_HUE_STEPS),
        PenParams(DEFAULT_PENSIZE, (255, 0, 0), DEFAULT_SPEED,
                  wheel, 0.8, 0, DEFAULT_HUE_STEPS),
        PenParams(DEFAULT_PENSIZE, random_hue(), DEFAULT_SPEED,
                  wheel, 1, 0.5, DEFAULT_HUE_STEPS),
    ]

    pens: list[SpirographPen] = list(map(create_pen_from_params, penparams))

    # Draw loop
    time_start = time.time()
    t = 0.0
    while t <= 1:
        t += INCREMENT
        wheel.go_to_next(t)
        for pen in pens:
            pen.go_to_next(t)
    print(f"Drawing finished in: {time.time() - time_start:0.5} seconds.")

    screen.exitonclick()


if __name__ == "__main__":
    main()
