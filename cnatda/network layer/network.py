from manim import *


class Pic(Scene):
    def construct(self):
        flow_table = Table([['首部', '计数器', '行为'], ['...\n...\n...\n...', '...\n...\n...\n...', '...\n...\n...\n...']],
                           include_outer_lines=True).scale(.8)
        flow_table.add_highlighted_cell((2, 1), color=BLUE_C)
        flow_table.add_highlighted_cell((2, 2), color=BLUE_D)
        flow_table.add_highlighted_cell((2, 3), color=BLUE_E)
        flow_table.add(Text('流表').next_to(flow_table, UP)).shift(DOWN*.3)
        self.add(flow_table)
