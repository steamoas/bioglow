"""
Mission(s):
Setup:
Author(s):
"""
from pybricks.tools import run_task, wait
from robot import drive, hub


async def test():
    await drive.straight(250)
    await drive.turn(90)
    print(hub.imu.heading())
if __name__ == '__main__':
    run_task(test())
