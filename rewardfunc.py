    def reward_function(self, on_track, x, y, distance_from_center, car_orientation, progress, steps,
                        throttle, steering, track_width, waypoints, closest_waypoints):
        reward = 1e-3
        if distance_from_center >= 0.0 and distance_from_center <= 0.03:
            reward = 1.0
            
        # add steering penalty
        if abs(steering) > 0.5:
            reward *= 0.80
            
        # add throttle penalty
        if throttle < 0.5:
            reward *= 0.80
            
        return reward