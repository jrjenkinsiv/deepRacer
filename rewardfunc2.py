    def reward_function(on_track, x, y, distance_from_center, car_orientation, progress, steps, throttle, steering, track_width, waypoints, closest_waypoint):

    '''
    '''

    import math

    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    reward = 1e-3
    if distance_from_center >= 0.0 and distance_from_center <= marker_1:
        reward = 0.7
    elif distance_from_center <= marker_2:
        reward = 0.3
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    # penalize reward if the car is steering way too much
    ABS_STEERING_THRESHOLD = 0.5
    if abs(steering) > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    # penalize reward for the car taking slow actions
    THROTTLE_THRESHOLD = 0.75
    if throttle < THROTTLE_THRESHOLD:
        reward *= 0.8

    #reward for i wanna go fast
    THROTTLE_THRESHOLD = 1
    if throttle == THROTTLE_THRESHOLD:
        reward = 0.8

    return float(reward)