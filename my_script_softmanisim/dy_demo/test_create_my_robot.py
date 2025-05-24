import numpy as np
import time
import pybullet as p 

from pybullet_env.BasicEnvironment import SoftRobotBasicEnvironment
from visualizer.visualizer import ODE 

from my_script.dy_demo.DataLogger import DataLogger
from pathlib import Path
import pandas as pd
import csv
import os 
    

if __name__ == "__main__":
    
    yomo = SoftRobotBasicEnvironment(number_of_segment=1, head_color=[1,0.75, 1])
 
    t = 0
    dt = 0.01
    counter = 0
    # --- Initialize Logger ---
    FIELDNAMES = ['time', 'cable1', 'cable2', 'cable3', 'head_x', 'head_y', 'head_z']
    OUTPUT_DIR = Path("./output_data/my_yomo_refactored") # Define output dir base
    FILENAME_PREFIX = "yomo_run_log" # Define file prefix
    logger = DataLogger(output_dir_base=OUTPUT_DIR,
                        filename_prefix=FILENAME_PREFIX,
                        fieldnames=FIELDNAMES) 
    rollId = p.addUserDebugParameter("roll", -np.pi, np.pi, -np.pi/2)
    pitchId = p.addUserDebugParameter("pitch", -np.pi, np.pi, 0)
    yawId = p.addUserDebugParameter("yaw", -np.pi, np.pi, 0)

    try:
        while True:
            t += dt
            counter += 1
            
            roll = p.readUserDebugParameter(rollId)
            pitch = p.readUserDebugParameter(pitchId)
            yaw = p.readUserDebugParameter(yawId)
            
            #TODO this part substitute the real data
            yomo_cable_1 = 0
            yomo_cable_2 = .005*np.sin(0.5*np.pi*t+2+5)
            yomo_cable_3 = .005*np.sin(0.5*np.pi*t+2+5)
            
            yomo.move_robot_ori(action=np.array([0.0, yomo_cable_1, yomo_cable_2]),
                                base_pos = np.array([0.0, 0.0, 1.0]), #修改底座
                                base_orin= np.array([roll, pitch, yaw])) #修改底座     
            
            head_pose, head_ori = yomo.calc_tip_pos(action=np.array([0.0, yomo_cable_1, yomo_cable_2]),
                                base_pos = np.array([0.0, 0.0, 1.0]), #修改底座
                                base_orin= np.array([roll, pitch, yaw])) #修改底座     

            # --- Log Data Row ---
            data_row = {
                'time': t,
                'cable1': yomo_cable_1,
                'cable2': yomo_cable_2,
                'cable3': yomo_cable_3,
                'head_x': head_pose[0],
                'head_y': head_pose[1],
                'head_z': head_pose[2]
            }
            logger.log(data_row) # Use the logger's log method

            
            if counter % 200 == 0:
                print("hello world")
                formatted_head_pose = [f"{head_pose:.2f}" for head_pose in head_pose]
                formatted_head_ori = [f"{head_ori:.2f}" for head_ori in head_ori]
                print(f"the time at {t:.2f}, the head position is {formatted_head_pose}, and the orientation is {formatted_head_ori}")
                
    except KeyboardInterrupt:
        print("\n[info] Program interrupted by user.")
        
    finally:
        print("\n---保存最终数据---")
        saved_filepath = logger.save()
        if saved_filepath:
            print(f"[info] Data saving process finished. File: {saved_filepath}")
        else:
            print("[info] Data saving process finished (no data saved or error occurred).")


                    

                
        
            