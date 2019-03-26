    def two_steering_three_throttle_15_states(self,throttle_, steering_angle_, action):
        
        # Convert discrete to continuous
        if action == 0:  # move left
            steering_angle = steering_angle_
            throttle = throttle_
        elif action == 1:  # move right
            steering_angle = -1 * steering_angle_
            throttle = throttle_            
        elif action == 2:  # move left
            steering_angle = 0.5 * steering_angle_
            throttle = throttle_
        elif action == 3:  # move right
            steering_angle = -0.5 * steering_angle_
            throttle = throttle_
        elif action == 4:  # straight
            steering_angle = 0
            throttle = throttle_
            
            
        elif action == 5:  # move left
            steering_angle = steering_angle_
            throttle = 0.5 * throttle_
        elif action == 6:  # move right
            steering_angle = -1 * steering_angle_
            throttle = 0.5 * throttle_      
        elif action == 7:  # move left
            steering_angle = 0.5 * steering_angle_
            throttle = 0.5 * throttle_
        elif action == 8:  # move right
            steering_angle = -0.5 * steering_angle_
            throttle = 0.5 * throttle_          
        elif action == 9:  # slow straight
            steering_angle = 0
            throttle = throttle_ *0.5
            
        elif action == 10:  # move left
            steering_angle = 1 * steering_angle_
            throttle = throttle_ * 2.0
        elif action == 11:  # move right
            steering_angle = -1 * steering_angle_
            throttle = throttle_ * 2.0
        elif action == 12:  # move left
            steering_angle = 0.5 * steering_angle_
            throttle = throttle_ * 2.0
        elif action == 13:  # move right
            steering_angle = -0.5 * steering_angle_
            throttle = throttle_ * 2.0
        elif action == 14:  # fast straight
            steering_angle = 0
            throttle = throttle_ * 2.0
            
        else:  # should not be here
            raise ValueError("Invalid action")
            
        return throttle, steering_angle