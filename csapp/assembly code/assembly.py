from manim import *
config.max_files_cached = 300


class AssemblyCode(Scene):
    def construct(self):
        # coord_reference = NumberPlane()
        # self.add(coord_reference)

        # b_code = Code('hello_b.txt', insert_line_no=False)
        # self.play(Create(b_code))
        #
        # c_file = Text('hello.c').scale(0.8)
        # c_rect = SurroundingRectangle(c_file, color=GREEN, buff=0.4)
        # c_code = Code('hello.c', style=Code.styles_list[9])
        # c_group = VGroup(c_file, c_rect, c_code.copy().next_to(c_rect, DOWN, buff=0.2).scale(0.7).shift(RIGHT*0.4))
        #
        # self.play(Create(c_code.shift(LEFT*4)), b_code.animate.next_to(c_code, RIGHT))
        # self.wait()
        #
        # i_file = Text('hello.i').next_to(c_file, RIGHT, buff=1.2).scale(0.8)
        # i_rect = SurroundingRectangle(i_file, color=GREEN, buff=0.4)
        # i_arrow = CurvedArrow(i_rect.get_top(), c_rect.get_top(), color=BLUE).flip()
        # preprocess_text = Text('预处理', color=YELLOW).move_to(i_arrow).scale(0.6)
        # i_group = VGroup(i_file, i_rect, i_arrow, preprocess_text)
        #
        # s_file = Text('hello.s').next_to(i_file, RIGHT, buff=1.2).scale(0.8)
        # s_rect = SurroundingRectangle(s_file, color=GREEN, buff=0.4)
        # s_code = Code('hello.s', style=Code.styles_list[9]).next_to(s_rect, DOWN, buff=0.2).scale(0.7)
        # s_arrow = CurvedArrow(s_rect.get_top(), i_rect.get_top(), color=BLUE).flip()
        # compile_text = Text('编译', color=YELLOW).move_to(s_arrow).scale(0.6)
        # s_group = VGroup(s_file, s_rect, s_code, s_arrow, compile_text)
        #
        # o_file1 = Text('hello.o').next_to(s_file, RIGHT, buff=1.2).scale(0.8)
        # o_rect1 = SurroundingRectangle(o_file1, color=GREEN, buff=0.4)
        # o_file2 = Text('printf.o').next_to(o_file1, UP, buff=1.5).scale(0.8)
        # o_rect2 = SurroundingRectangle(o_file2, color=GREEN, buff=0.4)
        # o_group_pre = VGroup(o_file1, o_file2, o_rect1, o_rect2)
        # o_arrow = CurvedArrow(o_rect1.get_top(), s_rect.get_top(), color=BLUE).flip()
        # assemble_text = Text('汇编', color=YELLOW).move_to(o_arrow).scale(0.6)
        # br = Brace(o_group_pre, RIGHT, color=BLUE)
        # o_code = Code('hello_o.txt',
        #               insert_line_no=False).next_to(o_rect1, DOWN, buff=0.2).scale(0.7).shift(RIGHT*0.7)
        # o_group = VGroup(o_arrow, assemble_text, o_group_pre, br, o_code)
        #
        # b_file = Text('hello').next_to(br, RIGHT, buff=0.5).scale(0.8)
        # b_rect = SurroundingRectangle(b_file, color=GREEN, buff=0.4)
        # link_text = Text('链接', color=YELLOW).next_to(br, LEFT, buff=0.2).scale(0.6)
        # b_group = VGroup(b_file, b_rect, link_text)
        #
        # translation_phase = VGroup(c_group, i_group, s_group, o_group, b_group).move_to(ORIGIN)
        #
        # self.play(Transform(c_code, c_group[-1]),
        #           Transform(b_code, b_group[:2]))
        # self.play(Create(translation_phase), run_time=3)
        # self.play(Circumscribe(s_group[:3]))
        # self.play(FadeOut(c_group, i_group, s_group[3:], o_group, b_group, c_code, b_code))
        # s_group.remove(s_arrow, compile_text)
        # self.play(s_group.animate.move_to(ORIGIN).scale(1.5))
        # self.clear()
        #
        mov_c = Code('mov.c', style=Code.styles_list[9])
        # self.play(Fad/eIn(mov_c))
        #
        # mov_34 = Rectangle(height=0.7, width=1.5, fill_color=GREY,
        #                    fill_opacity=0.3, stroke_width=0).move_to([-0.6, 0, 0])
        # mov_5 = Rectangle(height=0.35, width=1.7, fill_color=GREY,
        #                   fill_opacity=0.3, stroke_width=0).move_to([-.45, -.5, 0])
        # self.play(Create(mov_34))
        # self.play(FadeOut(mov_34), Create(mov_5))
        # self.clear()
        #
        # compile_cmd = Text('gcc  -Og  -S  mov.c')
        # self.play(Write(compile_cmd))
        # self.play(Circumscribe(compile_cmd[:3]))
        # self.play(Circumscribe(compile_cmd[3:6]))
        # opt_o1 = Text('1').move_to(compile_cmd[5])
        # opt_o2 = Text('2').move_to(compile_cmd[5])
        # opt_og = Text('g').move_to(compile_cmd[5])
        # self.play(ReplacementTransform(compile_cmd[5], opt_o1), Circumscribe(compile_cmd[3:6]))
        # self.play(ReplacementTransform(opt_o1, opt_o2), Circumscribe(compile_cmd[3:6]))
        # self.play(Circumscribe(compile_cmd[6:8]), ReplacementTransform(opt_o2, opt_og))
        # self.clear()
        #
        # mov_s = Code('mov.s', style=Code.styles_list[9]).scale(0.7)
        # mov_s_text = Text('mov.s').next_to(mov_s, RIGHT)
        # self.play(Create(mov_s), Write(mov_s_text), run_time=3)
        # self.play(Circumscribe(mov_s_text[4], Circle))
        # self.play(FadeOut(mov_s_text))
        mov_s_core = Code('mov_core.s', style=Code.styles_list[9])
        # self.play(ReplacementTransform(mov_s, mov_s_core))
        #
        # instruction_names = Rectangle(height=1.2, width=1.1).move_to([-0.6, -0.1, 0])
        # operands = Rectangle(height=1, width=2.1).move_to([1, 0, 0])
        # self.play(Circumscribe(instruction_names))
        # self.play(Circumscribe(operands))
        #
        # registers_eg = Text('%rdi, %esi, %rax')
        # self.play(mov_s_core.animate.shift(UP))
        # self.play(ReplacementTransform(mov_s_core.copy(), registers_eg.next_to(mov_s_core, DOWN)))
        # registers = ImageMobject('registers.PNG').scale(0.9).shift(RIGHT*3)
        # self.play(FadeOut(registers_eg), mov_s_core.animate.shift(LEFT*3), FadeIn(registers))
        #
        # rdi_indicator = Rectangle(height=0.5, width=5.6, stroke_color=BLUE,
        #                           fill_color=BLUE, fill_opacity=0.2).move_to([3, 1.05, 0])
        # rsi_indicator = Rectangle(height=0.5, width=5.6, stroke_color=BLUE,
        #                           fill_color=BLUE, fill_opacity=0.2).move_to([3, 1.5, 0])
        # rdx_indicator = Rectangle(height=0.5, width=5.6, stroke_color=BLUE,
        #                           fill_color=BLUE, fill_opacity=0.2).move_to([3, 1.95, 0])
        # rcx_indicator = Rectangle(height=0.5, width=5.6, stroke_color=BLUE,
        #                           fill_color=BLUE, fill_opacity=0.2).move_to([3, 2.35, 0])
        # r8_indicator = Rectangle(height=0.5, width=5.6, stroke_color=BLUE,
        #                          fill_color=BLUE, fill_opacity=0.2).move_to([3, -0.3, 0])
        # r9_indicator = Rectangle(height=0.5, width=5.6, stroke_color=BLUE,
        #                          fill_color=BLUE, fill_opacity=0.2).move_to([3, -0.7, 0])
        # self.play(Create(rdi_indicator))
        # self.play(Create(rsi_indicator))
        # self.play(Create(rdx_indicator))
        # self.play(Create(rcx_indicator))
        # self.play(Create(r8_indicator))
        # self.play(Create(r9_indicator))
        # self.play(FadeOut(rdi_indicator, rsi_indicator, rdx_indicator, rcx_indicator, r8_indicator, r9_indicator))
        #
        # self.play(Create(mov_c.next_to(mov_s_core, DOWN*2)))
        # arrow_xp = Arrow([-2, -0.8, 0], [0.2, 1, 0], color=RED, buff=0)
        # arrow_y = Arrow([-1, -0.8, 0], [0.2, 1.5, 0], color=RED, buff=0)
        # self.play(Create(arrow_xp))
        # self.play(FadeOut(arrow_xp))
        # self.play(Create(arrow_y))
        # self.play(FadeOut(arrow_y))
        #
        # rax = Rectangle(height=1, width=6.4, fill_color=RED, fill_opacity=0.7).move_to([3.5, 0, 0])
        # eax = Rectangle(height=1, width=3.2, fill_color=BLUE, fill_opacity=0.7).move_to([5.1, 0, 0])
        # ax = Rectangle(height=1, width=1.6, fill_color=GREEN, fill_opacity=0.7).move_to([5.9, 0, 0])
        # al = Rectangle(height=1, width=0.8, fill_color=YELLOW, fill_opacity=0.7).move_to([6.3, 0, 0])
        # rax_text = Text('%rax').move_to(rax.get_left()).shift(0.4*RIGHT).scale(0.5)
        # eax_text = Text('%eax').move_to(eax.get_left()).shift(0.4*RIGHT).scale(0.5)
        # ax_text = Text('%ax').move_to(ax.get_left()).shift(0.3*RIGHT).scale(0.5)
        # al_text = Text('%al').move_to(al).scale(0.5)
        # rax_group = VGroup(rax, eax, ax, al, rax_text, eax_text, ax_text, al_text)
        # self.play(FadeOut(registers))
        # self.play(Create(rax_group))
        # self.play(rax_group[1].animate.scale(1.25))
        # self.play(rax_group[1].animate.scale(0.8))
        # self.play(rax_group[2].animate.scale(1.25))
        # self.play(rax_group[2].animate.scale(0.8))
        # self.play(rax_group[3].animate.scale(1.25))
        # self.play(rax_group[3].animate.scale(0.8))
        # self.clear()
        #
        # self.play(Write(mov_s_core.move_to(ORIGIN)))
        # self.play(Circumscribe(instruction_names))
        # instruction_mov = Text('mov', color=GREEN).shift(DOWN)
        # self.play(mov_s_core.animate.shift(UP), Write(instruction_mov))
        # mov = Text('mov    S, D', color=GREEN).shift(DOWN)
        # mov[3:].set_color(BLUE)
        # self.play(ReplacementTransform(instruction_mov, mov))
        #
        # destination = Square(.7).next_to(mov, RIGHT*2)
        # arrow_to_dest = Arrow(mov.get_right(), destination.get_left(), buff=0)
        # src = mov[3].copy()
        # self.play(Create(destination), Create(arrow_to_dest), src.animate.move_to(destination))
        # self.play(FadeOut(destination, arrow_to_dest, src))
        #
        # imm = Text('mov    $Imm, D', color=GREEN).shift(DOWN)
        # imm[3:].set_color(BLUE)
        # self.play(ReplacementTransform(mov, imm))
        # self.play(Indicate(imm[3], color=RED))
        # register_src = Text('mov    %rdi, D', color=GREEN).shift(DOWN)
        # register_src[3:].set_color(BLUE)
        # self.play(ReplacementTransform(imm, register_src))
        # memory_src = Text('mov    (%rdi), D', color=GREEN).shift(DOWN)
        # memory_src[3:].set_color(BLUE)
        # self.play(ReplacementTransform(register_src, memory_src))
        # register_dest = Text('mov    S, %rdi', color=GREEN).shift(DOWN)
        # register_dest[3:].set_color(BLUE)
        # self.play(ReplacementTransform(memory_src, register_dest))
        # memory_dest = Text('mov    S, (%rdi)', color=GREEN).shift(DOWN)
        # memory_dest[3:].set_color(BLUE)
        # self.play(ReplacementTransform(register_dest, memory_dest))
        # memory_src_dest = Text('mov    (%rdi), (%rsi)', color=GREEN).shift(DOWN)
        # memory_src_dest[3:].set_color(BLUE)
        # self.play(ReplacementTransform(memory_dest, memory_src_dest))
        # forbidden = VGroup(Line([-3, -.9, 0], [3, -.9, 0], color=RED), Line([-3, -1.1, 0], [3, -1.1, 0], color=RED))
        # self.play(Create(forbidden))
        # self.play(FadeOut(forbidden, memory_src_dest))
        #
        # self.play(mov_s_core.animate.move_to(ORIGIN))
        # pointer = Triangle(color=ORANGE, fill_color=ORANGE,
        #                    fill_opacity=1).rotate(PI*(3/2)).scale(0.1).move_to([-1.4, .3, 0])
        # self.play(Create(pointer))
        # self.play(mov_s_core.animate.shift(UP*1.5), pointer.animate.shift(UP*1.5),
        #           Write(mov_c.next_to(mov_s_core, DOWN, buff=0)))
        # self.play(Circumscribe(mov_c[2][0][14:17], shape=Circle))
        # self.play(pointer.animate.shift(DOWN*.33))
        # rect = Rectangle(height=.35, width=.8).move_to([.6, 1.5, 0])
        # self.play(Circumscribe(rect, buff=0))
        # self.play(Circumscribe(mov_c[2][0][-2], shape=Circle))
        # rect.shift(RIGHT)
        # self.play(Circumscribe(rect, buff=0))
        # self.play(pointer.animate.shift(DOWN*.33))
        # self.play(pointer.animate.shift(DOWN*.33))
        # self.play(FadeOut(mov_c, pointer), mov_s_core.animate.move_to(ORIGIN))
        #
        # self.play(Indicate(mov_s_core[2][1][4], color=RED), Indicate(mov_s_core[2][3][4], color=RED))
        # self.play(Indicate(mov_s_core[2][2][4:7], color=RED))
        #
        # q = VGroup(*[Square(1, fill_color=YELLOW) for _ in range(8)]).arrange(RIGHT, buff=0).move_to(ORIGIN)
        # q_text = Text('q', color=BLUE)
        # quad_word = Text('quad word', color=RED)
        # long = VGroup(*[Square(1, fill_color=YELLOW) for _ in range(4)]).arrange(RIGHT, buff=0).move_to([-2, -1.5, 0])
        # l_text = Text('l', color=BLUE)
        # double_word = Text('double word', color=RED)
        # w = VGroup(Square(1), Square(1)).arrange(RIGHT, buff=0).move_to([-3, -3, 0])
        # w_text = Text('w', color=BLUE)
        # word = Text('word', color=RED)
        # b = Square(1).move_to([-3.5, -4.5, 0])
        # b_text = Text('b', color=BLUE)
        # byte = Text('byte', color=RED)
        # suffix = VGroup(q_text, l_text, w_text, b_text).arrange(DOWN, buff=1.125)
        # name = VGroup(quad_word, double_word, word, byte).arrange(DOWN, buff=1.125)
        # data_size = VGroup(q, long, w, b)
        # data_size_group = VGroup(suffix, data_size, name).arrange(RIGHT, buff=.2).scale(.75).move_to([1.5, -1.25, 0])
        # self.play(mov_s_core.animate.shift(UP*2.5),
        #           Create(VGroup(data_size_group[0][0], data_size_group[1][0], data_size_group[2][0])))
        # self.play(Create(VGroup(data_size_group[0][1], data_size_group[1][1], data_size_group[2][1])))
        # self.play(Create(VGroup(data_size_group[0][2], data_size_group[1][2], data_size_group[2][2])))
        # self.play(Create(VGroup(data_size_group[0][3], data_size_group[1][3], data_size_group[2][3])))
        #
        # q_copy = data_size_group[1][0].copy()
        # long_copy = data_size_group[1][1].copy()
        # for square in q_copy:
        #     square.set_opacity(.5)
        # for square in long_copy:
        #     square.set_opacity(.5)
        # self.play(Create(long_copy))
        # self.play(ReplacementTransform(long_copy, q_copy))
        #
        # sign_ext = Text('sign\nextension').move_to([-5, 2, 0])
        # sign_ext[0].set_color(RED)
        # zero_ext = Text('zero\nextension').move_to([-5, -2, 0])
        # zero_ext[0].set_color(RED)
        # self.play(Write(sign_ext))
        # self.play(Write(zero_ext))
        #
        # self.play(FadeOut(sign_ext, zero_ext, q_copy, data_size_group))
        # mov_cvt_eg = Text('movsbw, movsbl, movzwl, \n'
        #                   'movzbq, movzwq, movsql...', color=BLUE).next_to(mov_s_core, DOWN, buff=1)
        # self.play(Write(mov_cvt_eg))
        # self.clear()
        #
        # arith_c = Code('arith.c', style=Code.styles_list[9])
        # arith_s = Code('arith.s', style=Code.styles_list[9])
        # eg2 = VGroup(arith_c, arith_s).arrange(RIGHT, buff=1)
        # self.play(Create(eg2))
        #
        # self.play(ReplacementTransform(arith_c[2][0][16].copy(),
        #                                arith_s[2][1][11:]))
        # self.play(Indicate(arith_s[2][1][11:], color=RED))
        # self.play(ReplacementTransform(arith_c[2][0][24].copy(),
        #                                arith_s[2][1][6:10]))
        # self.play(Indicate(arith_s[2][1][6:10], color=RED))
        # self.play(ReplacementTransform(arith_c[2][0][32].copy(),
        #                                arith_s[2][2][7:16]))
        # self.play(Indicate(arith_s[2][2][7:16], color=RED))
        #
        # pointer.next_to(arith_c[2][2][4], LEFT, buff=.2)
        # self.play(Create(pointer))
        # self.play(ReplacementTransform(arith_c[2][2].copy(),
        #                                arith_s[2][1]))
        # self.play(Indicate(VGroup(arith_c[2][2][14], arith_s[2][1][11:]), color=RED))
        # self.play(Indicate(VGroup(arith_c[2][2][18], arith_s[2][1][6:10]), color=RED))
        #
        # self.play(pointer.animate.next_to(arith_c[2][3][4], LEFT, buff=.2))
        # self.play(Indicate(arith_s[2][2][1:5], color=RED))
        # lea_full = Text('load effective address').next_to(eg2[1], DOWN, buff=.5)
        # self.play(ReplacementTransform(arith_s[2][2][1:5].copy(), lea_full))
        # lea_eg = VGroup(Text('p → %rbx'), Text('q → %rdx'), Text('leaq    (%rdx, %rbx, 3), %rax'),
        #                 Text('3*p+q → %rax')).arrange(DOWN, buff=.2).scale(.7).move_to([3.5, -2.7, 0])
        # lea_eg[0][0].set_color(RED)
        # lea_eg[0][2:].set_color(BLUE)
        # lea_eg[1][0].set_color(RED)
        # lea_eg[1][2:].set_color(BLUE)
        # lea_eg[2][:4].set_color(GREEN)
        # lea_eg[2][4:].set_color(BLUE)
        # lea_eg[3][:5].set_color(RED)
        # lea_eg[3][6:].set_color(BLUE)
        # self.play(FadeOut(lea_full), Write(lea_eg[0]))
        # self.play(Write(lea_eg[1]))
        # self.play(Write(lea_eg[2]))
        # self.play(Write(lea_eg[3]))
        # self.play(FadeOut(lea_eg))
        #
        # pointer2 = Triangle(color=YELLOW, fill_color=YELLOW,
        #                     fill_opacity=1).rotate(PI*(3/2)).scale(0.1).next_to(arith_s[2][2][1], LEFT, buff=.2)
        # self.play(Create(pointer2))
        # lea_result = Text('3*z → %rax').next_to(arith_s, DOWN, buff=.3)
        # lea_result[:4].set_color(RED)
        # lea_result[4:].set_color(BLUE)
        # self.play(ReplacementTransform(arith_s[2][2].copy(), lea_result))
        #
        # self.play(pointer2.animate.next_to(arith_s[2][3][1], LEFT, buff=.2))
        # self.play(Indicate(arith_s[2][3][1:5], color=RED))
        # sal_result = Text('16*3*z → %rax', color=RED).next_to(arith_s, DOWN, buff=.3)
        # self.play(FadeOut(lea_result), ReplacementTransform(arith_s[2][3].copy(), sal_result))
        # result = Text('48*z → %rax').next_to(arith_s, DOWN, buff=.3)
        # result[:4].set_color(RED)
        # result[5:].set_color(BLUE)
        # self.play(ReplacementTransform(sal_result, result))
        # self.play(FadeOut(result))
        #
        # self.play(pointer.animate.next_to(arith_c[2][4][4], LEFT, buff=.2),
        #           pointer2.animate.next_to(arith_s[2][4][1], LEFT, buff=.2))
        # self.play(pointer.animate.next_to(arith_c[2][5][4], LEFT, buff=.2),
        #           pointer2.animate.next_to(arith_s[2][5][1], LEFT, buff=.2))
        # self.clear()
        #
        # add_up1 = Table([['inc', '自增'], ['dec', '自减'],
        #                 ['neg', '取反'], ['not', '非'],
        #                  ['or', '或']])
        # add_up2 = Table([['add', '加'], ['imul', '乘'],
        #                  ['idiv', '除'], ['shl', '逻辑左移'],
        #                  ['sar', '算术右移'], ['shr', '逻辑右移']])
        # add_up = VGroup(add_up1, add_up2).arrange(RIGHT, buff=1)
        # self.play(Create(add_up), run_time=3)
        # self.wait()
        # self.clear()
        #
        # xor = Text('xorq    %rax, %rax', color=GREEN)
        # xor[4:].set_color(BLUE)
        # self.play(Write(xor))
        # xor_result = Text('0 → %rax').next_to(xor, DOWN)
        # xor_result[0].set_color(RED)
        # xor_result[2:].set_color(BLUE)
        # self.play(Write(xor_result))
        # self.clear()
        #
        # imul_2op = Text('imul   S, D', color=GREEN)
        # imul_2op[4:].set_color(BLUE)
        # idiv_2op = Text('idiv   S, D', color=GREEN)
        # idiv_2op[4:].set_color(BLUE)
        # imul_idiv_2op = VGroup(imul_2op, Line([-2, 0, 0], [2, 0, 0]), idiv_2op).arrange(DOWN)
        # self.play(Create(imul_idiv_2op))
        # imul_1op = Text('imul   S', color=GREEN)
        # imul_1op[-1].set_color(BLUE)
        # idiv_1op = Text('idiv   S', color=GREEN)
        # idiv_1op[-1].set_color(BLUE)
        # imul_idiv_1op = VGroup(imul_1op, Line([-2, 0, 0], [2, 0, 0]), idiv_1op).arrange(DOWN)
        # self.play(ReplacementTransform(imul_idiv_2op, imul_idiv_1op))
        # self.play(FadeToColor(imul_idiv_1op[2], GREY))
        # imul_result = Text('S*S\'', color=BLUE).next_to(imul_1op, UP, buff=.7)
        # self.play(ReplacementTransform(imul_1op[-1].copy(), imul_result[0]))
        # rax_rect = Rectangle(height=.7, width=4, stroke_color=RED)
        # rax_text = Text('%rax').scale(.5).move_to(rax_rect)
        # rax = VGroup(rax_text, rax_rect).next_to(imul_result, UP, buff=.7)
        # self.play(Create(rax))
        # self.play(ReplacementTransform(rax.copy(), imul_result[1:]))
        # rdx_rect = Rectangle(height=.7, width=4, stroke_color=ORANGE)
        # rdx_text = Text('%rdx').scale(.5).move_to(rdx_rect)
        # rdx = VGroup(rdx_text, rdx_rect)
        # imul_result_loc = VGroup(rdx, rax.copy()).arrange(RIGHT, buff=0).next_to(imul_result, UP, buff=.7)
        # imul_result_dest = Rectangle(height=.7, width=8, fill_color=YELLOW,
        #                              fill_opacity=.5, stroke_width=0).next_to(imul_result, UP, buff=.7)
        # self.play(ReplacementTransform(rax, imul_result_loc))
        # self.play(ReplacementTransform(imul_result, imul_result_dest))
        # self.play(imul_result_dest.animate.shift(DOWN), imul_result_loc.animate.shift(DOWN))
        # self.play(Indicate(imul_result_loc[1]))
        # self.play(Indicate(imul_result_loc[0]))
        #
        # self.play(FadeToColor(imul_idiv_1op[0], GREY),
        #           FadeToColor(imul_idiv_1op[2][:4], GREEN),
        #           FadeToColor(imul_idiv_1op[2][4:], BLUE))
        # idiv_result = Text('S\'/S', color=BLUE).next_to(idiv_1op, DOWN, buff=.7)
        # self.play(ReplacementTransform(idiv_1op[-1].copy(), idiv_result[-1]))
        # idiv_dividend = imul_result_loc.copy().next_to(idiv_result, DOWN, buff=.7)
        # self.play(Create(idiv_dividend))
        # self.play(ReplacementTransform(idiv_dividend, idiv_result[:3]))
        # rax_rect = Rectangle(height=.7, width=4, stroke_color=RED)
        # rax_text = Text('%rax').scale(.5).move_to(rax_rect)
        # idiv_result_loc = VGroup(rax_text, rax_rect).next_to(idiv_result, DOWN, buff=.7)
        # idiv_result_dest = Rectangle(height=.7, width=4, fill_color=YELLOW,
        #                              fill_opacity=.5, stroke_width=0).next_to(idiv_result, DOWN, buff=.7)
        # self.play(Create(idiv_result_loc))
        # self.play(ReplacementTransform(idiv_result, idiv_result_dest))
        # self.play(idiv_result_dest.animate.shift(UP), idiv_result_loc.animate.shift(UP))
        #
        # mul = Text('mul   S', color=GREEN)
        # mul[-1].set_color(BLUE)
        # div = Text('div   S', color=GREEN)
        # div[-1].set_color(BLUE)
        # mul_div = VGroup(mul, Line([-2, 0, 0], [2, 0, 0]), div).arrange(DOWN)
        # self.play(ReplacementTransform(imul_idiv_1op, mul_div))
        # self.clear()
        #
        # if_c = Code('if.c', style=Code.styles_list[9])
        # self.play(Create(if_c))
        # self.play(Circumscribe(if_c[2][3], stroke_color=RED, buff=0))
        # if_s = Code('if.s', style=Code.styles_list[9]).shift(RIGHT*3.5)
        # eg3 = VGroup(if_c, if_s)
        # self.play(Create(if_s), if_c.animate.shift(LEFT*3.5))
        # self.play(Indicate(if_s[2][1][1:5], color=RED),
        #           Indicate(if_s[2][2][1:4], color=RED))
        # self.play(Circumscribe(if_s[2][:7], stroke_color=RED))
        # self.play(Circumscribe(if_s[2][7:], stroke_color=RED))
        # self.play(Indicate(if_s[2][1][1:5], color=RED))
        # self.play(Indicate(if_s[2][2][1:4], color=RED))
        #
        # cf_text = Text('CF')
        # cf = VGroup(cf_text, SurroundingRectangle(cf_text, fill_color=RED,
        #                                           fill_opacity=.5))
        # zf_text = Text('ZF')
        # zf = VGroup(zf_text, SurroundingRectangle(zf_text, fill_color=BLUE,
        #                                           fill_opacity=.5))
        # sf_text = Text('SF')
        # sf = VGroup(sf_text, SurroundingRectangle(sf_text, fill_color=GREEN,
        #                                           fill_opacity=.5))
        # of_text = Text('OF')
        # of = VGroup(of_text, SurroundingRectangle(of_text, fill_color=YELLOW,
        #                                           fill_opacity=.5))
        # condition_codes = VGroup(cf, zf, sf, of).arrange(RIGHT).shift(DOWN*3.5)
        # self.play(Create(condition_codes))
        #
        # unsigned_overflow = Tex('0-1=18446744073709551615', color=ORANGE).next_to(condition_codes, UP, buff=1.2)
        # self.play(eg3.animate.shift(UP*1.4), Write(unsigned_overflow))
        # one = Tex('1')
        # self.play(condition_codes[0][0].animate.shift(UP),
        #           Write(one.move_to(condition_codes[0][1])))
        # zero = Tex('1-1=0', color=ORANGE).next_to(condition_codes, UP, buff=.2)
        # self.play(ReplacementTransform(unsigned_overflow, zero),
        #           condition_codes[0][0].animate.shift(DOWN), FadeOut(one))
        # self.play(condition_codes[1][0].animate.shift(UP),
        #           Write(one.move_to(condition_codes[1][1])))
        # neg = Tex('0-1=-1', color=ORANGE).next_to(condition_codes, UP, buff=.2)
        # self.play(ReplacementTransform(zero, neg),
        #           condition_codes[1][0].animate.shift(DOWN), FadeOut(one))
        # self.play(condition_codes[2][0].animate.shift(UP),
        #           Write(one.move_to(condition_codes[2][1])))
        # signed_overflow = Tex('0+$2^{32}$=0', color=ORANGE).next_to(condition_codes, UP, buff=.2)
        # self.play(ReplacementTransform(neg, signed_overflow),
        #           condition_codes[2][0].animate.shift(DOWN), FadeOut(one))
        # self.play(condition_codes[3][0].animate.shift(UP),
        #           Write(one.move_to(condition_codes[3][1])))
        # self.play(FadeOut(one, signed_overflow),
        #           condition_codes[3][0].animate.shift(DOWN))
        #
        # self.play(Indicate(if_s[2][1][1:5], color=RED))
        # cmp = Text('%rdi - %rsi', color=BLUE).next_to(condition_codes, UP, buff=.8)
        # self.play(Write(cmp))
        # self.play(FadeOut(cmp))
        # self.play(Indicate(if_s[2][2][1:4], color=RED))
        # jump_condition = Text('~(SF^OF)').next_to(condition_codes, UP, buff=.8)
        # self.play(Write(jump_condition))
        # self.play(FadeOut(jump_condition))
        # self.clear()
        #
        # self.play(FadeIn(ImageMobject('jmp.PNG')))
        # self.clear()
        #
        # self.play(Create(eg3))
        # self.play(Create(pointer.next_to(if_c[2][3], LEFT, buff=.2)),
        #           Create(pointer2.next_to(if_s[2][1], LEFT, buff=.2)))
        # self.play(pointer.animate.next_to(if_c[2][7], LEFT, buff=.2),
        #           pointer2.animate.next_to(if_s[2][7], LEFT, buff=.2))
        # self.play(pointer2.animate.next_to(if_s[2][8], LEFT, buff=.2))
        # self.play(FadeOut(pointer, pointer2))
        # self.play(Create(pointer.next_to(if_c[2][3], LEFT, buff=.2)),
        #           Create(pointer2.next_to(if_s[2][1], LEFT, buff=.2)))
        # self.play(pointer.animate.next_to(if_c[2][4], LEFT, buff=.2),
        #           pointer2.animate.next_to(if_s[2][3], LEFT, buff=.2))
        # self.play(pointer2.animate.next_to(if_s[2][4], LEFT, buff=.2))
        # self.clear()
        #
        # switch_c = Code('switch.c', style=Code.styles_list[9]).scale(.8)
        # self.play(Write(switch_c), run_time=3)
        # self.play(Indicate(VGroup(switch_c[2][5][9:12], switch_c[2][9][9:12],
        #                           switch_c[2][12][9:12], switch_c[2][16][9:12],
        #                           switch_c[2][17][9:12]), color=RED))
        # self.play(Circumscribe(switch_c[2][16:20], buff=0))
        # rect1 = SurroundingRectangle(switch_c[2][9:11], color=YELLOW, buff=0)
        # self.play(Create(rect1))
        # rect2 = SurroundingRectangle(switch_c[2][12:15], color=YELLOW, buff=0)
        # self.play(ReplacementTransform(rect1, rect2))
        # self.play(FadeOut(rect2))
        #
        # jmp_table = Code('jmp_table.s', style=Code.styles_list[9]).shift(RIGHT*1.5)
        # self.play(Write(jmp_table))
        # switch_s = Code('switch.s', style=Code.styles_list[9]).scale(.8).shift(RIGHT*3.5)
        # self.play(Write(switch_s), VGroup(switch_c, jmp_table).animate.shift(LEFT*3.5))
        #
        # self.play(Indicate(switch_s[2][1], color=RED))
        # index0 = Integer(0, color=RED).next_to(jmp_table[2][1], LEFT, buff=.2).scale(.8)
        # index2 = Integer(2, color=RED).next_to(jmp_table[2][3], LEFT, buff=.2).scale(.8)
        # index3 = Integer(3, color=RED).next_to(jmp_table[2][4], LEFT, buff=.2).scale(.8)
        # index4 = Integer(4, color=RED).next_to(jmp_table[2][5], LEFT, buff=.2).scale(.8)
        # index6 = Integer(6, color=RED).next_to(jmp_table[2][7], LEFT, buff=.2).scale(.8)
        # arrow0 = Line(switch_c[2][5].get_right(), index0, color=RED, buff=0, stroke_width=.8)
        # arrow2 = Line(switch_c[2][9].get_right(), index2, color=RED, buff=0, stroke_width=.8)
        # arrow3 = Line(switch_c[2][12].get_right(), index3, color=RED, buff=0, stroke_width=.8)
        # arrow4 = Line(switch_c[2][16].get_right(), index4, color=RED, buff=0, stroke_width=.8)
        # arrow6 = Line(switch_c[2][17].get_right(), index6, color=RED, buff=0, stroke_width=.8)
        # mapping = VGroup(index0, index2, index3, index4, index6,
        #                  arrow0, arrow2, arrow3, arrow4, arrow6)
        # self.play(Create(mapping))
        #
        # self.play(Indicate(jmp_table[2][1][7:], color=RED),
        #           Circumscribe(switch_s[2][7:11], buff=0))
        # self.play(Circumscribe(switch_c[2][5:8], buff=0))
        # self.play(Indicate(jmp_table[2][3][7:], color=RED),
        #           Circumscribe(switch_s[2][11:13], buff=0))
        # self.play(Circumscribe(switch_c[9:11], buff=0))
        # self.play(Indicate(VGroup(jmp_table[2][5][7:],
        #                           jmp_table[2][7][7:]), color=RED))
        # self.play(Circumscribe(switch_c[2][16:20],  buff=0))
        # self.play(Indicate(jmp_table[2][2][7:], color=RED),
        #           Indicate(jmp_table[2][6][7:], color=RED),
        #           Circumscribe(switch_s[2][21:24], buff=0))
        # self.play(Indicate(VGroup(switch_s[2][10], switch_s[2][20], switch_s[2][23]),
        #                    color=RED))
        # self.play(Circumscribe(switch_s[2][15:18], buff=0))
        # self.play(Circumscribe(switch_s[2][11:13], buff=0))
        # self.play(Circumscribe(switch_c[2][9:11], buff=0))
        # self.play(Indicate(switch_s[2][2], color=RED))
        # self.play(Indicate(switch_s[2][3][1:3], color=RED))
        # self.clear()
        #
        # loop = VGroup(Text('do...while'), Text('while'), Text('for')).arrange(DOWN)
        # self.play(Create(loop))
        # self.clear()
        #
        # do_while_c = Code('do_while.c', style=Code.styles_list[9])
        # self.play(Write(do_while_c))
        # self.play(Circumscribe(do_while_c[2][5:7], buff=0))
        # self.play(Indicate(do_while_c[2][7][5:], color=RED))
        # do_while_s = Code('do_while.s', style=Code.styles_list[9]).shift(RIGHT*3.5)
        # self.play(Write(do_while_s), do_while_c.animate.shift(LEFT*3.5))
        #
        # self.play(Create(pointer.next_to(do_while_c[2][2], LEFT, buff=.2)),
        #           Create(pointer2.next_to(do_while_s[2][1], LEFT, buff=.2)))
        # self.play(pointer.animate.next_to(do_while_c[2][5], LEFT, buff=.2),
        #           pointer2.animate.next_to(do_while_s[2][3], LEFT, buff=.2))
        # self.play(pointer.animate.next_to(do_while_c[2][6], LEFT, buff=.2),
        #           pointer2.animate.next_to(do_while_s[2][4], LEFT, buff=.2))
        # self.play(pointer.animate.next_to(do_while_c[2][7], LEFT, buff=.2),
        #           pointer2.animate.next_to(do_while_s[2][5], LEFT, buff=.2))
        # self.play(pointer.animate.next_to(do_while_c[2][5], LEFT, buff=.2),
        #           pointer2.animate.next_to(do_while_s[2][3], LEFT, buff=.2))
        # self.play(pointer.animate.next_to(do_while_c[2][8], LEFT, buff=.2),
        #           pointer2.animate.next_to(do_while_s[2][7], LEFT, buff=.2))
        # self.clear()
        #
        # while_c = Code('while.c', style=Code.styles_list[9])
        # while_s = Code('while.s', style=Code.styles_list[9])
        # eg6 = VGroup(while_c, while_s).arrange(RIGHT, buff=1)
        # self.play(Create(eg6), run_time=3)
        #
        # self.play(Create(pointer2.next_to(while_s[2][1], LEFT, buff=.2)))
        # self.play(pointer2.animate.next_to(while_s[2][7], LEFT, buff=.2))
        # self.play(pointer2.animate.next_to(while_s[2][8], LEFT, buff=.2))
        # self.play(pointer2.animate.next_to(while_s[2][4], LEFT, buff=.2))
        # self.play(pointer2.animate.next_to(while_s[2][9], LEFT, buff=.2))
        # self.clear()
        #
        # for_c = Code('for.c', style=Code.styles_list[9])
        # for_s = Code('for.s', style=Code.styles_list[9])
        # eg7 = VGroup(for_c, for_s).arrange(RIGHT, buff=1)
        # self.play(Create(eg7), run_time=3)
        #
        # self.play(Create(pointer2.next_to(for_s[2][1], LEFT, buff=.2)))
        # self.play(pointer2.animate.next_to(for_s[2][2], LEFT, buff=.2))
        # self.play(pointer2.animate.next_to(for_s[2][8], LEFT, buff=.2))
        # self.play(pointer2.animate.next_to(for_s[2][9], LEFT, buff=.2))
        # self.play(pointer2.animate.next_to(for_s[2][5], LEFT, buff=.2))
        # self.play(pointer2.animate.next_to(for_s[2][6], LEFT, buff=.2))
        # self.play(pointer2.animate.next_to(for_s[2][11], LEFT, buff=.2))
        # self.clear()
        #
        # stack_c = Code('stack.c', style=Code.styles_list[9])
        # stack_s = Code('stack.s', style=Code.styles_list[9]).scale(.7)
        # eg8 = VGroup(stack_c, stack_s).arrange(RIGHT, buff=.8)
        # self.play(Create(eg8), run_time=3)
        #
        # self.play(Indicate(stack_s[2][23][1:5], color=RED))
        # self.play(ReplacementTransform(stack_c[2][17][9:-2].copy(),
        #                                VGroup(stack_c[2][0][10:], stack_c[2][1:4])))
        #
        # bl = Square(1)
        # bl_text = Text('%bl').next_to(bl, UP)
        # original_data = Text('00', color=RED).move_to(bl)
        # bl_group = VGroup(bl, bl_text, original_data)
        # self.play(Create(bl_group))
        # current_data = Text('FF', color=RED).next_to(bl, LEFT)
        # self.play(Write(current_data))
        # self.play(current_data.animate.move_to(bl),
        #           bl_group[2].animate.shift(RIGHT))
        # self.play(FadeOut(original_data))
        # self.play(FadeOut(bl_group[:2], current_data))
        #
        # return_arrow = CurvedArrow(stack_c[2][8].get_right(),
        #                            stack_c[2][13].get_right(), color=RED).flip().shift(RIGHT*.5)
        # how = Text('?', color=RED).scale(.8).next_to(return_arrow, RIGHT)
        # self.play(Create(return_arrow))
        # self.play(Write(how))
        # self.clear()
        #
        # stack_cells = [Rectangle(width=5, height=.8) for _ in range(4)]
        # stack = VGroup(*stack_cells).arrange(DOWN, buff=0).shift(UP*2)
        # self.play(Create(stack))
        # grey_rect = Rectangle(width=5, height=3.2, fill_color=GREY, fill_opacity=.5).move_to(stack)
        # self.play(Create(grey_rect))
        # arg7_cell = Rectangle(width=5, height=.8, fill_color=BLUE, fill_opacity=.5)
        # arg7_text = Text('参数7').move_to(arg7_cell).scale(.8)
        # arg7 = VGroup(arg7_text, arg7_cell).next_to(stack, DOWN, buff=1.5)
        # self.play(Create(arg7))
        # self.play(arg7.animate.next_to(stack, DOWN, buff=0))
        # save_reg_cell = Rectangle(width=5, height=.8, fill_color=YELLOW, fill_opacity=.5)
        # saved_reg_text = Text('寄存器保存值').move_to(save_reg_cell).scale(.8)
        # saved_reg = VGroup(saved_reg_text, save_reg_cell).next_to(arg7, DOWN, buff=1.5)
        # self.play(Create(saved_reg))
        # self.play(saved_reg.animate.next_to(arg7, DOWN, buff=0))
        # loc_arg_cell = Rectangle(width=5, height=.8, fill_color=GREEN, fill_opacity=.5)
        # loc_arg_text = Text('局部变量').move_to(loc_arg_cell).scale(.8)
        # loc_arg = VGroup(loc_arg_text, loc_arg_cell).next_to(saved_reg, DOWN, buff=1.5)
        # self.play(Create(loc_arg))
        # self.play(loc_arg.animate.next_to(saved_reg, DOWN, buff=0))
        # address_cell = Rectangle(width=5, height=.8, fill_color=RED, fill_opacity=.5)
        # address_text = Text('返回地址').move_to(address_cell).scale(.8)
        # return_address = VGroup(address_cell, address_text).next_to(loc_arg, DOWN, buff=1)
        # self.play(Create(return_address))
        # self.play(return_address.animate.next_to(loc_arg, DOWN, buff=0))
        # self.play(return_address.animate.shift(DOWN*2.1),
        #           loc_arg.animate.shift(DOWN*3),
        #           saved_reg.animate.shift(DOWN*4), arg7.animate.shift(DOWN*5),
        #           FadeOut(grey_rect))
        # self.play(stack.animate.move_to(ORIGIN))
        # self.clear()
        #
        # self.play(Create(eg8), run_time=3)
        # self.play(Indicate(stack_s[2][9][-4:], color=RED, scale_factor=2.5))
        # stack = VGroup(*[Rectangle(width=2.4, height=.4) for _ in range(4)]).arrange(DOWN, buff=0).shift(LEFT*.3)
        # self.play(Create(stack))
        # pointer.next_to(stack[-1], LEFT, buff=0)
        # rsp_text = Text('%rsp', color=BLUE).scale(.5).next_to(pointer, LEFT)
        # rsp = VGroup(pointer, rsp_text)
        # self.play(Create(rsp))
        # address = VGroup(Integer(24), Integer(16), Integer(8), Integer(0)).arrange(DOWN, buff=.4)
        # address.next_to(stack, RIGHT, buff=0).set_color(RED).scale(.6)
        # stack.add(address)
        # note = Text('*这里的地址只是抽象表示，并非实际地址').scale(.5).next_to(eg8[0], DOWN, buff=0)
        # self.play(Create(stack[-1]), Write(note))
        #
        # self.play(Indicate(stack_s[2][9], color=RED, scale_factor=2.5))
        # add_space = stack[:-1].copy().shift(DOWN*.8)
        # self.play(Create(add_space), stack.animate.shift(UP*.8))
        # add_address = VGroup(Integer(-8), Integer(-16), Integer(-24), Integer(-32)).arrange(DOWN, buff=.4)
        # add_address.set_color(RED).next_to(add_space, RIGHT, buff=0).scale(.6).shift(LEFT*.1)
        # add_space.add(add_address)
        # self.play(Create(add_space[-1]), rsp.animate.next_to(add_space[3], LEFT, buff=0))
        #
        # self.play(Indicate(VGroup(stack_c[2][17][13:16], stack_c[2][17][22:25],
        #                           stack_c[2][17][31:34], stack_c[2][17][40:43]),
        #                    color=RED))
        # self.play(Indicate(stack_s[2][10], color=RED, scale_factor=2.5))
        # x1_rect = Rectangle(width=2.4, height=.4, fill_color=BLUE,
        #                     fill_opacity=.5).move_to(add_space[0])
        # x1_text = Text('x1').scale(.5).move_to(x1_rect)
        # x1 = VGroup(x1_rect, x1_text)
        # self.play(ReplacementTransform(stack_c[2][13][9:11].copy(), x1))
        # x2_rect = Rectangle(width=1.2, height=.4, fill_color=BLUE,
        #                     fill_opacity=.5).move_to(add_space[1]).shift(LEFT*.6)
        # stack_x2 = Text('x2').scale(.5).move_to(x2_rect)
        # x2 = VGroup(x2_rect, stack_x2)
        # self.play(Indicate(stack_s[2][11], color=RED, scale_factor=2.5))
        # self.play(ReplacementTransform(stack_c[2][14][8:10].copy(), x2))
        # x3_rect = Rectangle(width=.6, height=.4, fill_color=BLUE,
        #                     fill_opacity=.5).next_to(x2_rect, RIGHT, buff=0)
        # stack_x3 = Text('x3').scale(.5).move_to(x3_rect)
        # x3 = VGroup(x3_rect, stack_x3)
        # self.play(Indicate(stack_s[2][12], color=RED, scale_factor=2.5))
        # self.play(ReplacementTransform(stack_c[2][15][10:12].copy(), x3))
        # x4_rect = Rectangle(width=.3, height=.4, fill_color=BLUE,
        #                     fill_opacity=.5).next_to(x3_rect, RIGHT, buff=0)
        # stack_x4 = Text('x4').scale(.5).move_to(x4_rect)
        # x4 = VGroup(x4_rect, stack_x4)
        # self.play(Indicate(stack_s[2][13], color=RED, scale_factor=2.5))
        # self.play(ReplacementTransform(stack_c[2][16][9:11].copy(), x4))
        #
        # self.play(Indicate(VGroup(stack_c[2][17][8:33],
        #                           stack_s[2][15:23]), color=RED))
        # arg8_rect = Rectangle(width=2.4, height=.4, fill_color=GREEN,
        #                       fill_opacity=.5).move_to(add_space[2])
        # arg8_text = Text('&x4').scale(.5).move_to(arg8_rect)
        # arg8 = VGroup(arg8_text, arg8_rect)
        # self.play(Indicate(stack_s[2][14:16], color=RED))
        # self.play(ReplacementTransform(stack_c[2][17][-5:-2].copy(), arg8))
        # arg7_rect = Rectangle(width=.3, height=.4, fill_color=GREEN,
        #                       fill_opacity=.5).move_to(add_space[3]).shift(RIGHT*1.05)
        # arg7_text = Text('4').scale(.5).move_to(arg7_rect)
        # arg7 = VGroup(arg7_text, arg7_rect)
        # self.play(Indicate(stack_s[2][16], color=RED))
        # self.play(ReplacementTransform(stack_c[2][17][-9:-7].copy(), arg7))
        # self.play(Indicate(VGroup(arg8, stack_c[2][17][-5:-2]), color=GREEN))
        # self.play(Indicate(VGroup(arg7, stack_c[2][17][-9:-7]), color=GREEN))
        #
        # return_rect = Rectangle(width=2.4, height=.4, fill_color=RED,
        #                         fill_opacity=.5).next_to(add_space[3], DOWN, buff=0)
        # return_text = Text('返回地址').scale(.5).move_to(return_rect)
        # return_address = VGroup(return_rect, return_text)
        # self.play(Create(return_address))
        # self.play(Indicate(stack_s[2][23], color=RED), Circumscribe(stack_s[2][:8], buff=0))
        # self.play(FadeOut(return_address))
        # self.play(Indicate(stack_s[2][24:31], color=RED))
        # self.play(Indicate(stack_s[2][-2], color=RED))
        # self.play(FadeOut(x1, x2, x3, x4, arg7, arg8, add_space, add_address),
        #           stack.animate.shift(DOWN*.8),
        #           rsp.animate.next_to(add_space[1], LEFT, buff=0))
        # self.clear()
        #
        # registers = ImageMobject('registers_hd.png').scale(1.4)
        # self.play(FadeIn(registers))
        # rbx_rect = Rectangle(width=6.2, height=.5, stroke_color=BLUE, fill_color=BLUE,
        #                      fill_opacity=.5).move_to([0, 3.3, 0])
        # rbp_rect = rbx_rect.copy().shift(DOWN*2.55)
        # r12_r15_rect = Rectangle(width=6.2, height=2, stroke_color=BLUE, fill_color=BLUE,
        #                          fill_opacity=.5).move_to([0, -3, 0])
        # self.play(Create(rbx_rect))
        # self.play(Create(rbp_rect))
        # self.play(Create(r12_r15_rect))
        # self.play(Write(Text('caller\nsaved', should_center=True).next_to(registers, RIGHT, buff=1)))
        # self.clear()
        #
        # saved_reg_c = Code('save_register.c', style=Code.styles_list[9])
        # saved_reg_s = Code('save_register.s', style=Code.styles_list[9])
        # saved_reg = VGroup(saved_reg_c, saved_reg_s).arrange(RIGHT, buff=1)
        # self.play(Create(saved_reg))
        #
        # self.play(Indicate(saved_reg_c[2][2], color=RED))
        # self.play(Indicate(saved_reg_c[2][0][12], color=RED, scale_factor=2.5))
        # self.play(Indicate(saved_reg_c[2][3], color=RED))
        # self.play(Indicate(saved_reg_c[2][2][9], color=RED, scale_factor=2.5))
        # self.play(Indicate(saved_reg_s[2][3], color=RED))
        # self.play(Indicate(saved_reg_s[2][6], color=RED))
        # self.play(Indicate(saved_reg_s[2][1:3], color=RED))
        # self.play(Indicate(saved_reg_s[2][10:12], color=RED))
        # self.clear()
        #
        # recurse_c = Code('recurse.c', style=Code.styles_list[9])
        # recurse_s = Code('recurse.s', style=Code.styles_list[9])
        # recurse = VGroup(recurse_c, recurse_s).arrange(RIGHT, buff=1)
        # self.play(Create(recurse))
        # self.play(Indicate(VGroup(recurse[1][2][0], recurse[1][2][5]), color=RED))
        # self.play(Indicate(recurse[1][2][6], color=RED))
        #
        # n4 = Text('n = 4', color=GREEN).next_to(recurse[0], DOWN, buff=1)
        # recurse_s.move_to(recurse[1])
        # self.play(Write(n4))
        # self.play(Create(pointer2.next_to(recurse_s[2][1], LEFT, buff=.2)))
        # self.play(pointer2.animate.next_to(recurse_s[2][6], LEFT, buff=.2))
        # self.play(FadeOut(recurse[0]))
        # yellow_cell = Rectangle(width=5, height=.8, fill_color=YELLOW,
        #                         fill_opacity=.5).next_to(recurse[1], LEFT, buff=1).shift(UP*2)
        # red_cell = Rectangle(width=5, height=.8, fill_color=RED, fill_opacity=.5)
        # return_text = Text('返回地址').scale(.8).move_to(red_cell)
        # return_address = VGroup(red_cell, return_text).next_to(yellow_cell, DOWN, buff=0)
        # rbx_text = Text('%rbx').scale(.8).move_to(yellow_cell)
        # stack = VGroup(VGroup(yellow_cell, rbx_text))
        # self.play(Create(stack[-1]))
        # rbx1 = Text('%rbx = 4', color=BLUE).next_to(recurse_s, DOWN)
        # self.play(pointer2.animate.next_to(recurse_s[2][7], LEFT, buff=.2),
        #           Write(rbx1))
        # n3 = Text('n = 3', color=GREEN).move_to(n4)
        # self.play(pointer2.animate.next_to(recurse_s[2][8], LEFT, buff=.2),
        #           ReplacementTransform(n4, n3))
        # stack.add(return_address)
        # self.play(pointer2.animate.next_to(recurse_s[2][9], LEFT, buff=.2))
        # call1 = recurse_s.copy().scale(.9)
        # self.play(Create(stack[-1]), FadeOut(pointer2),
        #           ReplacementTransform(recurse_s[2][9][6:].copy(), call1))
        # stack.add(VGroup(yellow_cell.copy().shift(DOWN*1.6),
        #                  Text('%rbx=4').scale(.8).move_to(yellow_cell.copy().shift(DOWN*1.6))))
        # self.play(Create(pointer2.next_to(call1[2][1], LEFT, buff=.2)))
        # self.play(Create(stack[-1]),
        #           pointer2.animate.next_to(call1[2][6], LEFT, buff=.2))
        # rbx2 = Text('%rbx = 3', color=BLUE).move_to(rbx1)
        # self.play(ReplacementTransform(rbx1, rbx2),
        #           pointer2.animate.next_to(call1[2][7], LEFT, buff=.2))
        # n2 = Text('n = 2', color=GREEN).move_to(n4)
        # self.play(ReplacementTransform(n3, n2),
        #           pointer2.animate.next_to(call1[2][8], LEFT, buff=.2))
        # self.play(pointer2.animate.next_to(call1[2][9], LEFT, buff=.2))
        # call2 = recurse_s.copy().scale(.8)
        # stack.add(return_address.copy().shift(DOWN*1.6))
        # self.play(Create(stack[-1]), FadeOut(pointer2),
        #           ReplacementTransform(call1[2][9][6:].copy(), call2))
        # self.play(Create(pointer2.next_to(call2[2][1], LEFT, buff=.2)))
        # stack.add(VGroup(yellow_cell.copy().shift(DOWN*3.2),
        #                  Text('%rbx = 3').scale(.8).move_to(yellow_cell.copy().shift(DOWN*3.2))))
        # self.play(Create(stack[-1]),
        #           pointer2.animate.next_to(call2[2][6], LEFT, buff=.2))
        # rbx3 = Text('%rbx = 2', color=BLUE).move_to(rbx1)
        # self.play(pointer2.animate.next_to(call2[2][7], LEFT, buff=.2),
        #           ReplacementTransform(rbx2, rbx3))
        # n1 = Text('n = 1', color=GREEN).move_to(n4)
        # self.play(ReplacementTransform(n2, n1),
        #           pointer2.animate.next_to(call2[2][8], LEFT, buff=.2))
        # call3 = recurse_s.copy().scale(.7)
        # stack.add(return_address.copy().shift(DOWN*3.2))
        # self.play(pointer2.animate.next_to(call2[2][9], LEFT, buff=.2))
        # self.play(Create(stack[-1]), FadeOut(pointer2),
        #           ReplacementTransform(call2[2][9][6:].copy(), call3))
        #
        # self.play(Create(pointer2.next_to(call3[2][1], LEFT, buff=.2)))
        # result1 = Text('result = 1', color=RED).move_to([0, -3.5, 0])
        # self.play(Write(result1),
        #           pointer2.animate.next_to(call3[2][3], LEFT, buff=.2))
        # self.play(pointer2.animate.next_to(call3[2][4], LEFT, buff=.2))
        # self.play(FadeOut(pointer2, stack[-1], call3),
        #           ReplacementTransform(call3[2][4], call2))
        # stack.remove(stack[-1])
        # result2 = Text('result = 1*2', color=RED).move_to(result1)
        # self.play(Create(pointer2.next_to(call2[2][10], LEFT, buff=.2)),
        #           ReplacementTransform(result1, result2))
        # rbx2 = Text('%rbx = 3', color=BLUE).move_to(rbx1)
        # self.play(pointer2.animate.next_to(call2[2][11], LEFT, buff=.2),
        #           FadeOut(stack[-1]), ReplacementTransform(rbx3, rbx2))
        # stack.remove(stack[-1])
        # self.play(pointer2.animate.next_to(call2[2][-1], LEFT, buff=.2))
        # self.play(FadeOut(pointer2, stack[-1], call2),
        #           ReplacementTransform(call2[2][-1], call1))
        # stack.remove(stack[-1])
        # result3 = Text('result = 1*2*3', color=RED).move_to(result1)
        # self.play(Create(pointer2.next_to(call1[2][10], LEFT, buff=.2)),
        #           ReplacementTransform(result2, result3))
        # rbx1 = Text('%rbx = 4', color=BLUE).next_to(recurse_s, DOWN)
        # self.play(pointer2.animate.next_to(call1[2][11], LEFT, buff=.2),
        #           FadeOut(stack[-1]), ReplacementTransform(rbx2, rbx1))
        # stack.remove(stack[-1])
        # self.play(pointer2.animate.next_to(call1[2][-1], LEFT, buff=.2))
        # self.play(FadeOut(pointer2, stack[-1], call1),
        #           ReplacementTransform(call1[2][-1], recurse_s))
        # stack.remove(stack[-1])
        # result4 = Text('result = 1*2*3*4', color=RED).move_to(result1)
        # self.play(Create(pointer2.next_to(recurse_s[2][10], LEFT, buff=.2)),
        #           ReplacementTransform(result3, result4))
        # self.play(pointer2.animate.next_to(recurse_s[2][11], LEFT, buff=.2),
        #           FadeOut(stack[-1]))
        # self.play(pointer2.animate.next_to(recurse_s[2][12], LEFT, buff=.2))
        # self.play(FadeOut(rbx1, n1), result4.animate.next_to(recurse_s, LEFT, buff=1.5))
        # self.clear()
        #
        # array_3cells = VGroup(*[Square(1) for _ in range(3)]).arrange(RIGHT, buff=0)
        # array = VGroup(array_3cells, Text('...'), Square(1, fill_color=YELLOW),
        #                Text('...'), array_3cells.copy()).arrange(RIGHT)
        # array.add(Integer(0, color=ORANGE).next_to(array[0][0], UP),
        #           Integer(1, color=ORANGE).next_to(array[0][1], UP),
        #           Integer(2, color=ORANGE).next_to(array[0][2], UP),
        #           Text('i', color=ORANGE).next_to(array[2], UP),
        #           Text('...', color=ORANGE).next_to(array[-1], UP))
        # self.play(Create(array))
        # rdx = Text('%rdx', color=BLUE).next_to(array[0][0], DOWN, buff=1.5)
        # self.play(Create(VGroup(rdx, Arrow(array[0][0].get_bottom(), rdx.get_top(), buff=0, color=ORANGE))))
        # rcx = Text('%rcx', color=BLUE).next_to(array[-2], UP, buff=1.5)
        # self.play(Create(VGroup(rcx, Arrow(array[-2].get_top(), rcx.get_bottom(), buff=0, color=RED))))
        # ei = Text('(%rdx, %rcx, L)', color=BLUE).next_to(array[2], DOWN, buff=1.5)
        # self.play(array[2].animate.set_opacity(.5), Write(ei),
        #           Create(Arrow(array[2].get_bottom(), ei.get_top(), buff=0, color=RED)))
        # self.clear()
        #
        # row = VGroup(*[Square(1, fill_color=YELLOW) for _ in range(6)]).arrange(RIGHT, buff=0)
        # array2d = VGroup(*[row.copy() for _ in range(6)]).arrange(DOWN, buff=0)
        # self.play(Create(array2d))
        # row_br = Brace(array2d, DOWN, color=BLUE)
        # column_br = Brace(array2d, RIGHT, color=BLUE)
        # self.play(Create(VGroup(column_br, Text('M', color=RED).next_to(column_br, RIGHT))))
        # self.play(Create(VGroup(row_br, Text('N', color=RED).next_to(row_br, DOWN, buff=0))))
        # self.play(Create(VGroup(Text('i', color=ORANGE).next_to(array2d[1][0], LEFT),
        #                         Text('j', color=ORANGE).next_to(array2d[0][3], UP))))
        # crossing_line = VGroup(Line([.5, 3.5, 0], [.5, -3.5, 0], color=BLUE),
        #                        Line([-3.5, 1.5, 0], [3.5, 1.5, 0], color=BLUE))
        # self.play(Create(crossing_line))
        # self.play(FadeOut(crossing_line),
        #           array2d[1][3].animate.set_opacity(.5))
        # self.play(array2d[0].animate.set_opacity(.3),
        #           array2d[1][:3].animate.set_opacity(.3),
        #           Write(Text('首地址+L*(N*i+j)', color=GREEN).rotate(PI/2).next_to(array2d, LEFT, buff=1)))
        # self.clear()
        #
        # self.play(FadeIn(ImageMobject('float_registers.png').scale(1.4)))
        # ref_line = Line([2.7, 0, 0], [2.7, 4, 0])
        # arg_reg_br = Brace(ref_line, RIGHT, color=BLUE)
        # self.play(Create(arg_reg_br),
        #           Write(Text('传递参数', color=GREEN).next_to(arg_reg_br, RIGHT)))
        # xmm0_rect = Rectangle(width=5.4, height=.5, stroke_color=BLUE, fill_color=BLUE,
        #                       fill_opacity=.5).move_to([0, 3.8, 0])
        # self.play(Create(xmm0_rect), Write(Text('函数返回值', color=GREEN).next_to(xmm0_rect, LEFT).scale(.7)))
        # self.clear()
        #
        # float_ins_eg = Table([['movsd', '转移'],
        #                       ['cvttss2si',  '单精度浮点型转化为整型'],
        #                       ['addss', '加'],
        #                       ['subss', '减'],
        #                       ['mulss', '乘'],
        #                       ['divss', '除'],
        #                       ['maxss', '最大值'],
        #                       ['minss', '最小值'],
        #                       ['sqrtss', '开根号'],
        #                       ['xorps', '异或'],
        #                       ['andps', '与'],
        #                       ['comiss', '比较']],
        #                      col_labels=[Text('指令', color=GREEN), Text('注释', color=ORANGE)]).scale(.45)
        # table_name = Text('浮点数指令例', color=GREEN).scale(.7).rotate(PI/2).next_to(float_ins_eg, LEFT)
        # self.play(Create(VGroup(float_ins_eg, table_name)), run_time=3)
        #
        # suffix = VGroup()
        # for row in range(2, 14):
        #     suffix.add((float_ins_eg.get_entries((row, 1))[0][-2:]))
        # self.add(suffix)
        # self.play(Indicate(suffix, color=RED))
        # self.clear()
        #
        # float_imm = VGroup(Code('float_num.c', style=Code.styles_list[9]),
        #                    Code('float_num.s', style=Code.styles_list[9])).arrange(DOWN)
        # self.play(Create(float_imm))
        # self.play(Circumscribe(float_imm[1][2][4:]))
        # self.clear()
        #
        # pf_text = Text('PF')
        # pf = VGroup(pf_text, SurroundingRectangle(pf_text, fill_color=GREEN, fill_opacity=.5))
        # condition_codes = VGroup(cf, zf, pf).arrange(RIGHT)
        # self.play(Create(condition_codes))
        # condition_table = Table([['无序', '1', '1', '1'],
        #                          ['S2 < S1', '1', '0', '0'],
        #                          ['S2 = S1', '0', '1', '0'],
        #                          ['S2 > S1', '0', '0', '0']],
        #                         col_labels=[Text('序', color=ORANGE), Text('CF', color=RED),
        #                                     Text('ZF', color=BLUE), Text('PF', color=GREEN)]).shift(UP*1.5).scale(.8)
        # condition_table.remove(*condition_table.get_vertical_lines())
        # self.play(Create(condition_table), condition_codes.animate.next_to(condition_table, DOWN, buff=1))
        # self.wait()
        # self.clear()
        #
        com_table = Table([['pushq, movq', 'push, mov'],
                           ['%rbx', 'rbx'],
                           ['(%rbx)', 'QWORD PTR [rbx]']],
                          col_labels=[Text('ATT', color=RED), Text('Intel', color=BLUE)])
        att_intel = VGroup(com_table.get_entries((1, 1)).copy(),
                           com_table.get_entries((1, 2)).copy()).shift(DOWN*2)
        self.play(Create(att_intel))
        self.play(Circumscribe(att_intel[0]))
        self.play(att_intel.animate.shift(UP*2))
        self.play(Create(com_table))
        self.wait()
