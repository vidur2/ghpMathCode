from manimlib import *
from math import floor

class ComplexMapping(Scene):
    def construct(self):
        c_grid = ComplexPlane()
        moving_c_grid = c_grid.copy()
        moving_c_grid.prepare_for_nonlinear_transform()
        c_grid.set_stroke(BLUE_E, 1)
        c_grid.add_coordinate_labels(font_size=24)
        complex_map_words.to_corner(UR)
        complex_map_words.set_stroke(BLACK, 5, background=True)

        self.play(
            Write(c_grid, run_time=3),
            FadeIn(moving_c_grid),
        )
        self.wait()

        self.play(
            moving_c_grid.animate.apply_complex_function(lambda x: x**2 + b*floor(x) + 1),
            run_time=6,
        )
        self.wait(2)