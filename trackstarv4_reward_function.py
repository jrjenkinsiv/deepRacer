def reward_function(on_track, x, y, distance_from_center, car_orientation, progress, steps, throttle, steering, track_width, waypoints, closest_waypoint):

    '''
    
    @on_track (boolean) :: The vehicle is off-track if the front of the vehicle is outside of the white
    lines

    @x (float range: [0, 1]) :: Fraction of where the car is along the x-axis. 1 indicates
    max 'x' value in the coordinate system.

    @y (float range: [0, 1]) :: Fraction of where the car is along the y-axis. 1 indicates
    max 'y' value in the coordinate system.

    @distance_from_center (float [0, track_width/2]) :: Displacement from the center line of the track
    as defined by way points

    @car_orientation (float: [-3.14, 3.14]) :: yaw of the car with respect to the car's x-axis in
    radians

    @progress (float: [0,1]) :: % of track complete

    @steps (int) :: numbers of steps completed

    @throttle :: (float) 0 to 1 (0 indicates stop, 1 max throttle)

    @steering :: (float) -1 to 1 (-1 is right, 1 is left)

    @track_width (float) :: width of the track (> 0)

    @waypoints (ordered list) :: list of waypoint in order; each waypoint is a set of coordinates
    (x,y,yaw) that define a turning point

    @closest_waypoint (int) :: index of the closest waypoint (0-indexed) given the car's x,y
    position as measured by the eucliedean distance

    @@output: @reward (float [-1e5, 1e5])
    # track width marker definitions
    # marker_1 = 0.1 * track_width
    # marker_2 = 0.2 * track_width
    # marker_3 = 0.3 * track_width
    # marker_4 = 0.4 * track_width
    # marker_5 = 0.5 * track_width
    # marker_6 = 0.6 * track_width
    # marker_7 = 0.7 * track_width
    # marker_8 = 0.8 * track_width
    # marker_9 = 0.9 * track_width
    # marker_10 = track_width

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
        reward = 0.75
    elif distance_from_center <= marker_2:
        reward = 0.7
    elif distance_from_center <= marker_3:
        reward = 0.65
    elif distance_from_center <= marker_4:
        reward = 0.6
    elif distance_from_center <= marker_5:
        reward = 0.4
    elif distance_from_center <= marker_10:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    #reward for going fast
    THROTTLE_THRESHOLD = 1
    if throttle == THROTTLE_THRESHOLD:
        reward = 0.5

    # penalize reward if the car is steering way too much
    ABS_STEERING_THRESHOLD = 0.5
    if abs(steering) > ABS_STEERING_THRESHOLD:
        reward *= 0.85

    # penalize reward for the car taking slow actions
    THROTTLE_THRESHOLD = 0.9
    if throttle <= THROTTLE_THRESHOLD:
        reward *= 0.2

    return float(reward)