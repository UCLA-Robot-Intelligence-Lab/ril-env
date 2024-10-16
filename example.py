import time
from ril_env.xarm_env import XArmEnv, XArmConfig
from ril_env.controller import SpaceMouse, SpaceMouseConfig

spacemouse_cfg = SpaceMouseConfig()
xarm_cfg = XArmConfig()

xarm_env = XArmEnv(xarm_cfg)
spacemouse = SpaceMouse(spacemouse_cfg)

control_loop_rate = xarm_cfg.control_loop_rate
control_loop_period = 1.0 / control_loop_rate

xarm_env._arm_reset()

try:
    while True:
        loop_start_time = time.time()

        controller_state = spacemouse.get_controller_state()
        dpos = controller_state["dpos"] * xarm_cfg.position_gain
        drot = controller_state["raw_drotation"] * xarm_cfg.orientation_gain
        grasp = controller_state["grasp"]

        xarm_env.step(dpos, drot, grasp)
        elapsed_time = time.time() - loop_start_time
        sleep_time = max(0.0, control_loop_period - elapsed_time)
        time.sleep(sleep_time)
except KeyboardInterrupt:
    print("Teleop manually shut down!")
    xarm_env._arm_reset()
except Exception as e:
    print(f"An error occurred: {e}")
    xarm_env._arm_reset()
