'''
    #21 steering, 10 throttle, 600 States

    #my steering angles
    steering_angle = steering_angle_ # full left (30)
    steering_angle = 0.9 * steering_angle_
    steering_angle = 0.8 * steering_angle_
    steering_angle = 0.7 * steering_angle_
    steering_angle = 0.6 * steering_angle_
    steering_angle = 0.5 * steering_angle_ # half left 15
    steering_angle = 0.4 * steering_angle_
    steering_angle = 0.3 * steering_angle_
    steering_angle = 0.2 * steering_angle_v
    steering_angle = 0.1 * steering_angle_
    steering_angle = 0 # straight 0
    steering_angle = -0.1 * steering_angle_
    steering_angle = -0.2 * steering_angle_
    steering_angle = -0.3 * steering_angle_
    steering_angle = -0.4 * steering_angle_
    steering_angle = -0.5 * steering_angle_ # half right -15
    steering_angle = -0.6 * steering_angle_
    steering_angle = -0.7 * steering_angle_
    steering_angle = -0.8 * steering_angle_
    steering_angle = -0.9 * steering_angle_
    steering_angle = -1 * steering_angle_ # full right -30
    
    #my throttles
    throttle = 0.1 * throttle_ # 0.5
    throttle = 0.2 * throttle_ # 1.0
    throttle = 0.3 * throttle_ # 1.5
    throttle = 0.4 * throttle_ # 2.0
    throttle = 0.5 * throttle_ # 2.5
    throttle = 0.6 * throttle_ # 3.0
    throttle = 0.7 * throttle_ # 3.5
    throttle = 0.8 * throttle_ # 4.0
    throttle = 0.9 * throttle_ # 4.5
    throttle = throttle_ # 5.0
'''

	def twentyone_steering_ten_throttle_600_states(self,throttle_, steering_angle_, action):
	# 5.0 throttle
        if action == 0: # 30, 5.0
        	steering_angle = steering_angle_
        	throttle = throttle_
        elif action == 1:
        	steering_angle = 0.9 * steering_angle_
        	throttle = throttle_
        elif action == 2:
        	steering_angle = 0.8 * steering_angle_
        	throttle = throttle_
        elif action == 3:
        	steering_angle = 0.7 * steering_angle_
        	throttle = throttle_
        elif action == 4:
        	steering_angle = 0.6 * steering_angle_
        	throttle = throttle_
        elif action == 5:
        	steering_angle = 0.5 * steering_angle_
        	throttle = throttle_
        elif action == 6:
        	steering_angle = 0.4 * steering_angle_
        	throttle = throttle_
        elif action == 7:
        	steering_angle = 0.3 * steering_angle_
        	throttle = throttle_
        elif action == 8:
        	steering_angle = 0.2 * steering_angle_
        	throttle = throttle_
        elif action == 9:
        	steering_angle = 0.1 * steering_angle_
        	throttle = throttle_
        elif action == 10:
        	steering_angle = 0
        	throttle = throttle_
        elif action == 11:
        	steering_angle = -0.1 * steering_angle_
        	throttle = throttle_
        elif action == 12:
        	steering_angle = -0.2 * steering_angle_
        	throttle = throttle_
        elif action == 13:
        	steering_angle = -0.3 * steering_angle_
        	throttle = throttle_
        elif action == 14:
        	steering_angle = -0.4 * steering_angle_
        	throttle = throttle_
        elif action == 15:
        	steering_angle = -0.5 * steering_angle_
        	throttle = throttle_
        elif action == 16:
        	steering_angle = -0.6 * steering_angle_
        	throttle = throttle_
        elif action == 17:
        	steering_angle = -0.7 * steering_angle_
        	throttle = throttle_
        elif action == 18:
        	steering_angle = -0.8 * steering_angle_
        	throttle = throttle_
        elif action == 19: # -30, 5.0
        	steering_angle = -0.9 * steering_angle_
        	throttle = throttle_

	# 4.5 throttle (0.9)
        if action == 0: # 30, 4.5
        	steering_angle = steering_angle_
        	throttle = 0.9 * throttle_
        elif action == 1:
        	steering_angle = 0.9 * steering_angle_
        	throttle = 0.9 * throttle_
        elif action == 2:
        	steering_angle = 0.8 * steering_angle_
        	throttle = 0.9 * throttle_
        elif action == 3:
        	steering_angle = 0.7 * steering_angle_
        	throttle = 0.9 * throttle_
        elif action == 4:
        	steering_angle = 0.6 * steering_angle_
        	throttle = 0.9 * throttle_
        elif action == 5:
        	steering_angle = 0.5 * steering_angle_
        	throttle = 0.9 * throttle_
        elif action == 6:
        	steering_angle = 0.4 * steering_angle_
        	throttle = 0.9 * throttle_
        elif action == 7:
        	steering_angle = 0.3 * steering_angle_
        	throttle = 0.9 * throttle_
        elif action == 8:
        	steering_angle = 0.2 * steering_angle_
        	throttle = 0.9 * throttle_
        elif action == 9:
        	steering_angle = 0.1 * steering_angle_
        	throttle = 0.9 * throttle_
        elif action == 10:
        	steering_angle = 0
        	throttle = 0.9 * throttle_
        elif action == 11:
        	steering_angle = -0.1 * steering_angle_
        	throttle = 0.9 * throttle_
        elif action == 12:
        	steering_angle = -0.2 * steering_angle_
        	throttle = 0.9 * throttle_
        elif action == 13:
        	steering_angle = -0.3 * steering_angle_
        	throttle = 0.9 * throttle_
        elif action == 14:
        	steering_angle = -0.4 * steering_angle_
        	throttle = 0.9 * throttle_
        elif action == 15:
        	steering_angle = -0.5 * steering_angle_
        	throttle = 0.9 * throttle_
        elif action == 16:
        	steering_angle = -0.6 * steering_angle_
        	throttle = 0.9 * throttle_
        elif action == 17:
        	steering_angle = -0.7 * steering_angle_
        	throttle = 0.9 * throttle_
        elif action == 18:
        	steering_angle = -0.8 * steering_angle_
        	throttle = 0.9 * throttle_
        elif action == 19: # -30, 4.5
        	steering_angle = -0.9 * steering_angle_
        	throttle = 0.9 * throttle_

    # 4.0 throttle (0.8)
        if action == 0: # 30, 4.0
        	steering_angle = steering_angle_
        	throttle = 0.8 * throttle_
        elif action == 1:
        	steering_angle = 0.9 * steering_angle_
        	throttle = 0.8 * throttle_
        elif action == 2:
        	steering_angle = 0.8 * steering_angle_
        	throttle = 0.8 * throttle_
        elif action == 3:
        	steering_angle = 0.7 * steering_angle_
        	throttle = 0.8 * throttle_
        elif action == 4:
        	steering_angle = 0.6 * steering_angle_
        	throttle = 0.8 * throttle_
        elif action == 5:
        	steering_angle = 0.5 * steering_angle_
        	throttle = 0.8 * throttle_
        elif action == 6:
        	steering_angle = 0.4 * steering_angle_
        	throttle = 0.8 * throttle_
        elif action == 7:
        	steering_angle = 0.3 * steering_angle_
        	throttle = 0.8 * throttle_
        elif action == 8:
        	steering_angle = 0.2 * steering_angle_
        	throttle = 0.8 * throttle_
        elif action == 9:
        	steering_angle = 0.1 * steering_angle_
        	throttle = 0.8 * throttle_
        elif action == 10:
        	steering_angle = 0
        	throttle = 0.8 * throttle_
        elif action == 11:
        	steering_angle = -0.1 * steering_angle_
        	throttle = 0.8 * throttle_
        elif action == 12:
        	steering_angle = -0.2 * steering_angle_
        	throttle = 0.8 * throttle_
        elif action == 13:
        	steering_angle = -0.3 * steering_angle_
        	throttle = 0.8 * throttle_
        elif action == 14:
        	steering_angle = -0.4 * steering_angle_
        	throttle = 0.8 * throttle_
        elif action == 15:
        	steering_angle = -0.5 * steering_angle_
        	throttle = 0.8 * throttle_
        elif action == 16:
        	steering_angle = -0.6 * steering_angle_
        	throttle = 0.8 * throttle_
        elif action == 17:
        	steering_angle = -0.7 * steering_angle_
        	throttle = 0.8 * throttle_
        elif action == 18:
        	steering_angle = -0.8 * steering_angle_
        	throttle = 0.8 * throttle_
        elif action == 19: # -30, 4.0
        	steering_angle = -0.9 * steering_angle_
        	throttle = 0.8 * throttle_

    # 3.5 throttle (0.7)
        if action == 0: # 30, 3.5
        	steering_angle = steering_angle_
        	throttle = 0.7 * throttle_
        elif action == 1:
        	steering_angle = 0.9 * steering_angle_
        	throttle = 0.7 * throttle_
        elif action == 2:
        	steering_angle = 0.8 * steering_angle_
        	throttle = 0.7 * throttle_
        elif action == 3:
        	steering_angle = 0.7 * steering_angle_
        	throttle = 0.7 * throttle_
        elif action == 4:
        	steering_angle = 0.6 * steering_angle_
        	throttle = 0.7 * throttle_
        elif action == 5:
        	steering_angle = 0.5 * steering_angle_
        	throttle = 0.7 * throttle_
        elif action == 6:
        	steering_angle = 0.4 * steering_angle_
        	throttle = 0.7 * throttle_
        elif action == 7:
        	steering_angle = 0.3 * steering_angle_
        	throttle = 0.7 * throttle_
        elif action == 8:
        	steering_angle = 0.2 * steering_angle_
        	throttle = 0.7 * throttle_
        elif action == 9:
        	steering_angle = 0.1 * steering_angle_
        	throttle = 0.7 * throttle_
        elif action == 10:
        	steering_angle = 0
        	throttle = 0.7 * throttle_
        elif action == 11:
        	steering_angle = -0.1 * steering_angle_
        	throttle = 0.7 * throttle_
        elif action == 12:
        	steering_angle = -0.2 * steering_angle_
        	throttle = 0.7 * throttle_
        elif action == 13:
        	steering_angle = -0.3 * steering_angle_
        	throttle = 0.7 * throttle_
        elif action == 14:
        	steering_angle = -0.4 * steering_angle_
        	throttle = 0.7 * throttle_
        elif action == 15:
        	steering_angle = -0.5 * steering_angle_
        	throttle = 0.7 * throttle_
        elif action == 16:
        	steering_angle = -0.6 * steering_angle_
        	throttle = 0.7 * throttle_
        elif action == 17:
        	steering_angle = -0.7 * steering_angle_
        	throttle = 0.7 * throttle_
        elif action == 18:
        	steering_angle = -0.8 * steering_angle_
        	throttle = 0.7 * throttle_
        elif action == 19: # -30, 3.5
        	steering_angle = -0.9 * steering_angle_
        	throttle = 0.7 * throttle_

    # 3.0 throttle (0.6)
        if action == 0: # 30, 3.0
        	steering_angle = steering_angle_
        	throttle = 0.6 * throttle_
        elif action == 1:
        	steering_angle = 0.9 * steering_angle_
        	throttle = 0.6 * throttle_
        elif action == 2:
        	steering_angle = 0.8 * steering_angle_
        	throttle = 0.6 * throttle_
        elif action == 3:
        	steering_angle = 0.7 * steering_angle_
        	throttle = 0.6 * throttle_
        elif action == 4:
        	steering_angle = 0.6 * steering_angle_
        	throttle = 0.6 * throttle_
        elif action == 5:
        	steering_angle = 0.5 * steering_angle_
        	throttle = 0.6 * throttle_
        elif action == 6:
        	steering_angle = 0.4 * steering_angle_
        	throttle = 0.6 * throttle_
        elif action == 7:
        	steering_angle = 0.3 * steering_angle_
        	throttle = 0.6 * throttle_
        elif action == 8:
        	steering_angle = 0.2 * steering_angle_
        	throttle = 0.6 * throttle_
        elif action == 9:
        	steering_angle = 0.1 * steering_angle_
        	throttle = 0.6 * throttle_
        elif action == 10:
        	steering_angle = 0
        	throttle = 0.6 * throttle_
        elif action == 11:
        	steering_angle = -0.1 * steering_angle_
        	throttle = 0.6 * throttle_
        elif action == 12:
        	steering_angle = -0.2 * steering_angle_
        	throttle = 0.6 * throttle_
        elif action == 13:
        	steering_angle = -0.3 * steering_angle_
        	throttle = 0.6 * throttle_
        elif action == 14:
        	steering_angle = -0.4 * steering_angle_
        	throttle = 0.6 * throttle_
        elif action == 15:
        	steering_angle = -0.5 * steering_angle_
        	throttle = 0.6 * throttle_
        elif action == 16:
        	steering_angle = -0.6 * steering_angle_
        	throttle = 0.6 * throttle_
        elif action == 17:
        	steering_angle = -0.7 * steering_angle_
        	throttle = 0.6 * throttle_
        elif action == 18:
        	steering_angle = -0.8 * steering_angle_
        	throttle = 0.6 * throttle_
        elif action == 19: # -30, 3.0
        	steering_angle = -0.9 * steering_angle_
        	throttle = 0.6 * throttle_

    # 2.5 throttle (0.5)
        if action == 0: # 30, 2.5
        	steering_angle = steering_angle_
        	throttle = 0.5 * throttle_
        elif action == 1:
        	steering_angle = 0.9 * steering_angle_
        	throttle = 0.5 * throttle_
        elif action == 2:
        	steering_angle = 0.8 * steering_angle_
        	throttle = 0.5 * throttle_
        elif action == 3:
        	steering_angle = 0.7 * steering_angle_
        	throttle = 0.5 * throttle_
        elif action == 4:
        	steering_angle = 0.6 * steering_angle_
        	throttle = 0.5 * throttle_
        elif action == 5:
        	steering_angle = 0.5 * steering_angle_
        	throttle = 0.5 * throttle_
        elif action == 6:
        	steering_angle = 0.4 * steering_angle_
        	throttle = 0.5 * throttle_
        elif action == 7:
        	steering_angle = 0.3 * steering_angle_
        	throttle = 0.5 * throttle_
        elif action == 8:
        	steering_angle = 0.2 * steering_angle_
        	throttle = 0.5 * throttle_
        elif action == 9:
        	steering_angle = 0.1 * steering_angle_
        	throttle = 0.5 * throttle_
        elif action == 10:
        	steering_angle = 0
        	throttle = 0.5 * throttle_
        elif action == 11:
        	steering_angle = -0.1 * steering_angle_
        	throttle = 0.5 * throttle_
        elif action == 12:
        	steering_angle = -0.2 * steering_angle_
        	throttle = 0.5 * throttle_
        elif action == 13:
        	steering_angle = -0.3 * steering_angle_
        	throttle = 0.5 * throttle_
        elif action == 14:
        	steering_angle = -0.4 * steering_angle_
        	throttle = 0.5 * throttle_
        elif action == 15:
        	steering_angle = -0.5 * steering_angle_
        	throttle = 0.5 * throttle_
        elif action == 16:
        	steering_angle = -0.6 * steering_angle_
        	throttle = 0.5 * throttle_
        elif action == 17:
        	steering_angle = -0.7 * steering_angle_
        	throttle = 0.5 * throttle_
        elif action == 18:
        	steering_angle = -0.8 * steering_angle_
        	throttle = 0.5 * throttle_
        elif action == 19: # -30, 2.5
        	steering_angle = -0.9 * steering_angle_
        	throttle = 0.5 * throttle_

    # 2.0 throttle (0.4)
        if action == 0: # 30, 2.0
        	steering_angle = steering_angle_
        	throttle = 0.4 * throttle_
        elif action == 1:
        	steering_angle = 0.9 * steering_angle_
        	throttle = 0.4 * throttle_
        elif action == 2:
        	steering_angle = 0.8 * steering_angle_
        	throttle = 0.4 * throttle_
        elif action == 3:
        	steering_angle = 0.7 * steering_angle_
        	throttle = 0.4 * throttle_
        elif action == 4:
        	steering_angle = 0.6 * steering_angle_
        	throttle = 0.4 * throttle_
        elif action == 5:
        	steering_angle = 0.5 * steering_angle_
        	throttle = 0.4 * throttle_
        elif action == 6:
        	steering_angle = 0.4 * steering_angle_
        	throttle = 0.4 * throttle_
        elif action == 7:
        	steering_angle = 0.3 * steering_angle_
        	throttle = 0.4 * throttle_
        elif action == 8:
        	steering_angle = 0.2 * steering_angle_
        	throttle = 0.4 * throttle_
        elif action == 9:
        	steering_angle = 0.1 * steering_angle_
        	throttle = 0.4 * throttle_
        elif action == 10:
        	steering_angle = 0
        	throttle = 0.4 * throttle_
        elif action == 11:
        	steering_angle = -0.1 * steering_angle_
        	throttle = 0.4 * throttle_
        elif action == 12:
        	steering_angle = -0.2 * steering_angle_
        	throttle = 0.4 * throttle_
        elif action == 13:
        	steering_angle = -0.3 * steering_angle_
        	throttle = 0.4 * throttle_
        elif action == 14:
        	steering_angle = -0.4 * steering_angle_
        	throttle = 0.4 * throttle_
        elif action == 15:
        	steering_angle = -0.5 * steering_angle_
        	throttle = 0.4 * throttle_
        elif action == 16:
        	steering_angle = -0.6 * steering_angle_
        	throttle = 0.4 * throttle_
        elif action == 17:
        	steering_angle = -0.7 * steering_angle_
        	throttle = 0.4 * throttle_
        elif action == 18:
        	steering_angle = -0.8 * steering_angle_
        	throttle = 0.4 * throttle_
        elif action == 19: # -30, 2.0
        	steering_angle = -0.9 * steering_angle_
        	throttle = 0.4 * throttle_

    # 1.5 throttle (0.3)
        if action == 0: # 30, 1.5
        	steering_angle = steering_angle_
        	throttle = 0.3 * throttle_
        elif action == 1:
        	steering_angle = 0.9 * steering_angle_
        	throttle = 0.3 * throttle_
        elif action == 2:
        	steering_angle = 0.8 * steering_angle_
        	throttle = 0.3 * throttle_
        elif action == 3:
        	steering_angle = 0.7 * steering_angle_
        	throttle = 0.3 * throttle_
        elif action == 4:
        	steering_angle = 0.6 * steering_angle_
        	throttle = 0.3 * throttle_
        elif action == 5:
        	steering_angle = 0.5 * steering_angle_
        	throttle = 0.3 * throttle_
        elif action == 6:
        	steering_angle = 0.4 * steering_angle_
        	throttle = 0.3 * throttle_
        elif action == 7:
        	steering_angle = 0.3 * steering_angle_
        	throttle = 0.3 * throttle_
        elif action == 8:
        	steering_angle = 0.2 * steering_angle_
        	throttle = 0.3 * throttle_
        elif action == 9:
        	steering_angle = 0.1 * steering_angle_
        	throttle = 0.3 * throttle_
        elif action == 10:
        	steering_angle = 0
        	throttle = 0.3 * throttle_
        elif action == 11:
        	steering_angle = -0.1 * steering_angle_
        	throttle = 0.3 * throttle_
        elif action == 12:
        	steering_angle = -0.2 * steering_angle_
        	throttle = 0.3 * throttle_
        elif action == 13:
        	steering_angle = -0.3 * steering_angle_
        	throttle = 0.3 * throttle_
        elif action == 14:
        	steering_angle = -0.4 * steering_angle_
        	throttle = 0.3 * throttle_
        elif action == 15:
        	steering_angle = -0.5 * steering_angle_
        	throttle = 0.3 * throttle_
        elif action == 16:
        	steering_angle = -0.6 * steering_angle_
        	throttle = 0.3 * throttle_
        elif action == 17:
        	steering_angle = -0.7 * steering_angle_
        	throttle = 0.3 * throttle_
        elif action == 18:
        	steering_angle = -0.8 * steering_angle_
        	throttle = 0.3 * throttle_
        elif action == 19: # -30, 5.0
        	steering_angle = -0.9 * steering_angle_
        	throttle = 0.3 * throttle_

    # 1.0 throttle (0.2)
        if action == 0: # 30, 1.0
        	steering_angle = steering_angle_
        	throttle = 0.2 * throttle_
        elif action == 1:
        	steering_angle = 0.9 * steering_angle_
        	throttle = 0.2 * throttle_
        elif action == 2:
        	steering_angle = 0.8 * steering_angle_
        	throttle = 0.2 * throttle_
        elif action == 3:
        	steering_angle = 0.7 * steering_angle_
        	throttle = 0.2 * throttle_
        elif action == 4:
        	steering_angle = 0.6 * steering_angle_
        	throttle = 0.2 * throttle_
        elif action == 5:
        	steering_angle = 0.5 * steering_angle_
        	throttle = 0.2 * throttle_
        elif action == 6:
        	steering_angle = 0.4 * steering_angle_
        	throttle = 0.2 * throttle_
        elif action == 7:
        	steering_angle = 0.3 * steering_angle_
        	throttle = 0.2 * throttle_
        elif action == 8:
        	steering_angle = 0.2 * steering_angle_
        	throttle = 0.2 * throttle_
        elif action == 9:
        	steering_angle = 0.1 * steering_angle_
        	throttle = 0.2 * throttle_
        elif action == 10:
        	steering_angle = 0
        	throttle = 0.2 * throttle_
        elif action == 11:
        	steering_angle = -0.1 * steering_angle_
        	throttle = 0.2 * throttle_
        elif action == 12:
        	steering_angle = -0.2 * steering_angle_
        	throttle = 0.2 * throttle_
        elif action == 13:
        	steering_angle = -0.3 * steering_angle_
        	throttle = 0.2 * throttle_
        elif action == 14:
        	steering_angle = -0.4 * steering_angle_
        	throttle = 0.2 * throttle_
        elif action == 15:
        	steering_angle = -0.5 * steering_angle_
        	throttle = 0.2 * throttle_
        elif action == 16:
        	steering_angle = -0.6 * steering_angle_
        	throttle = 0.2 * throttle_
        elif action == 17:
        	steering_angle = -0.7 * steering_angle_
        	throttle = 0.2 * throttle_
        elif action == 18:
        	steering_angle = -0.8 * steering_angle_
        	throttle = 0.2 * throttle_
        elif action == 19: # -30, 5.0
        	steering_angle = -0.9 * steering_angle_
        	throttle = 0.2 * throttle_

    # 0.5 throttle (0.1)
        if action == 0: # 30, 0.5
        	steering_angle = steering_angle_
        	throttle = 0.1 * throttle_
        elif action == 1:
        	steering_angle = 0.9 * steering_angle_
        	throttle = 0.1 * throttle_
        elif action == 2:
        	steering_angle = 0.8 * steering_angle_
        	throttle = 0.1 * throttle_
        elif action == 3:
        	steering_angle = 0.7 * steering_angle_
        	throttle = 0.1 * throttle_
        elif action == 4:
        	steering_angle = 0.6 * steering_angle_
        	throttle = 0.1 * throttle_
        elif action == 5:
        	steering_angle = 0.5 * steering_angle_
        	throttle = 0.1 * throttle_
        elif action == 6:
        	steering_angle = 0.4 * steering_angle_
        	throttle = 0.1 * throttle_
        elif action == 7:
        	steering_angle = 0.3 * steering_angle_
        	throttle = 0.1 * throttle_
        elif action == 8:
        	steering_angle = 0.2 * steering_angle_
        	throttle = 0.1 * throttle_
        elif action == 9:
        	steering_angle = 0.1 * steering_angle_
        	throttle = 0.1 * throttle_
        elif action == 10:
        	steering_angle = 0
        	throttle = 0.1 * throttle_
        elif action == 11:
        	steering_angle = -0.1 * steering_angle_
        	throttle = 0.1 * throttle_
        elif action == 12:
        	steering_angle = -0.2 * steering_angle_
        	throttle = 0.1 * throttle_
        elif action == 13:
        	steering_angle = -0.3 * steering_angle_
        	throttle = 0.1 * throttle_
        elif action == 14:
        	steering_angle = -0.4 * steering_angle_
        	throttle = 0.1 * throttle_
        elif action == 15:
        	steering_angle = -0.5 * steering_angle_
        	throttle = 0.1 * throttle_
        elif action == 16:
        	steering_angle = -0.6 * steering_angle_
        	throttle = 0.1 * throttle_
        elif action == 17:
        	steering_angle = -0.7 * steering_angle_
        	throttle = 0.1 * throttle_
        elif action == 18:
        	steering_angle = -0.8 * steering_angle_
        	throttle = 0.1 * throttle_
        elif action == 19: # -30, 0.5
        	steering_angle = -0.9 * steering_angle_
        	throttle = 0.1 * throttle_