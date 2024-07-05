import numpy as np

#===========================#
# Photon arrival simulation #
#===========================#

def PoissonProcess(t, lambda_rate):

    """
    Pulse repetition rate (lambda_rate): photon emmitted rate (photon/s).
    Mean time interval (t_interval) (s)
    Time passed (t_pass) (s)

    """

    t_interval = 1 / lambda_rate
    t_pass = 0
    arrival_time_points = []

    while t_pass < t:
        interarrival_time = np.random.exponential(scale = t_interval)
        t_pass += interarrival_time
        
        if t_pass < t:
            arrival_time_points.append(t_pass)

    # Convert arrival times to seconds
    arrival_times_array = np.array(arrival_time_points)

    return arrival_times_array