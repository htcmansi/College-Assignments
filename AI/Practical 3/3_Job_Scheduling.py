def schedule_jobs(jobs):
    # Sort jobs in descending order of their durations
    sorted_jobs = sorted(jobs, key=lambda x: x[1], reverse=True)

    # Initialize the schedule and the finish time
    schedule = []
    finish_time = 0

    # Iterate over the sorted jobs and assign them to the schedule
    for job in sorted_jobs:
        start_time = max(job[0], finish_time)  # Start time is the maximum of the current job's start time and the finish time of the previous job
        finish_time = start_time + job[1]  # Update the finish time
        schedule.append((job[0], start_time, finish_time))  # Add the job to the schedule

    return schedule


jobs = [(1, 4), (2, 2), (3, 5), (4, 7), (5, 1)]
result = schedule_jobs(jobs)

# Print the schedule
for job in result:
    print(f"Job {job[0]} starts at {job[1]} and finishes at {job[2]}")
