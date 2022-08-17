from controller import Robot

bot = Robot()

timestep = 64

# getting devices
# get the camera device

left_wheel = bot.getDevice('left_front_wheel')
right_wheel = bot.getDevice('right_front_wheel')
l_steer = bot.getDevice('left_steer')
r_steer = bot.getDevice('right_steer')

# enable the camera

left_wheel.setPosition(float('inf'))
right_wheel.setPosition(float('inf'))
l_steer.setPosition(0)
r_steer.setPosition(0)
left_wheel.setVelocity(0)
right_wheel.setVelocity(0)
