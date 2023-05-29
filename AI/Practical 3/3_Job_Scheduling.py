def schedule_job(jobs):
    jobs=sorted(jobs,key=lambda x:x[1])
    
    schedule=[]
    prev_end_time=0
    
    for job in jobs:
        start_time,end_time,profit=job
        if start_time >= prev_end_time:
            schedule.append(job)
            prev_end_time=end_time
    return schedule

job=[(0,2,30),(3,6,35),(4,7,56),(7,9,67)]
result=schedule_job(job)
print("Scheduled jobs: ")

for job in result:
    print(f"Start time: {job[0]}, End time: {job[1]}, Profit: {job[2]}")
        
