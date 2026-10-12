from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor

hub = PrimeHub()
left_drive = Motor(Port.A,Direction.COUNTERCLOCKWISE)
right_drive = Motor(Port.F,Direction.CLOCKWISE)
AXLE_TRACK=103
drive=DriveBase(left_drive,right_drive,62,AXLE_TRACK)
drive.use_gyro(True)


