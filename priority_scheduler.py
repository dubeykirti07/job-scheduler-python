# Priority Scheduling Algorithm
# Job with the highest priority (lowest number) executes first

def priority_scheduler(jobs):
    """
    jobs = list of tuples: (job_name, burst_time, priority)
    priority 1 = highest, priority 5 = lowest
    """
    print("=" * 60)
    print("   Priority Job Scheduler")
    print("=" * 60)
    print(f"{'Job':<10} {'Burst Time':<15} {'Priority':<12} {'Start':<10} {'Finish':<10} {'Waiting'}")
    print("-" * 60)

    # Sort jobs by priority (1 = highest priority)
    sorted_jobs = sorted(jobs, key=lambda x: x[2])

    current_time = 0
    total_waiting = 0

    for job_name, burst_time, priority in sorted_jobs:
        start_time = current_time
        finish_time = current_time + burst_time
        waiting_time = start_time

        total_waiting += waiting_time
        current_time = finish_time

        print(f"{job_name:<10} {burst_time:<15} {priority:<12} {start_time:<10} {finish_time:<10} {waiting_time}")

    avg_waiting = total_waiting / len(jobs)
    print("-" * 60)
    print(f"Average Waiting Time: {avg_waiting:.2f}")
    print("=" * 60)


if __name__ == "__main__":
    # (job_name, burst_time, priority)
    jobs = [
        ("Job_A", 5, 3),   # medium priority
        ("Job_B", 3, 1),   # highest priority → executes first
        ("Job_C", 8, 4),   # low priority
        ("Job_D", 2, 2),   # second highest priority
    ]
    priority_scheduler(jobs)