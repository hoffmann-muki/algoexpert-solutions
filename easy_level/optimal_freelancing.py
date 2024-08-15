# O(nlogn) time | O(1) space
def optimalFreelancing(jobs):
    if len(jobs) == 0:
        return 0
    # sort jobs by payment
    jobs.sort(key=lambda x: x["payment"], reverse=True)
    week = 7
    array = [False for _ in range(week)]
    maxPayment = 0
    for job in jobs:
        deadline = job["deadline"] - 1
        if deadline >= week:
            slot = week-1
        else:
            slot = deadline
        # attempt to place at latest possible value
        if slot >= 0:
            if not array[slot]:
                maxPayment += job["payment"]
                array[slot] = True
            else:
                # try placing at latest possible value before deadline
                slot -= 1
                while slot >= 0:
                    if not array[slot]:
                        maxPayment += job["payment"]
                        array[slot] = True
                        break
                    slot -= 1
    return maxPayment
