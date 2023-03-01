from manim import *
config.max_files_cached = 300

coord_reference = NumberPlane()


class Intro(Scene):
    def construct(self):
        virtual_text = Text('Virtualization').set_color_by_gradient(BLUE_A, BLUE_E).move_to(UP*2.5)
        self.play(Write(virtual_text))
        cpu = ImageMobject('cpu.png').next_to(virtual_text, DOWN, buff=.5)
        self.play(FadeIn(cpu))
        qq = ImageMobject('QQ.png').scale(.5).next_to(cpu, DOWN, buff=.5)
        chrome = ImageMobject('chrome.png').scale(.5).next_to(qq, LEFT, buff=.7)
        wangyi = ImageMobject('wangyiyun.png').scale(.5).next_to(qq, RIGHT, buff=.5)
        self.play(FadeIn(qq, chrome, wangyi))
        cpu_c1 = cpu.copy().next_to(chrome, UP, buff=.4)
        cpu_c2 = cpu.copy().next_to(wangyi, UP, buff=.3)
        self.play(FadeIn(cpu_c1, cpu_c2))
        self.play(FadeOut(cpu_c1, cpu_c2))
        for times in range(3):
            self.play(cpu.animate.next_to(chrome, UP, buff=.4), run_time=.2)
            self.play(cpu.animate.next_to(wangyi, UP, buff=.3), run_time=.2)
        self.wait()


class Process(Scene):
    def construct(self):
        process_txt = Text('Process?').set_color_by_gradient(BLUE_A, BLUE_E)
        self.play(Write(process_txt))
        self.clear()
        self.camera.background_color = WHITE
        self.play(FadeIn(ImageMobject('create_process.png').scale(1.2)))
        disk_data = Rectangle(width=1.15, height=.5, stroke_width=0, fill_color=RED, fill_opacity=.5
                              ).move_to([-.15, -1.6, 0])
        mem_data = Rectangle(width=1.1, height=1.7, stroke_width=0, fill_color=RED, fill_opacity=.5
                             ).move_to([.75, 1.65, 0])
        self.play(Create(disk_data))
        self.play(ReplacementTransform(disk_data, mem_data))
        self.camera.background_color = BLACK
        self.clear()
        proc_struct = Code('proc_struct.cpp', style=Code.styles_list[9]).scale(.7)
        self.play(Write(proc_struct))
        self.play(Succession(Indicate(proc_struct[2][18]), Indicate(proc_struct[2][19]), Indicate(proc_struct[2][22]),
                             Indicate(proc_struct[2][23]), Indicate(proc_struct[2][29])))
        pcb = Text('Process\nControl\nBlock\n(PCB)').set_color_by_gradient(BLUE_A, BLUE_E).next_to(proc_struct, RIGHT)
        self.play(Write(pcb))
        self.clear()
        running = VGroup(Circle(stroke_width=0, fill_color=GREEN, fill_opacity=.8))
        running.add(Text('running').scale(.8).move_to(running)).shift(LEFT*2, UP*1.5)
        ready = VGroup(Circle(stroke_width=0, fill_color=YELLOW, fill_opacity=.8))
        ready.add(Text('ready').scale(.8).move_to(ready)).shift(RIGHT*2, UP*1.5)
        blocked = VGroup(Circle(stroke_width=0, fill_color=RED, fill_opacity=.8))
        blocked.add(Text('blocked').scale(.8).move_to(blocked)).shift(DOWN*1.5)
        self.play(Create(VGroup(running, ready, blocked)))
        self.play(Succession(Create(Arrow([-2, .5, 0], blocked)), Create(Arrow([1.1, 1.7, 0], [-1.1, 1.7, 0])),
                             Create(Arrow(blocked, [2, .5, 0])), Create(Arrow([-1.1, 1.3, 0], [1.1, 1.3, 0]))))
        self.wait()


class Control(Scene):
    def construct(self):
        user_mode = Text('user mode').set_color_by_gradient(BLUE_A, BLUE_E)
        kernel_mode = Text('kernel mode').set_color_by_gradient(BLUE_A, BLUE_E)
        self.play(Create(VGroup(user_mode, kernel_mode).arrange(RIGHT, buff=1)))
        cur_mode = SurroundingRectangle(user_mode, stroke_width=0, fill_color=YELLOW, fill_opacity=.5)
        self.play(Create(cur_mode))
        self.play(ReplacementTransform(cur_mode, SurroundingRectangle(kernel_mode, stroke_width=0,
                                                                      fill_color=YELLOW, fill_opacity=.5)))
        self.clear()

        self.camera.background_color = WHITE
        self.play(FadeIn(ImageMobject('restrict.png').scale(1.2)))
        indication = Rectangle(width=2.5, height=.15, stroke_width=0, fill_color=RED, fill_opacity=.5
                               ).move_to([-2.2, 2.4, 0])
        self.play(Create(indication))

        def move_down(line_num, dist):
            for line in range(line_num):
                self.play(indication.animate.shift(DOWN*dist))

        def move_left():
            self.play(indication.animate.shift(LEFT*2.5, DOWN*.22))

        def move_right():
            self.play(indication.animate.shift(RIGHT*2.5, DOWN*.22))
        move_down(3, .2)
        self.play(indication.animate.shift(RIGHT*2.5, DOWN*.8))
        move_down(1, .2)
        move_right()
        move_down(3, .2)
        move_left()
        move_down(2, .2)
        move_left()
        move_down(2, .2)
        move_right()
        move_down(2, .2)
        move_right()
        move_down(2, .2)
        self.play(indication.animate.shift(LEFT*5, DOWN*.2))
        move_down(1, .2)
        self.clear()
        self.play(FadeIn(ImageMobject('timer_interrupt.png').scale(1.2)))
        self.play(Create(indication.move_to([-3, 2.8, 0])))
        self.play(indication.animate.move_to([.7, .6, 0]))
        move_down(3, .21)
        self.play(indication.animate.shift(LEFT*3.5, DOWN*.25))
        move_down(5, .24)
        self.play(indication.animate.shift(RIGHT*3.5, DOWN*.26))
        move_down(2, .23)
        self.wait()


class Schedule(Scene):
    def construct(self):
        fcfs = Text('First Come, First Served').set_color_by_gradient(BLUE_A, BLUE_E)
        self.play(Write(fcfs))
        self.clear()
        turnaround = Text('turnaround time').set_color_by_gradient(BLUE_A, BLUE_E)
        self.play(Write(turnaround))
        turnaround_compute = Tex('$=T_{completion}-T_{arrival}$'
                                 ).scale(1.2).set_color_by_gradient(BLUE_A, BLUE_E).next_to(turnaround, DOWN)
        self.play(Write(turnaround_compute))
        self.clear()
        time = NumberLine(x_range=[0, 120, 20], length=6, include_numbers=True).shift(DOWN)
        proc_a = VGroup(Rectangle(width=.5, height=1, stroke_width=0, fill_color=BLUE_A, fill_opacity=.8))
        proc_b = VGroup(Rectangle(width=.5, height=1, stroke_width=0, fill_color=BLUE_C, fill_opacity=.8))
        proc_c = VGroup(Rectangle(width=.5, height=1, stroke_width=0, fill_color=BLUE_E, fill_opacity=.8))
        processes = VGroup(proc_a, proc_b, proc_c
                           ).arrange(RIGHT, buff=0).move_to([-2.25, -.5, 0])
        proc_a.add(Text('A').next_to(proc_a, UP))
        proc_b.add(Text('B').next_to(proc_b, UP))
        proc_c.add(Text('C').next_to(proc_c, UP))
        self.play(Create(VGroup(time, processes)))
        turnaround_eg1 = Tex(r'$average\quad turnaround\quad time = \frac{10+20+30}{3}=20$'
                             ).next_to(time, DOWN, buff=.5)
        self.play(Write(turnaround_eg1))
        self.play(FadeOut(turnaround_eg1))
        self.play(proc_a[0].animate.stretch(10, 0),
                  VGroup(proc_b, proc_c).animate.shift(RIGHT*4.5))
        self.play(proc_a.animate.shift(RIGHT*2.25))
        turnaround_eg2 = Text('average turnaround time = 110').next_to(time, DOWN, buff=.5)
        self.play(Write(turnaround_eg2))
        self.play(FadeOut(turnaround_eg2))
        self.play(VGroup(proc_b, proc_c).animate.shift(LEFT*5), proc_a.animate.shift(RIGHT))
        turnaround_eg3 = Text('average turnaround time = 50').next_to(time, DOWN, buff=.5)
        self.play(Write(turnaround_eg3))
        self.play(FadeOut(turnaround_eg3))
        self.play(proc_a.animate.shift(LEFT), FadeOut(proc_b, proc_c))
        self.play(Create(VGroup(proc_b, proc_c).next_to(proc_a, RIGHT, buff=0)))
        proc_a1 = VGroup(Rectangle(width=.5, height=1, stroke_width=0, fill_color=BLUE_A, fill_opacity=.8
                                   ).move_to([-2.75, -.5, 0]))
        proc_a1.add(Text('A').next_to(proc_a1, UP))
        proc_a2 = VGroup(Rectangle(width=4.5, height=1, stroke_width=0, fill_color=BLUE_A, fill_opacity=.8
                                   ).next_to(proc_a1[0], RIGHT, buff=1))
        proc_a2.add(Text('A').next_to(proc_a2, UP))
        self.play(ReplacementTransform(proc_a, VGroup(proc_a1, proc_a2)),
                  VGroup(proc_b, proc_c).animate.shift(LEFT*4.5))
        self.clear()
        self.play(Write(Text('response time').set_color_by_gradient(BLUE_A, BLUE_E)))
        self.clear()
        time = NumberLine(x_range=[0, 30, 5], length=6, include_numbers=True).shift(DOWN)
        proc_a = VGroup(Rectangle(width=1, height=1.2, stroke_width=0, fill_color=BLUE_A, fill_opacity=.8))
        proc_b = VGroup(Rectangle(width=1, height=1.2, stroke_width=0, fill_color=BLUE_C, fill_opacity=.8))
        proc_c = VGroup(Rectangle(width=1, height=1.2, stroke_width=0, fill_color=BLUE_E, fill_opacity=.8))
        processes = VGroup(proc_a, proc_b, proc_c
                           ).arrange(RIGHT, buff=0).move_to([-1.5, -.4, 0])
        proc_a.add(Text('A').next_to(proc_a, UP))
        proc_b.add(Text('B').next_to(proc_b, UP))
        proc_c.add(Text('C').next_to(proc_c, UP))
        self.play(Create(VGroup(time, processes)))
        proc_a_seg = proc_a.copy()
        proc_a_seg[0].stretch(.2, 0)
        proc_a_seg[1].scale(.5)
        proc_b_seg = proc_b.copy()
        proc_b_seg[0].stretch(.2, 0)
        proc_b_seg[1].scale(.5)
        proc_c_seg = proc_c.copy()
        proc_c_seg[0].stretch(.2, 0)
        proc_c_seg[1].scale(.5)
        single_round = VGroup(proc_a_seg, proc_b_seg, proc_c_seg).arrange(RIGHT, buff=0)
        rr = VGroup(*[single_round.copy() for _ in range(5)]).arrange(RIGHT, buff=0).move_to(processes)
        self.play(ReplacementTransform(processes, rr))
        rr_txt = Text('Round Robin').set_color_by_gradient(BLUE_A, BLUE_E).next_to(time, DOWN, buff=.5)
        self.play(Write(rr_txt))
        self.wait()


class MultiLevel(Scene):
    def construct(self):
        mlfq = Text('Multi-level Feedback Queue').set_color_by_gradient(BLUE_A, BLUE_E)
        self.play(Write(mlfq))
        self.clear()
        q1 = Text('Q1', color=BLUE_D)
        q2 = Text('Q2', color=BLUE_D)
        q3 = Text('Q3', color=BLUE_D)
        queues = VGroup(q1, q2, q3).scale(.8).arrange(UP, buff=1).shift(LEFT*2)

        def proc_generator(name):
            proc = VGroup(Circle(.5, stroke_width=0, fill_color=BLUE, fill_opacity=.8))
            proc.add(Text(name).scale(.5).move_to(proc))
            proc.add(Arrow(proc.get_left()+LEFT*1.5, proc.get_left()))
            return proc
        queues.add(proc_generator('A').next_to(queues[2], RIGHT),
                   proc_generator('C').next_to(queues[1], RIGHT),
                   proc_generator('D').next_to(queues[0], RIGHT))
        queues.add(proc_generator('B').next_to(queues[3], RIGHT))
        self.play(Create(queues))
        low_priority = Text('low priority', color=BLUE_A).scale(.5).next_to(queues[0], LEFT)
        high_priority = Text('high priority', color=BLUE_A).scale(.5).next_to(queues[2], LEFT)
        self.play(Create(VGroup(low_priority, high_priority)))
        self.play(Circumscribe(VGroup(queues[3][:2], queues[6])))
        self.clear()
        queue_eg = queues[:3].copy()
        time = NumberLine(x_range=[0, 200, 50], length=4).shift(RIGHT)
        queue_eg.add(time.set_y((queue_eg[1].get_y()+queue_eg[2].get_y())/2),
                     time.copy().set_y((queue_eg[0].get_y()+queue_eg[1].get_y())/2))
        dist = queue_eg[3].get_y() - queue_eg[4].get_y()
        num_time = NumberLine(x_range=[0, 200, 50], length=4, include_numbers=True)
        queue_eg.add(num_time.next_to(queue_eg[4], DOWN, buff=1.25))
        proc_q3 = Rectangle(width=.2, height=dist, stroke_width=0, fill_color=BLUE, fill_opacity=.8
                            ).next_to(queue_eg[2], RIGHT, buff=.7)
        proc_q2 = proc_q3.copy().next_to(queue_eg[1], RIGHT, buff=.9)
        proc_q1 = proc_q3.copy().stretch(18, 0).next_to(queue_eg[0], RIGHT, buff=1.1)
        self.play(Succession(Create(queue_eg), Create(proc_q3), Create(proc_q2), Create(proc_q1)))
        self.clear()
        self.camera.background_color = WHITE
        self.play(FadeIn(ImageMobject('starvation.png').scale(1.5)))
        self.clear()
        self.play(FadeIn(ImageMobject('game_scheduler.png')))
        self.clear()
        self.play(FadeIn(ImageMobject('burst.png').scale(1.5)))
        self.play(Create(Arrow([.1, -1.3, 0], [.7, .9, 0], buff=0, color=RED)))
        self.clear()
        self.camera.background_color = BLACK
        mlfq_rules = Text('Rule 1: If Priority(A)>Priority(B), A runs(B doesn\'t).\n'
                          'Rule 2: If Priority(A)=Priority(B), A&B run in RR.\n'
                          'Rule 3: When a job enters the system, it is placed at\n the highest priority.\n'
                          'Rule 4: Once a job uses up its time allotment at a given\n level, its priority is reduced.\n'
                          'Rule 5: After some time period S, move all the jobs in\n the system to the topmost queue.'
                          ).scale(.8)
        VGroup(mlfq_rules[:5], mlfq_rules[48:53], mlfq_rules[91:96], mlfq_rules[152:157], mlfq_rules[223:228]
               ).set(color=BLUE)
        self.play(Write(mlfq_rules))
        self.wait()


class Patch(Scene):
    def construct(self):
        # self.play(Write(Text('How to regain control of the CPU?').set_color_by_gradient(YELLOW_A, YELLOW_E)))
        # self.clear()
        # self.play(Write(Text('timer interrupt').set_color_by_gradient(BLUE_A, BLUE_E)))
        # self.clear()
        self.play(Write(Text('process scheduling').set_color_by_gradient(BLUE_A, BLUE_E)))
        self.clear()
        #
        # time = NumberLine(x_range=[0, 120, 20], length=6, include_numbers=True).shift(DOWN)
        # proc_a = VGroup(Rectangle(width=.5, height=1, stroke_width=0, fill_color=BLUE_A, fill_opacity=.8))
        # proc_b = VGroup(Rectangle(width=.5, height=1, stroke_width=0, fill_color=BLUE_C, fill_opacity=.8))
        # proc_c = VGroup(Rectangle(width=.5, height=1, stroke_width=0, fill_color=BLUE_E, fill_opacity=.8))
        # processes = VGroup(proc_a, proc_b, proc_c
        #                    ).arrange(RIGHT, buff=0).move_to([-2.25, -.5, 0])
        # proc_a.add(Text('A').next_to(proc_a, UP))
        # proc_b.add(Text('B').next_to(proc_b, UP))
        # proc_c.add(Text('C').next_to(proc_c, UP))
        # self.play(Create(VGroup(time, processes)))
        # self.play(Circumscribe(Dot([-3, -1.4, 0]), shape=Circle))
        # run_time = VGroup(Text('10s').scale(.5).next_to(proc_a, DOWN, buff=.8))
        # run_time.add(Arrow(proc_a.get_bottom(), run_time.get_top(), buff=0)).set(color=YELLOW)
        # self.play(Create(run_time))
        # self.play(FadeOut(run_time))
        # turnaround_a = Text('turnaround time of A = 10\n', color=BLUE_A)
        # turnaround_b = Text('turnaround time of B = 20\n', color=BLUE_C)
        # turnaround_c = Text('turnaround time of C = 30\n', color=BLUE_E)
        # each_turnaround = VGroup(turnaround_a, turnaround_b, turnaround_c).arrange(DOWN).scale(.8).next_to(time, UP, 2)
        # self.play(Create(each_turnaround), run_time=3)
        # avg_turnaround = Tex(r'$average\quad turnaround\quad time = \frac{10+20+30}{3}=20$'
        #                      ).next_to(time, DOWN, buff=.5)
        # self.play(ReplacementTransform(each_turnaround, avg_turnaround))
        # self.clear()
        #
        # self.play(Write(Text('No Oracle!', color=RED)))
        # self.clear()
        # self.play(Write(Text('CPU bound → I/O bound').set_color_by_gradient(BLUE, YELLOW)))
        # self.clear()

        # time = NumberLine(x_range=[0, 30, 5], length=6, include_numbers=True).shift(DOWN)
        # proc_a = VGroup(Rectangle(width=1, height=1.2, stroke_width=0, fill_color=BLUE_A, fill_opacity=.8))
        # proc_b = VGroup(Rectangle(width=1, height=1.2, stroke_width=0, fill_color=BLUE_C, fill_opacity=.8))
        # proc_c = VGroup(Rectangle(width=1, height=1.2, stroke_width=0, fill_color=BLUE_E, fill_opacity=.8))
        # processes = VGroup(proc_a, proc_b, proc_c
        #                    ).arrange(RIGHT, buff=0).move_to([-1.5, -.4, 0])
        # proc_a.add(Text('A').next_to(proc_a, UP))
        # proc_b.add(Text('B').next_to(proc_b, UP))
        # proc_c.add(Text('C').next_to(proc_c, UP))
        # self.play(Create(VGroup(time, processes)))
        # proc_a_seg = proc_a.copy()
        # proc_a_seg[0].stretch(.2, 0)
        # proc_a_seg[1].scale(.5)
        # proc_b_seg = proc_b.copy()
        # proc_b_seg[0].stretch(.2, 0)
        # proc_b_seg[1].scale(.5)
        # proc_c_seg = proc_c.copy()
        # proc_c_seg[0].stretch(.2, 0)
        # proc_c_seg[1].scale(.5)
        # single_round = VGroup(proc_a_seg, proc_b_seg, proc_c_seg).arrange(RIGHT, buff=0)
        # rr = VGroup(*[single_round.copy() for _ in range(5)]).arrange(RIGHT, buff=0).move_to(processes)
        # self.play(ReplacementTransform(processes, rr))
        # rr_txt = Text('Round Robin').set_color_by_gradient(BLUE_A, BLUE_E).next_to(time, DOWN, buff=.5)
        # self.play(Write(rr_txt))
        # result = VGroup(Text('response time↓', color=BLUE), Text('turnaround time↑', color=RED)
        #                 ).arrange(RIGHT, buff=1).next_to(time, UP, 2.25)
        # self.play(Create(result))
        # self.play(FadeOut(result))
        # self.wait()

        self.play(Write(Text('进程？').set_color_by_gradient(BLUE_A, BLUE_E)))
        self.clear()
        self.play(Write(Text('如何重新获得CPU控制权？').set_color_by_gradient(YELLOW_A, YELLOW_E)))
        self.clear()
        self.play(Write(Text('时钟中断').set_color_by_gradient(BLUE_A, BLUE_E)))
        self.clear()
        self.play(Write(Text('进程调度').set_color_by_gradient(BLUE_A, BLUE_E)))
        self.clear()
        self.play(Write(Text('响应时间').set_color_by_gradient(BLUE_A, BLUE_E)))
        self.clear()
        self.play(Write(Text('多级反馈队列').set_color_by_gradient(BLUE_A, BLUE_E)))
        self.clear()
        self.play(Write(Text('依赖CPU → 依赖I/O').set_color_by_gradient(BLUE, YELLOW)))
        self.clear()
        mlfq_rules_cn = Text('规则 1：如果 A 的优先级 > B 的优先级，运行 A（不运行 B）。\n'
                             '规则 2：如果 A 的优先级 = B 的优先级，轮转运行 A 和 B。\n'
                             '规则 3：工作进入系统时，放在最高优先级（最上层队列）。\n'
                             '规则 4：一旦工作用完了其在某一层中的时间配额，就降低其优先级。\n'
                             '规则 5：经过一段时间 S，就将系统中所有工作重新加入最高优先级队列。').scale(.6)
        VGroup(mlfq_rules_cn[:3], mlfq_rules_cn[28:31], mlfq_rules_cn[54:57],
               mlfq_rules_cn[81:84], mlfq_rules_cn[112:115]).set(color=BLUE)
        self.play(Write(mlfq_rules_cn))
        self.clear()
        self.wait()
