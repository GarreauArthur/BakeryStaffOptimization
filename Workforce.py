class Workforce:
    """
    A collection of workers
    """
    def __init__(self):
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)

    def get_best_worker_for_job(self, job, day, start, end):
        """
        Go through the list of workers, compute a score and return the worker
        with the best score
        """

        job_matching_importance = 10
        hours_worked_importance = 1
        scores = [0]*len(self.workers) # list of zeros
        
        for worker in self.workers:
            
            index = self.workers.index(worker)

            if worker.schedule.is_busy(day, start, end):
                scores[index] = 0   
                break

            #scores[index] += worker.remaining_hours/worker.normal_hours*job_matching_importance
            if worker.remaining_hours <= 0:
                scores[index] -= 10
            else:
                scores[index] += worker.remaining_hours

            if job in worker.jobs:
                scores[index] += 100 #hours_worked_importance/(worker.jobs.index(job)+1) # lol wtf
            else:
                scores[index] -= 100
            
            # print(worker.first_name, scores[self.workers.index(worker)])
        return self.workers[scores.index(max(scores))]

    def get_worker_by_id(self, worker_id):
        for worker in self.workers:
            if worker.worker_id == worker_id:
                return worker
