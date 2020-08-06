from lib_crawl_job.indeed_jobs import get_jobs as get_indeed_jobs
from lib_crawl_job.so_jobs import get_jobs as get_so_jobs
from lib_crawl_job.save import save_to_file


indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()
jobs = indeed_jobs + so_jobs
save_to_file(jobs)

