# FCFS (First Come First Serve) Job Scheduler
# Jobs execute in the order they arrive

def fcfs_scheduler(jobs):
    """
    jobs = list of tuples: (job_name, burst_time)
    burst_time = time required to complete the job
    """
    print("=" * 55)
    print("   FCFS Job Scheduler")
    print("=" * 55)
    print(f"{'Job':<10} {'Burst Time':<15} {'Start':<10} {'Finish':<10} {'Waiting'}")
    print("-" * 55)

    current_time = 0
    total_waiting = 0

    for job_name, burst_time in jobs:
        start_time = current_time
        finish_time = current_time + burst_time
        waiting_time = start_time

        total_waiting += waiting_time
        current_time = finish_time

        print(f"{job_name:<10} {burst_time:<15} {start_time:<10} {finish_time:<10} {waiting_time}")

    avg_waiting = total_waiting / len(jobs)
    print("-" * 55)
    print(f"Average Waiting Time: {avg_waiting:.2f}")
    print("=" * 55)


if __name__ == "__main__":
    jobs = [
        ("Job_A", 5),
        ("Job_B", 3),
        ("Job_C", 8),
        ("Job_D", 2),
    ]
    fcfs_scheduler(jobs)