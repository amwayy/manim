from manim import *
import math

coord_ref = NumberPlane()


class Thread(Scene):
    def construct(self):
        mem = Rectangle(width=2.5, height=6, fill_color=BLUE_A, fill_opacity=.8)
        code = VGroup(Rectangle(width=2.5, height=.5, fill_color=BLUE, fill_opacity=.8))
        code.add(Text('代码').scale(.5).move_to(code))
        heap = VGroup(Rectangle(width=2.5, height=.5, fill_color=GREEN, fill_opacity=.8))
        heap.add(Text('堆').scale(.5).move_to(heap))
        stack = Rectangle(width=2.5, height=.5, fill_color=YELLOW_E, fill_opacity=.8)
        stack.add(Text('栈').scale(.5).move_to(stack))
        addr_space = VGroup(code, heap, Rectangle(width=2.5, height=.5, fill_color=BLUE_A, fill_opacity=.8), stack
                            ).arrange(DOWN, buff=0)
        self.play(Create(VGroup(mem, addr_space)))
        addr_space_c1 = addr_space.copy().next_to(addr_space, UP, buff=0)
        addr_space_c2 = addr_space.copy().next_to(addr_space, DOWN, buff=0)
        self.play(Create(VGroup(addr_space_c1, addr_space_c2)))
        self.play(FadeOut(mem, addr_space_c1, addr_space_c2), VGroup(code, heap).animate.shift(UP),
                  stack.animate.shift(DOWN), addr_space[2].animate.stretch(5, 1))
        stack2 = VGroup(Rectangle(width=2.5, height=.5, fill_color=YELLOW_E, fill_opacity=.8
                                  ).next_to(stack, UP, buff=.5))
        stack2.add(Text('栈2').scale(.5).move_to(stack2))
        self.play(Transform(stack[1], Text('栈1').scale(.5).move_to(stack)), Create(stack2))
        self.play(Write(Text('并发性').set_color_by_gradient(BLUE_A, BLUE_E).next_to(stack, DOWN, buff=1)))
        self.clear()

        concurrency = Code('concurrency.c', style=Code.styles_list[9]).scale(.75).shift(LEFT*2.5)
        self.play(Create(concurrency))
        self.play(Indicate(concurrency[2][23:25]))
        self.play(Circumscribe(concurrency[2][5:16]))
        expected = Code('expected.txt', insert_line_no=False).shift(RIGHT*4, UP*3)
        self.play(Write(expected))
        result1 = Code('result1.txt', insert_line_no=False).scale(.8).next_to(expected, DOWN)
        result2 = Code('result2.txt', insert_line_no=False).scale(.8).next_to(result1, DOWN)
        self.play(Create(VGroup(result1, result2)))
        self.play(Indicate(result1[2][-1]), Indicate(result2[2][-1]))
        asm = Code('counter_asm.s', style=Code.styles_list[9]).shift(RIGHT*4.5)
        self.play(FadeOut(expected, result1, result2),
                  ReplacementTransform(concurrency[2][11].copy(), asm))
        self.clear()

        cur_counter = Text('counter = 50', color=BLUE).shift(UP*2)
        updated_counter = Text('counter = 51', color=BLUE).shift(UP*2)
        thread_a = VGroup(Text('线程A', color=BLUE_B).scale(.8), asm[2].copy().scale(1.5),
                          Text('%eax = 51', color=BLUE).scale(.8)).arrange(DOWN)
        thread_b = VGroup(Text('线程B', color=BLUE_B).scale(.8), asm[2].copy().scale(1.5), thread_a[2].copy()
                          ).arrange(DOWN)
        VGroup(thread_a, thread_b).arrange(RIGHT, buff=1).next_to(cur_counter, DOWN, buff=1)
        t_pointer = Triangle(stroke_width=0, fill_color=YELLOW, fill_opacity=1
                             ).scale(.2).next_to(thread_a, UP).rotate(PI)
        self.play(Write(cur_counter))
        self.play(Create(VGroup(t_pointer, thread_a[0], thread_a[1][:2], thread_a[2])))
        self.play(t_pointer.animate.next_to(thread_b, UP), Create(thread_b[:2]))
        self.play(Indicate(cur_counter))
        self.play(Write(thread_b[2]))
        self.play(FadeOut(cur_counter), ReplacementTransform(thread_b[2], updated_counter))
        self.play(t_pointer.animate.next_to(thread_a, UP))
        self.play(Write(thread_a[1][2]), ReplacementTransform(thread_a[2], updated_counter))
        self.play(Write(Text('critical section(临界区)'
                             ).set_color_by_gradient(BLUE_A, BLUE_E).next_to(VGroup(thread_a, thread_b), DOWN, buff=1)))
        self.wait()


class Lock(Scene):
    def construct(self):
        critical_section = VGroup(Rectangle(width=3, height=1, fill_color=BLUE, fill_opacity=.5))
        critical_section.add(Text('临界区').scale(.8).next_to(critical_section, UP))
        thread1 = VGroup(Rectangle(width=2, height=.8, fill_color=BLUE_E, fill_opacity=.8)).move_to(critical_section[0])
        thread1.add(Text('线程1').scale(.8).move_to(thread1))
        thread2 = VGroup(Rectangle(width=2, height=.8, fill_color=BLUE_E, fill_opacity=.8)
                         ).next_to(critical_section[0], RIGHT, buff=1)
        thread2.add(Text('线程2').scale(.8).move_to(thread2))
        self.play(Create(VGroup(critical_section, thread1)))
        self.play(Create(thread2))
        lock = ImageMobject('lock.PNG').scale(.2).next_to(critical_section, DOWN)
        unlock = ImageMobject('unlock.PNG').scale(.2).next_to(critical_section, DOWN)
        self.play(FadeIn(lock))
        self.play(FadeOut(thread1, lock), FadeIn(unlock))
        self.play(thread2.animate.move_to(critical_section[0]))
        self.clear()

        self.play(Create(Code('disable_interrupt.c', style=Code.styles_list[9])))
        self.wait()
        self.clear()

        flag = Code('flag.c', style=Code.styles_list[9]).scale(.8)
        flag_init = Text('flag = 0', color=BLUE)
        thread1_eg = VGroup(Text('线程1', color=BLUE_B).scale(.8), flag[2][8:11].copy().scale(1.2)).arrange(DOWN)
        thread2_eg = VGroup(Text('线程2', color=BLUE_B).scale(.8), flag[2][8:11].copy().scale(1.2)).arrange(DOWN)
        bug = VGroup(flag_init, VGroup(thread1_eg, thread2_eg).arrange(RIGHT)).arrange(DOWN, buff=1)
        VGroup(flag, bug).arrange(RIGHT)
        pointer = Triangle(stroke_width=0, fill_color=YELLOW, fill_opacity=1
                           ).scale(.2).next_to(thread1_eg, UP).rotate(PI)
        self.play(Create(flag))
        self.play(Write(flag_init))
        self.play(Create(VGroup(pointer, thread1_eg[0])))
        self.play(Circumscribe(flag[2][7:12]))
        self.play(Write(thread1_eg[1][0]))
        self.play(pointer.animate.next_to(thread2_eg, UP), Create(thread2_eg))
        self.play(Indicate(flag_init))
        updated_flag = Text('flag = 1', color=BLUE).move_to(flag_init)
        self.play(ReplacementTransform(thread2_eg[1][2].copy(), updated_flag), FadeOut(flag_init))
        self.play(pointer.animate.next_to(thread1_eg, UP))
        self.play(Write(thread1_eg[1][1:]))
        self.play(ReplacementTransform(thread1_eg[1][2].copy(), updated_flag))
        self.clear()

        test_set = Code('test_set.c', style=Code.styles_list[9]).scale(.8)
        test_set_lock = Code('test_set_lock.c', style=Code.styles_list[9]).scale(.8)
        VGroup(test_set, test_set_lock).arrange(RIGHT)
        self.play(Create(test_set))
        self.play(Create(test_set_lock))
        self.play(Create(SurroundingRectangle(test_set_lock[2][9:13])))
        self.clear()

        thread100 = VGroup(Rectangle(width=2, height=.8, fill_color=BLUE_E, fill_opacity=.8))
        thread100.add(Text('线程100').scale(.8).move_to(thread100))
        time_slices = VGroup(Rectangle(width=.2, height=1.5, fill_color=BLUE, fill_opacity=.8),
                             Rectangle(width=4, height=1.5, fill_color=BLUE_E, fill_opacity=.8)).arrange(RIGHT, buff=0)
        time_slices.add(Brace(time_slices[1], DOWN))
        time_slices.add(Text('等待').scale(.8).next_to(time_slices[2], DOWN))
        waiting_threads = VGroup(thread2, Text('...'), thread100).arrange(RIGHT)
        eg = VGroup(VGroup(critical_section, thread1.move_to(critical_section[0])), waiting_threads, time_slices
                    ).arrange(DOWN)
        self.play(Create(eg[:2]))
        self.play(Create(eg[2][:2]))
        self.play(Indicate(eg[2][0], color=BLUE))
        self.play(Create(eg[2][2:]))
        self.clear()

        solaris_call = VGroup(Text('park()').set_color_by_gradient(BLUE_A, BLUE_E),
                              Text('unpark()').set_color_by_gradient(BLUE_A, BLUE_E)).arrange(DOWN)
        self.play(Write(solaris_call[0]))
        self.play(Write(solaris_call[1]))
        self.clear()

        solaris_lock = Code('solaris_lock.c', style=Code.styles_list[9]).scale(.6)
        self.play(Create(solaris_lock))
        guard = ImageMobject('guard.PNG').next_to(solaris_lock[2][2], RIGHT, buff=1).scale(.3)
        self.play(Indicate(solaris_lock[2][2]), FadeIn(guard))
        self.play(Circumscribe(solaris_lock[2][13:15]), Circumscribe(solaris_lock[2][26:28]))
        self.play(FadeOut(guard))
        c_pointer = Triangle(color=ORANGE, fill_color=ORANGE, fill_opacity=1
                             ).rotate(PI*(3/2)).scale(0.1).next_to(solaris_lock[2][15], LEFT, buff=.1)
        self.play(Create(c_pointer))
        lines = [16, 17, 19, 20, 21, 28, 29, 32, 31]
        for line in lines:
            self.play(c_pointer.animate.next_to(solaris_lock[2][line], LEFT, buff=.1))
        lock_trans = VGroup(thread1, thread2
                            ).arrange(DOWN, buff=1).next_to(solaris_lock[2][31], RIGHT).shift(UP*1.5, RIGHT*.5)
        lock.scale(.8).next_to(thread1, DOWN, buff=.1)
        lock_c = lock.copy().next_to(thread2, DOWN, buff=.1)
        self.play(Create(lock_trans), FadeIn(lock))
        self.play(FadeOut(lock), FadeIn(lock_c))
        self.play(FadeOut(lock_trans, lock_c))
        self.play(Circumscribe(solaris_lock[2][13:15]), Circumscribe(solaris_lock[2][26:28]))
        self.play(Circumscribe(solaris_lock[2][15:22]), Circumscribe(solaris_lock[2][28:32]))
        self.play(Circumscribe(solaris_lock[2][20:22]))
        race = VGroup(VGroup(thread1, Text('park();').scale(.5), Tex('$Z^{Z^{Z}}$')).arrange(DOWN), thread2
                      ).arrange(DOWN).next_to(solaris_lock[2][20:22], RIGHT, buff=4)
        pointer.next_to(thread1, UP)
        self.play(Create(VGroup(pointer, race[0][0])))
        lock.next_to(thread2, DOWN)
        unlock.scale(.8).next_to(thread2, DOWN)
        self.play(pointer.animate.next_to(thread2, UP), Create(thread2), FadeIn(lock))
        self.play(FadeOut(lock), FadeIn(unlock))
        self.play(pointer.animate.next_to(thread1, UP), Create(race[0][1:]))
        setpark = VGroup(Elbow().rotate(3/4*PI).next_to(solaris_lock[2][19], RIGHT, buff=0).shift(DOWN*.2))
        setpark.add(Text('setpark();').scale(.4).next_to(setpark, RIGHT, buff=0))
        self.play(Create(setpark))
        return_txt = Text('返回').scale(.7).move_to(race[0][2])
        self.play(ReplacementTransform(race[0][2], return_txt))
        self.play(FadeOut(race[0][:2], thread2, unlock, return_txt, pointer))
        self.wait()


class Condition(Scene):
    def construct(self):
        # def pointer_move(code, move):
        #     for line in move:
        #         self.play(c_pointer.animate.next_to(code[2][line], LEFT, buff=.1))
        #
        # parent_child = Code('parent_child.c', style=Code.styles_list[9])
        # self.play(Create(parent_child))
        # self.play(Indicate(parent_child[2][2]), Indicate(parent_child[2][10]))
        # line_ref3 = Dot(parent_child[2][1].get_left()+DOWN*.4)
        # line_ref11 = Dot(parent_child[2][10].get_left()+DOWN*.1)
        # self.play(ReplacementTransform(parent_child[2][2],
        #                                Code(code='done = 1', style=Code.styles_list[9], language='c'
        #                                     )[2].next_to(line_ref3, RIGHT, buff=-.1)),
        #           ReplacementTransform(parent_child[2][10],
        #                                Code(code='while(done == 0); // spin', style=Code.styles_list[9], language='c'
        #                                     )[2].next_to(line_ref11, RIGHT, buff=-.1)))
        # self.wait()
        # self.clear()
        #
        # cv = Code('cv.c', style=Code.styles_list[9]).scale(.6)
        # cv_txt = Text('条件变量').scale(.8).set_color_by_gradient(BLUE_A, BLUE_E).next_to(cv[2][2], RIGHT, buff=1)
        # self.play(Create(cv))
        # self.play(Indicate(cv[2][2]), Write(cv_txt))
        # self.play(FadeOut(cv_txt))
        # self.play(Indicate(cv[2][7]), Indicate(cv[2][20]))
        # self.play(Indicate(cv[2][20]))
        # self.play(Indicate(cv[2][7]))
        # self.play(Indicate(cv[2][0]))
        # c_pointer = Triangle(color=ORANGE, fill_color=ORANGE, fill_opacity=1
        #                      ).rotate(PI*(3/2)).scale(0.1).next_to(cv[2][19], LEFT, buff=.1)
        # self.play(Create(c_pointer))
        # pointer_move(cv, [20, 6, 7])
        # self.clear()
        #
        producer_consumer = Text('生产者/消费者问题').set_color_by_gradient(BLUE_A, BLUE_E).shift(UP*3)
        buffer = VGroup(Rectangle(width=1.5, height=1, stroke_color=BLUE).next_to(producer_consumer, DOWN, buff=1))
        buffer.add(Text('存储器', color=BLUE).scale(.6).move_to(buffer))
        producer = ImageMobject('producer.png').scale(1.2).next_to(buffer, DOWN, buff=.5).shift(LEFT)
        consumer = ImageMobject('consumer.png').scale(1.2).next_to(buffer, DOWN, buff=.5).shift(RIGHT)
        # data = VGroup(Rectangle(width=1.5, height=1, fill_color=BLUE, fill_opacity=1, stroke_width=0)
        #               ).next_to(producer, DOWN)
        # data.add(Text('数据').scale(.8).move_to(data))
        # http = VGroup(Rectangle(width=1.5, height=1, fill_color=BLUE, fill_opacity=1, stroke_width=0)
        #               ).next_to(producer, DOWN)
        # http.add(Text('HTTP').scale(.8).move_to(http))
        # self.play(Write(producer_consumer), Create(buffer), FadeIn(producer, consumer))
        # self.play(Create(data))
        # self.play(data.animate.move_to(buffer))
        # self.play(data.animate.next_to(consumer, DOWN))
        # self.play(FadeOut(data))
        # buffer.add(Text('工作列表', color=BLUE).scale(.5).move_to(buffer))
        # self.play(Create(http), FadeIn(buffer[-1]), FadeOut(buffer[1]))
        # self.play(http.animate.move_to(buffer))
        # self.play(http.animate.next_to(consumer, DOWN))
        # self.play(FadeOut(http))
        # buffer.add(Text('int', color=BLUE).scale(.8).move_to(buffer))
        # self.play(FadeOut(buffer[-2]), FadeIn(buffer[-1]))
        integer = VGroup(Rectangle(width=1.5, height=1, fill_color=BLUE, fill_opacity=1, stroke_width=0)
                         ).move_to(buffer)
        integer.add(Text('int').scale(.8).move_to(integer))
        # self.play(Create(integer))
        # self.play(integer.animate.next_to(consumer, DOWN))
        # self.play(FadeOut(integer))
        # self.play(Create(integer.next_to(producer, DOWN)))
        # self.play(integer.animate.move_to(buffer))
        # self.clear()
        #
        # put_get = Code('put_get.c', style=Code.styles_list[9])
        # self.play(Create(VGroup(put_get[:2], put_get[2][:2])))
        # self.play(Create(put_get[2][3:8]))
        # self.play(Create(c_pointer.next_to(put_get[2][4], LEFT, buff=.1)))
        # pointer_move(put_get, [5, 6])
        # self.play(Create(put_get[2][9:]))
        # pointer_move(put_get, [10, 11, 12])
        # self.clear()
        #
        producer_consumer = Code('producer_consumer.c', style=Code.styles_list[9]).scale(.7)
        # self.play(Create(producer_consumer))
        # self.play(Circumscribe(producer_consumer[2][4:13]))
        # self.play(Indicate(producer_consumer[2][6]), Indicate(producer_consumer[2][11]))
        # self.play(Create(c_pointer.next_to(producer_consumer[2][7], LEFT, buff=.1)))
        # pointer_move(producer_consumer, [8, 9, 10])
        # self.play(Indicate(producer_consumer[2][18]), Indicate(producer_consumer[2][23]))
        # pointer_move(producer_consumer, [19, 20, 21, 22])
        # self.clear()

        v2 = Code('producer_consumer_v2.c', style=Code.styles_list[9]).scale(.7)
        t_producer = VGroup(producer_consumer[2][9:11].copy(),
                            producer_consumer[2][8].copy()).arrange(DOWN)
        t_consumer1 = VGroup(producer_consumer[2][20].copy(), v2[2][19:21].copy()).arrange(DOWN)
        t_consumer2 = VGroup(producer_consumer[2][21:23].copy(), producer_consumer[2][20].copy()).arrange(DOWN)
        t_consumer1.shift(DOWN*2)
        t_producer.next_to(t_consumer1, LEFT)
        t_consumer2.next_to(t_consumer1, RIGHT, buff=1)
        consumer1 = consumer.next_to(t_consumer1, UP)
        t_pointer = Triangle(stroke_width=0, fill_color=YELLOW, fill_opacity=1
                             ).scale(.2).next_to(consumer1, UP).rotate(PI)
        self.play(Create(t_pointer), FadeIn(consumer1))
        self.play(Create(buffer[:2].next_to(t_pointer, UP, buff=1)))
        self.play(Create(t_consumer1[0]))
        producer.next_to(t_producer, UP)
        self.play(t_pointer.animate.next_to(producer, UP), FadeIn(producer))
        self.play(Create(VGroup(t_producer[0][0], integer.move_to(buffer))))
        self.play(Create(VGroup(t_producer[0][1], t_producer[1])))
        consumer2 = consumer.copy().next_to(t_consumer2, UP)
        self.play(t_pointer.animate.next_to(consumer2, UP), FadeIn(consumer2))
        self.play(ReplacementTransform(integer, t_consumer2[0][0]))
        self.play(t_pointer.animate.next_to(consumer1, UP))
        self.play(Indicate(buffer[:2], color=BLUE))
        self.clear()
        self.play(Create(v2))
        self.play(Indicate(v2[2][7]), Indicate(v2[2][19]))
        self.clear()
        self.play(FadeIn(producer, consumer1, consumer2, buffer[:2], t_producer, t_consumer1[0], t_consumer2[0][0]))
        self.play(Create(t_consumer1[1]))
        self.play(FadeOut(t_producer, t_consumer1, t_consumer2[0][0]))
        consumer1_zzz = ImageMobject('sleeping.png').scale(.1).next_to(consumer1, UR, buff=-.3)
        self.add(consumer1_zzz, ImageMobject('sleeping.png').scale(.1).next_to(producer, UR, buff=-.3))
        self.play(Create(VGroup(t_pointer.next_to(consumer2, UP), t_consumer2[0])))
        self.play(FadeOut(consumer1_zzz))
        self.play(Create(t_consumer2[1]), FadeIn(ImageMobject('sleeping.png').scale(.1).move_to(consumer2, UR)))
        self.play(t_pointer.animate.next_to(consumer1, UP), Create(t_consumer1[0]), FadeIn(consumer1_zzz))
        self.clear()

        # v3 = Code('producer_consumer_v3.c', style=Code.styles_list[9]).scale(.7)
        # self.play(Create(v3))
        # self.play(Succession(Indicate(v3[2][0]), Indicate(v3[2][8]), Indicate(v3[2][20]),
        #                      Indicate(v3[2][10]), Indicate(v3[2][22])))
        # self.clear()
        #
        # put_get_array = Code('put_get_array.c', style=Code.styles_list[9])
        # self.play(Create(VGroup(put_get_array[:2], put_get_array[2][:4])))
        # self.play(Indicate(put_get_array[2][0][-5:-2]))
        # self.play(Create(put_get_array[2][4:]))
        # self.play(Circumscribe(put_get_array[2][5:10]))
        # self.play(Circumscribe(put_get_array[2][11:17]))
        # self.clear()
        #
        # producer_consumer_array = Code('producer_consumer_array.c', style=Code.styles_list[9]).scale(.7)
        # self.play(Create(producer_consumer_array))
        # self.play(Indicate(producer_consumer_array[2][7]))
        # self.wait()


class Semaphore(Scene):
    def construct(self):
        def sem_change(num):
            self.play(Transform(sem[1], Text(str(num), color=BLUE).move_to(sem[1])))

        self.play(Write(Text('信号量（Semaphore）').set_color_by_gradient(BLUE_A, BLUE_E).shift(UP*2)))
        wait_post = VGroup(Text('sem_wat()', color=BLUE),
                           Text('sem_post()', color=BLUE)).shift(UP*.5).arrange(RIGHT, buff=.5)
        self.play(Create(wait_post))
        pv = VGroup(Text('P()').scale(.8).next_to(wait_post[0], DOWN),
                    Text('V()').scale(.8).next_to(wait_post[1], DOWN)).next_to(wait_post, DOWN)
        self.play(Create(pv))
        self.play(Create(VGroup(Text('Passenren').scale(.8).next_to(pv[0], DOWN),
                                Text('Verhoog').scale(.8).next_to(pv[1], DOWN)).next_to(pv, DOWN)))
        self.play(FadeIn(ImageMobject('Dijkstra.jpg').scale(.5).shift(RIGHT*5.5, DOWN*.5)))
        self.clear()

        sem_lock = Code('sem_lock.c', style=Code.styles_list[9])
        sem = VGroup(Text('sem=', color=BLUE), Text('1', color=BLUE)).arrange(RIGHT)
        VGroup(sem_lock, sem).arrange(RIGHT, buff=1)
        self.play(Write(sem_lock), Write(sem))
        self.play(Indicate(sem_lock[2][1][-3]))
        self.play(Indicate(sem_lock[2][1][-6]))
        self.play(Indicate(sem_lock[2][3]))
        thread1 = VGroup(Rectangle(width=2, height=.8, fill_color=BLUE_E, fill_opacity=.8)).next_to(sem, UP)
        thread1.add(Text('线程1').scale(.8).move_to(thread1))
        thread2 = VGroup(Rectangle(width=2, height=.8, fill_color=BLUE_E, fill_opacity=.8)).next_to(sem, DOWN)
        thread2.add(Text('线程2').scale(.8).move_to(thread2))
        self.play(Transform(sem[1], Text('0', color=BLUE).move_to(sem[1])), Create(thread1))
        self.play(Transform(sem[1], Text('-1', color=BLUE).move_to(sem[1])), Create(thread2))
        t2_zzz = ImageMobject('sleeping.png').scale(.1).next_to(thread2, RIGHT)
        self.play(FadeIn(t2_zzz))
        self.play(Indicate(sem_lock[2][5]))
        self.play(Transform(sem[1], Text('0', color=BLUE).move_to(sem[1])), FadeOut(t2_zzz))
        self.clear()

        sem_cv = Code('sem_cv.c', style=Code.styles_list[9])
        VGroup(sem_cv, sem).arrange(RIGHT, buff=1)
        father = VGroup(Rectangle(width=2, height=.8, fill_color=BLUE_E, fill_opacity=.8)).next_to(sem, UP)
        father.add(Text('父线程').scale(.8).move_to(father))
        child = VGroup(Rectangle(width=2, height=.8, fill_color=BLUE_E, fill_opacity=.8)).next_to(sem, DOWN)
        child.add(Text('子线程').scale(.8).move_to(child))
        self.play(Create(VGroup(sem_cv, sem)))
        self.play(Create(father), Indicate(sem_cv[2][15]))
        self.play(Transform(sem[1], Text('-1', color=BLUE).move_to(sem[1])))
        father_zzz = ImageMobject('sleeping.png').scale(.1).next_to(father, RIGHT)
        self.play(FadeIn(father_zzz))
        self.play(Create(child), Indicate(sem_cv[2][5]))
        sem_change(0)
        self.play(FadeOut(father_zzz))
        sem_change(1)
        self.play(Indicate(sem_cv[2][15]))
        sem_change(0)
        self.clear()

        pc_sem = Code('producer_consumer_sem.c', style=Code.styles_list[9]).scale(.6)
        self.play(Create(pc_sem))
        self.play(Indicate(pc_sem[2][-3]))
        self.play(Indicate(VGroup(pc_sem[2][7], pc_sem[2][11], pc_sem[2][18], pc_sem[2][22])))
        self.play(Indicate(pc_sem[2][-5:-3]))
        self.clear()

        buffer = VGroup(Rectangle(width=1.5, height=1, stroke_color=BLUE).shift(UP*2))
        buffer.add(Text('存储器', color=BLUE).scale(.6).move_to(buffer))
        consumer = ImageMobject('consumer.png').scale(1.2).shift(LEFT)
        producer = ImageMobject('producer.png').scale(1.2).shift(RIGHT)
        lock = ImageMobject('lock.PNG').scale(.15).next_to(consumer, DOWN)
        consumer_zzz = ImageMobject('sleeping.png').scale(.1).next_to(consumer, UR, buff=-.3)
        self.play(FadeIn(consumer, lock))
        self.play(Create(buffer))
        self.play(FadeIn(consumer_zzz))
        self.play(FadeIn(producer))
        self.play(Create(Arrow([.6, 0, 0], [-.8, -1.2, 0], color=BLUE)))
        self.play(Write(Text('死锁').set_color_by_gradient(BLUE_A, BLUE_E).shift(DOWN*2.5)))
        self.clear()

        self.play(Create(pc_sem))
        dist = .2
        self.play(VGroup(pc_sem[2][7], pc_sem[2][10], pc_sem[2][18], pc_sem[2][21]).animate.shift(DOWN*dist),
                  VGroup(pc_sem[2][8], pc_sem[2][11], pc_sem[2][19], pc_sem[2][22]).animate.shift(UP*dist))
        self.clear()

        reader = ImageMobject('reader.png').scale(1.2).shift(LEFT)
        writer = ImageMobject('writer.png').scale(1.2).shift(RIGHT)
        self.play(Write(Text('读者/写者问题').set_color_by_gradient(BLUE_A, BLUE_E).shift(UP*2)),
                  FadeIn(reader, writer))
        self.play(FadeIn(reader.copy().shift(LEFT), reader.copy().shift(LEFT*2)))
        self.clear()

        reader_writer = Code('reader_writer.c', style=Code.styles_list[9]).scale(.6)
        self.play(Create(reader_writer))
        self.play(Indicate(reader_writer[2][3]))
        self.play(Indicate(reader_writer[2][15:17]))
        self.play(Indicate(reader_writer[2][23:25]))
        self.clear()

        self.play(Write(Text('哲学家进餐问题').set_color_by_gradient(BLUE_A, BLUE_E).shift(UP*3)))
        table = Circle(1.5, stroke_width=0, fill_color=BLUE_A, fill_opacity=.8)
        philosophers = VGroup()
        for index in range(5):
            philosopher = VGroup(Circle(.5, stroke_width=0, fill_color=BLUE, fill_opacity=.8)
                                 ).move_to([2*math.sin(index*2*PI/5), 2*math.cos(index*2*PI/5), 0])
            philosopher.add(Text('p'+str(index)).scale(.5).move_to(philosopher))
            philosophers.add(philosopher)
        philosopher_code = Code('philosopher.c', style=Code.styles_list[9]).next_to(table, RIGHT, buff=1)
        self.play(Create(VGroup(table, philosophers)))
        self.play(Create(VGroup(philosopher_code[:2], philosopher_code[2][:2], philosopher_code[2][-1])))
        self.play(Create(philosopher_code[2][3]))
        chopsticks = VGroup()
        for index in range(5):
            chopsticks.add(Line(UR*.3, DL*.3, color=BLUE_E, stroke_width=10
                                ).move_to([2*math.sin((2*index+1)*PI/5), 2*math.cos((2*index+1)*PI/5), 0]))
        self.play(Create(chopsticks))
        self.play(Succession(Create(philosopher_code[2][2]), Create(philosopher_code[2][4])))
        self.play(Indicate(VGroup(philosopher_code[2][2], philosopher_code[2][4])))
        self.play(FadeOut(philosopher_code))
        solution = Code('philosopher_attempt.c', style=Code.styles_list[9]).scale(.8).next_to(table, RIGHT, buff=1)
        self.play(Create(VGroup(solution[:2], solution[2][:4])))
        self.play(Create(solution[2][4:]))
        self.play(chopsticks[0].animate.move_to(philosophers[0]), chopsticks[1].animate.move_to(philosophers[1]),
                  chopsticks[2].animate.move_to(philosophers[2]), chopsticks[3].animate.move_to(philosophers[3]),
                  chopsticks[4].animate.move_to(philosophers[4]))
        dead_circle = VGroup()
        for index in range(5):
            dead_circle.add(Arrow(philosophers[index], philosophers[(index-1) % 5]))
        self.play(Create(dead_circle))
        self.play(FadeOut(solution))
        modify = Code('philosopher_solution.c', style=Code.styles_list[9]).next_to(table, RIGHT, buff=.5).scale(.8)
        self.play(Create(modify))
        self.wait()


class DeadLock(Scene):
    def construct(self):
        deadlock_cond = VGroup(Text('1. 互斥\n'), Text('2. 持有并等待\n'), Text('3. 非抢占\n'), Text('4. 循环等待')
                               ).arrange(DOWN)
        for index in range(4):
            deadlock_cond[index][:2].set(color=BLUE)
        for cond in deadlock_cond:
            self.play(Write(cond))
        dead_circle = VGroup()
        for index in range(5):
            dead_circle.add(VGroup(Circle(.5, stroke_width=0, fill_color=BLUE, fill_opacity=.8),
                                   Line(UR*.3, DL*.3, color=BLUE_E, stroke_width=10)
                                   ).move_to([2*math.sin(index*2*PI/5), 2*math.cos(index*2*PI/5), 0]))
        for index in range(5):
            dead_circle.add(Arrow(dead_circle[index], dead_circle[(index-1) % 5]))
        dead_circle.next_to(deadlock_cond)
        self.play(Create(dead_circle))
        self.play(FadeToColor(deadlock_cond[3], GREY),
                  Create(Line(ORIGIN, RIGHT*4, color=GREY).move_to(deadlock_cond[3])))
        self.play(FadeOut(dead_circle[5]))
        self.play(FadeOut(dead_circle[:5], dead_circle[6:]))
        self.play(FadeToColor(deadlock_cond[1], GREY),
                  Create(Line(ORIGIN, RIGHT*5, color=GREY).move_to(deadlock_cond[1])))
        no_hold_wait = Code('no_hold_wait.c', style=Code.styles_list[9]).next_to(deadlock_cond)
        self.play(Create(no_hold_wait))
        self.play(FadeOut(no_hold_wait))
        self.play(FadeToColor(deadlock_cond[2], GREY),
                  Create(Line(ORIGIN, RIGHT*3, color=GREY).move_to(deadlock_cond[2])))
        try_lock = Code('trylock.c', style=Code.styles_list[9]).next_to(deadlock_cond)
        self.play(Create(try_lock))
        self.play(FadeOut(try_lock))
        self.clear()

        deadlock_avoid = Text('死锁避免').set_color_by_gradient(BLUE_A, BLUE_E)
        thread_lock = Table([['是', '是', '否', '否'], ['是', '是', '是', '否']],
                            row_labels=[Text('L1'), Text('L2')],
                            col_labels=[Text('T1'), Text('T2'), Text('T3'), Text('T4')]).scale(.7)
        thread_lock.get_row_labels().set(color=BLUE_A)
        thread_lock.get_col_labels().set(color=BLUE)
        t1 = VGroup(Rectangle(width=1.8, height=.5, fill_color=BLUE_E, fill_opacity=.8))
        t2 = VGroup(Rectangle(width=1, height=.5, fill_color=BLUE_B, fill_opacity=.8))
        t3 = VGroup(Rectangle(width=1, height=.5, fill_color=BLUE_D, fill_opacity=.8))
        t4 = VGroup(Rectangle(width=1.5, height=.5, fill_color=BLUE_C, fill_opacity=.8))
        t1.add(Text('T1').scale(.5).move_to(t1))
        t2.add(Text('T2').scale(.5).move_to(t2))
        t3.add(Text('T3').scale(.5).move_to(t3))
        t4.add(Text('T4').scale(.5).move_to(t4))
        schedule1 = VGroup(Text('CPU1').scale(.7), VGroup(t3, t4).arrange(RIGHT, buff=0),
                           Text('CPU2').scale(.7), VGroup(t1, t2).arrange(RIGHT, buff=0))
        VGroup(schedule1[0], schedule1[2]).arrange(DOWN)
        schedule1[1].next_to(schedule1[0], RIGHT)
        schedule1[3].next_to(schedule1[2], RIGHT)
        VGroup(deadlock_avoid, thread_lock, schedule1).arrange(DOWN)
        self.play(Write(deadlock_avoid))
        self.play(Create(thread_lock))
        self.play(Create(schedule1))
        self.play(FadeOut(schedule1))
        self.play(Transform(thread_lock.get_entries((2, 4)),
                            Text('是').scale(.7).move_to(thread_lock.get_entries((2, 4)))))
        schedule2 = VGroup(Text('CPU1').scale(.7), t4,
                           Text('CPU2').scale(.7), VGroup(t1, t2, t3).arrange(RIGHT, buff=0))
        VGroup(schedule2[0], schedule2[2]).arrange(DOWN)
        schedule2[1].next_to(schedule2[0], RIGHT)
        schedule2[3].next_to(schedule2[2], RIGHT)
        schedule2.next_to(thread_lock, DOWN)
        self.play(Create(schedule2))
        self.clear()

        self.play(Write(Text('死锁检测及恢复').set_color_by_gradient(BLUE_A, BLUE_E)))
        self.wait()


class Patch(Scene):
    def construct(self):
        concurrency = Code('concurrency.c', style=Code.styles_list[9]).scale(.75).shift(LEFT * 2.5)
        self.play(Create(concurrency))
        expected = Code('expected.txt', insert_line_no=False).shift(RIGHT * 4, UP * 3)
        self.play(Write(expected))
        result1 = Code('result1.txt', insert_line_no=False).scale(.8).next_to(expected, DOWN)
        result2 = Code('result2.txt', insert_line_no=False).scale(.8).next_to(result1, DOWN)
        self.play(Create(VGroup(result1, result2)))
        self.play(Indicate(result1[2][-1]), Indicate(result2[2][-1]))
        self.clear()

        solaris_call = VGroup(Text('park()').set_color_by_gradient(BLUE_A, BLUE_E),
                              Text('unpark(threadID)').set_color_by_gradient(BLUE_A, BLUE_E)).arrange(DOWN)
        self.play(Write(solaris_call[0]))
        self.play(Write(solaris_call[1]))
        self.clear()

        self.play(Write(Text('信号量（Semaphore）').set_color_by_gradient(BLUE_A, BLUE_E).shift(UP * 2)))
        wait_post = VGroup(Text('sem_wait()', color=BLUE),
                           Text('sem_post()', color=BLUE)).shift(UP * .5).arrange(RIGHT, buff=.5)
        self.play(Create(wait_post))
        pv = VGroup(Text('P()').scale(.8).next_to(wait_post[0], DOWN),
                    Text('V()').scale(.8).next_to(wait_post[1], DOWN)).next_to(wait_post, DOWN)
        self.play(Create(pv))
        self.play(Create(VGroup(Text('Passenren').scale(.8).next_to(pv[0], DOWN),
                                Text('Verhoog').scale(.8).next_to(pv[1], DOWN)).next_to(pv, DOWN)))
        self.play(FadeIn(ImageMobject('Dijkstra.jpg').scale(.5).shift(RIGHT * 5.5, DOWN * .5)))
        self.clear()

        self.wait()
