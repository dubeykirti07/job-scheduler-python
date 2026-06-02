# Synchronous vs Asynchronous Tasks
# Sync  = one task finishes before the next one starts (blocking)
# Async = all tasks can run at the same time (non-blocking)

import asyncio
import time


# ========================
# SYNCHRONOUS EXAMPLE
# ========================

def sync_job(job_name, duration):
    print(f"[SYNC] {job_name} started...")
    time.sleep(duration)    # blocks everything until done
    print(f"[SYNC] {job_name} finished! (took {duration}s)")

def run_sync_jobs():
    print("=" * 45)
    print("   SYNCHRONOUS Jobs (one by one)")
    print("=" * 45)
    start = time.time()

    sync_job("Job_A", 2)
    sync_job("Job_B", 1)
    sync_job("Job_C", 3)

    end = time.time()
    print(f"Total time (sync): {end - start:.2f}s")
    print()


# ========================
# ASYNCHRONOUS EXAMPLE
# ========================

async def async_job(job_name, duration):
    print(f"[ASYNC] {job_name} started...")
    await asyncio.sleep(duration)   # non-blocking, other tasks continue
    print(f"[ASYNC] {job_name} finished! (took {duration}s)")

async def run_async_jobs():
    print("=" * 45)
    print("   ASYNCHRONOUS Jobs (all at once)")
    print("=" * 45)
    start = time.time()

    # All jobs start together
    await asyncio.gather(
        async_job("Job_A", 2),
        async_job("Job_B", 1),
        async_job("Job_C", 3),
    )

    end = time.time()
    print(f"Total time (async): {end - start:.2f}s")
    print("Notice: async is much faster!")


# ========================
# MAIN
# ========================

if __name__ == "__main__":
    # Run sync jobs first
    run_sync_jobs()

    # Then run async jobs - notice the time difference!
    asyncio.run(run_async_jobs())