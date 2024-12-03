remote_control_code_enabled = True
disable_duration = 0
Disabletimer = 0
message1 = Event()
run_automation = Event()
botton_pressed = Event()
end_automation = Event()
disable_robot = Event()

def when_started1():
    global disable_duration, Disabletimer, message1, run_automation, botton_pressed, end_automation, disable_robot, remote_control_code_enabled
    remote_control_code_enabled = True
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    brain.screen.set_pen_color(Color.PURPLE)
    brain.screen.set_fill_color(Color.PURPLE)
    brain.screen.draw_rectangle(0, 0, 479, 239)

def onevent_bumper_a_pressed_0():
    global disable_duration, Disabletimer, message1, run_automation, botton_pressed, end_automation, disable_robot, remote_control_code_enabled
    remote_control_code_enabled = False
    brain.screen.set_fill_color(Color.RED)
    brain.screen.draw_rectangle(0, 0, 479, 329)
    motor_8.spin_for(REVERSE, 180, DEGREES)
    brain.screen.set_fill_color(Color.GREEN)
    brain.screen.draw_rectangle(0, 0, 479, 329)
    wait(Disabletimer, SECONDS)
    Disabletimer = Disabletimer * 2
    drivetrain.drive_for(REVERSE, 200, MM)
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    remote_control_code_enabled = True

def onevent_bumper_b_pressed_0():
    global disable_duration, Disabletimer, message1, run_automation, botton_pressed, end_automation, disable_robot, remote_control_code_enabled
    pass

def when_started2():
    global disable_duration, Disabletimer, message1, run_automation, botton_pressed, end_automation, disable_robot, remote_control_code_enabled
    disable_duration = 0

def onevent_disable_robot_0():
    global disable_duration, Disabletimer, message1, run_automation, botton_pressed, end_automation, disable_robot, remote_control_code_enabled
    wait(1, SECONDS)
    Disabletimer = 0 * 0
    Disabletimer = 0
    end_automation.broadcast()

def onevent_botton_pressed_0():
    global disable_duration, Disabletimer, message1, run_automation, botton_pressed, end_automation, disable_robot, remote_control_code_enabled
    disable_robot.broadcast()
    Disabletimer = 0
    run_automation.broadcast()

def onevent_run_automation_0():
    global disable_duration, Disabletimer, message1, run_automation, botton_pressed, end_automation, disable_robot, remote_control_code_enabled
    # disable_controller or commands
    while not (False or False):
        wait(5, MSEC)

def onevent_bumper_a_pressed_1():
    global disable_duration, Disabletimer, message1, run_automation, botton_pressed, end_automation, disable_robot, remote_control_code_enabled
    botton_pressed.broadcast()

# system event handlers
bumper_a.pressed(onevent_bumper_a_pressed_0)
bumper_a.pressed(onevent_bumper_a_pressed_1)
bumper_b.pressed(onevent_bumper_b_pressed_0)
disable_robot(onevent_disable_robot_0)
botton_pressed(onevent_botton_pressed_0)
run_automation(onevent_run_automation_0)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

ws2 = Thread( when_started2 )
when_started1()
