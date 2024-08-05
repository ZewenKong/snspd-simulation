import numpy as np

# use a script to generate photon-arrival events 
# with appropriate Poisson statistics, 
# and input these events into the gate to 
# simulate random photon arrival processes from a laser source.

def PoissonProcess(t, lambda_rate, v):

    """
    Pulse repetition rate (lambda_rate): photon emmitted rate (photon/s).
    Mean time interval (time_interval) (s)
    Time passed (time_point) (s)

    """

    time_interval = 1/lambda_rate  # time interval
    time_point = 0
    arrival_time_points = []

    while time_point < t:
        arrival_time = np.random.exponential(scale = time_interval)
        time_point += arrival_time
        
        if time_point < t:
            arrival_time_points.append(time_point)

    # Convert arrival times to seconds
    arrival_time_points_array = np.array(arrival_time_points)

    # Intrinsic detection efficiency (Range: 1 to 2 V)
    eta_max = 0.95  # max intrinsic detection efficiency
    Vm = 1.5        # mid point
    Vs = 0.2        # sharpness

    detection_p = eta_max * (np.tanh((v - Vm) / Vs) + 1) / 2
    return arrival_time_points_array, detection_p