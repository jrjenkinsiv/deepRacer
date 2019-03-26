def reward_function(on_track, x, y, distance_from_center, car_orientation, progress, steps, throttle, steering, track_width, waypoints, closest_waypoint):

    '''
    '''

    import math

    # track width markers
    marker_1 = 0.1 * track_width
    marker_2 = 0.2 * track_width
    marker_3 = 0.3 * track_width
    marker_4 = 0.4 * track_width
    marker_5 = 0.5 * track_width
    marker_10 = track_width

    # throttle thresholds
    low_throttle_threshold = 0.5
    mid_throttle_threshold = 0.75
    high_throttle_threshold = 1

    # steering thresholds
    abs_steering_threshold = 0.85

    # reward for making progress, penalize reward for falling off track
    if not on_track:
        reward = -1
    else:
        reward = progress * 0.25

    # reward car for distance_from_center
    reward = 1e-3 # 0.001
    if distance_from_center >= 0.0 and distance_from_center <= marker_1:
        reward = 0.6
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_4:
        reward = 0.4
    elif distance_from_center <= marker_5:
        reward = 0.2
    elif distance_from_center <= marker_10:
        reward = 0.05
    else:
        reward = 1e-3  # likely crashed/ close to off track

    # penalize reward if the car is steering way too much
    if abs(steering) > abs_steering_threshold:
        reward *= 0.95

    # penalize reward for the car taking slow actions
    if throttle <= low_throttle_threshold:
        reward *= 0.7

    # reward for maximum throttle
    if throttle >= high_throttle_threshold:
        reward *= 1.25

    return float(reward)