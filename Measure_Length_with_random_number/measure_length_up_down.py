from manim import *
import random

class RandomLineMeasurement(Scene):
    def construct(self):
        # Title
        title = Text("Measuring Length\nwith Random Numbers", font_size=48, weight=BOLD, gradient=(BLUE, GREEN), line_spacing=1.2)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.wait(0.5)
        
        # The line to measure (6 cm)
        true_length = 6
        ruler_length = 10
        
        # Scale factor for visualization
        scale = 0.8
        
        # Draw the line
        line_to_measure = Line(
            LEFT * true_length * scale / 2,
            RIGHT * true_length * scale / 2,
            color=RED,
            stroke_width=8
        ).shift(UP * 0.5)
        
        line_label = Text(f"Line to be measured (? cm)", font_size=32, color=RED)
        line_label.next_to(line_to_measure, UP, buff=0.3)
        
        self.play(Create(line_to_measure), Write(line_label))
        self.wait(0.5)
        
        # Draw the ruler (10 cm)
        ruler = Line(
            LEFT * ruler_length * scale / 2,
            RIGHT * ruler_length * scale / 2,
            color=YELLOW,
            stroke_width=6
        ).shift(DOWN * 0.5)
        
        # Ruler markings
        ruler_marks = VGroup()
        ruler_numbers = VGroup()
        for i in range(ruler_length + 1):
            x_pos = LEFT * ruler_length * scale / 2 + RIGHT * i * scale
            mark = Line(UP * 0.1, DOWN * 0.1, color=YELLOW, stroke_width=2).move_to(ruler.get_center() + x_pos)
            ruler_marks.add(mark)
            
            if i % 1 == 0:  # Show every cm
                num = Text(str(i), font_size=20, color=YELLOW)
                num.next_to(mark, DOWN, buff=0.15)
                ruler_numbers.add(num)
        
        ruler_label = Text("10 cm ruler", font_size=28, color=YELLOW)
        ruler_label.next_to(ruler, DOWN, buff=0.8)
        
        self.play(
            Create(ruler),
            Create(ruler_marks),
            Write(ruler_numbers),
            Write(ruler_label)
        )
        self.wait(1)
        
        # Explanation
        explanation = Text(
            "Generate random numbers between 0 and 10\nCount how many fall within the line",
            font_size=28,
            line_spacing=1.2,
            color=PURPLE
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(2)
        
        # Fade out for next slide
        self.play(
            FadeOut(line_to_measure),
            FadeOut(line_label),
            FadeOut(ruler),
            FadeOut(ruler_marks),
            FadeOut(ruler_numbers),
            FadeOut(ruler_label),
            FadeOut(explanation),
            FadeOut(title)
        )
        self.wait(0.5)
        
        # ========== SIMULATION SLIDE ==========
        
        # Setup for simulation
        # Line on top (horizontal orientation)
        line_width = 6
        sim_line = Line(
            LEFT * true_length / ruler_length * line_width / 2,
            RIGHT * true_length / ruler_length * line_width / 2,
            color=RED,
            stroke_width=10
        ).shift(UP * 2.5)
        
        # Ruler scale on top
        ruler_scale = Line(
            LEFT * line_width / 2,
            RIGHT * line_width / 2,
            color=YELLOW,
            stroke_width=4
        ).shift(UP * 3)
        
        ruler_scale_marks = VGroup()
        for i in range(11):
            x_pos = LEFT * line_width / 2 + RIGHT * i / 10 * line_width
            mark = Line(UP * 0.1, DOWN * 0.1, color=YELLOW, stroke_width=2).move_to(ruler_scale.get_center() + x_pos)
            ruler_scale_marks.add(mark)
            
            if i % 2 == 0:
                num = Text(str(i), font_size=18, color=YELLOW)
                num.next_to(mark, UP, buff=0.15)
                ruler_scale_marks.add(num)
        
        # Plot on the bottom
        axes = Axes(
            x_range=[0, 1000, 200],
            y_range=[0, 10, 2],
            x_length=7,
            y_length=3,
            axis_config={"color": BLUE, "include_tip": True},
            x_axis_config={"numbers_to_include": [0, 200, 400, 600, 800, 1000]},
            y_axis_config={"numbers_to_include": [0, 2, 4, 6, 8, 10]},
        ).shift(DOWN * 1.5)
        
        axes_labels = axes.get_axis_labels(
            x_label=Text("Number of Samples", font_size=20),
            y_label=Text("Estimated Length (cm)", font_size=20)
        )
        
        # True length reference line
        true_line = DashedLine(
            axes.c2p(0, true_length),
            axes.c2p(1000, true_length),
            color=GREEN,
            stroke_width=3
        )
        true_label = Text(f"True: {true_length} cm", font_size=18, color=GREEN)
        true_label.next_to(true_line, RIGHT, buff=0.1)
        
        self.play(
            Create(sim_line),
            Create(ruler_scale),
            Create(ruler_scale_marks),
            Create(axes),
            Write(axes_labels),
            Create(true_line),
            Write(true_label)
        )
        self.wait(1)
        
        # Counter - positioned to the right of the line
        counter = Text("Samples: 0", font_size=24, color=WHITE)
        estimate_display = Text("Estimate: 0.00 cm", font_size=24, color=PURPLE)
        counter_group = VGroup(counter, estimate_display).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        counter_group.next_to(sim_line, RIGHT, buff=0.8)
        self.play(Write(counter_group))
        
        # Run simulation
        num_samples = 1000
        dots = VGroup()
        plot_points = []
        plot_dots = VGroup()
        
        total_count = 0
        inside_count = 0
        
        for i in range(num_samples):
            # Generate random number between 0 and 10
            random_value = random.uniform(0, ruler_length)
            
            # Check if inside the line
            is_inside = random_value <= true_length
            
            # Create dot on the line visualization
            x_pos = LEFT * line_width / 2 + RIGHT * random_value / ruler_length * line_width
            dot = Dot(sim_line.get_center() + x_pos + DOWN * 0.3, radius=0.05, 
                     color=GREEN if is_inside else GRAY, fill_opacity=0.7)
            dots.add(dot)
            
            # Update counters
            total_count += 1
            if is_inside:
                inside_count += 1
            
            # Calculate estimate
            estimated_length = (inside_count / total_count) * ruler_length
            plot_points.append((total_count, estimated_length))
            
            # Add point to plot
            plot_dot = Dot(axes.c2p(total_count, estimated_length), radius=0.02, color=PURPLE)
            plot_dots.add(plot_dot)
            
            # Update displays
            new_counter = Text(f"Samples: {total_count}", font_size=24, color=WHITE)
            new_estimate = Text(f"Estimate: {estimated_length:.2f} cm", font_size=24, color=PURPLE)
            new_counter_group = VGroup(new_counter, new_estimate).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            new_counter_group.move_to(counter_group)
            
            # Animation speed based on progress
            if i < 20:
                run_time = 0.3
            elif i < 100:
                run_time = 0.1
            elif i < 500:
                run_time = 0.02
            else:
                run_time = 0.005
            
            # Animate every nth frame for performance
            if i < 20 or i % 5 == 0:
                self.play(
                    FadeIn(dot, scale=1.5),
                    FadeIn(plot_dot),
                    Transform(counter_group, new_counter_group),
                    run_time=run_time
                )
            else:
                self.add(dot, plot_dot)
                counter_group.become(new_counter_group)
        
        self.wait(1)
        
        # Clear simulation for explanation slide
        self.play(
            FadeOut(VGroup(sim_line, ruler_scale, ruler_scale_marks,
                          axes, axes_labels, true_line, true_label, 
                          counter_group, dots, plot_dots)),
            run_time=1
        )
        
        # ========== EXPLANATION SLIDE ==========
        
        # Draw the convergence curve
        if len(plot_points) > 1:
            # Recreate axes for explanation - positioned higher and smaller
            explain_axes = Axes(
                x_range=[0, 1000, 200],
                y_range=[0, 10, 2],
                x_length=7,
                y_length=3.5,
                axis_config={"color": BLUE, "include_tip": True},
                x_axis_config={"numbers_to_include": [0, 200, 400, 600, 800, 1000]},
                y_axis_config={"numbers_to_include": [0, 2, 4, 6, 8, 10]},
            ).shift(UP * 1.2)  # Moved up to make room for text below
            
            explain_labels = explain_axes.get_axis_labels(
                x_label=Text("Number of Samples", font_size=22),
                y_label=Text("Estimated Length (cm)", font_size=22)
            )
            
            explain_true_line = DashedLine(
                explain_axes.c2p(0, true_length),
                explain_axes.c2p(1000, true_length),
                color=GREEN,
                stroke_width=3
            )
            explain_true_label = Text(f"True: {true_length} cm", font_size=18, color=GREEN)
            explain_true_label.next_to(explain_true_line, RIGHT, buff=0.1)
            
            self.play(
                Create(explain_axes),
                Write(explain_labels),
                Create(explain_true_line),
                Write(explain_true_label)
            )
            
            convergence_curve = explain_axes.plot_line_graph(
                x_values=[p[0] for p in plot_points[::10]],
                y_values=[p[1] for p in plot_points[::10]],
                line_color=PURPLE,
                stroke_width=3,
                add_vertex_dots=False
            )
            self.play(Create(convergence_curve), run_time=2)
        
        # Final result - positioned below the plot with more space
        final_estimate = (inside_count / total_count) * ruler_length
        result_text = Text(
            f"Final Estimate: {final_estimate:.3f} cm\nTrue Length: {true_length} cm\nError: {abs(final_estimate - true_length):.3f} cm",
            font_size=26,
            line_spacing=1.2,
            color=GOLD,
            weight=BOLD
        ).shift(DOWN * 2.5)  # Positioned specifically below the plot
        
        self.play(Write(result_text))
        self.wait(3)