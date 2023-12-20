def fcfs_schedule(jobs):
    # Sort jobs based on their arrival time (assuming the jobs have arrival times)
    sorted_jobs = sorted(jobs, key=lambda x: x[0])

    # Initialize variables
    schedule = []
    current_time = 0

    # Schedule jobs
    for job in sorted_jobs:
        arrival_time, job_name, duration = job
        start_time = max(current_time, arrival_time)
        end_time = start_time + duration
        schedule.append((job_name, start_time, end_time))
        current_time = end_time

    return schedule

# Example usage
jobs = [(0, "Job1", 3), (2, "Job2", 1), (4, "Job3", 4), (6, "Job4", 2)]
result = fcfs_schedule(jobs)

# Display the schedule
for job in result:
    print(f"Job: {job[0]}, Start Time: {job[1]}, End Time: {job[2]}")
