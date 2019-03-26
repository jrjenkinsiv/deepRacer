def reward_function(on_track, x, y, distance_from_center, car_orientation, progress, steps, throttle, steering, track_width, waypoints, closest_waypoint):
    
    '''
    '''

    import math

    #track width markers
    marker_1 = 0.1 * track_width
    marker_2 = 0.2 * track_width
    marker_3 = 0.3 * track_width
    marker_4 = 0.4 * track_width
    marker_5 = 0.5 * track_width
    marker_10 = track_width

    # reward car for staying on the track
    reward = 1e-3
    if distance_from_center >= 0.0 and distance_from_center <= marker_1:
        reward = 0.35
    elif distance_from_center <= marker_2:
        reward = 0.3
    elif distance_from_center <= marker_3:
        reward = 0.25
    elif distance_from_center <= marker_4:
        reward = 0.2
    elif distance_from_center <= marker_5:
        reward = 0.15
    elif distance_from_center <= marker_10:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    # penalize reward if the car is steering way too much
    ABS_STEERING_THRESHOLD = 0.25
    if abs(steering) > ABS_STEERING_THRESHOLD:
        reward *= 0.65

    # penalize reward for the car taking slow actions
    LOW_THROTTLE_THRESHOLD = 0.75
    if throttle <= LOW_THROTTLE_THRESHOLD:
        reward *= 0.75

    #reward for i wanna go fast
    HIGH_THROTTLE_THRESHOLD = 1
    if throttle == HIGH_THROTTLE_THRESHOLD:
        reward *= 1.25

    return float(reward)