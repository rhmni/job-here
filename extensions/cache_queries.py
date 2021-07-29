from django.conf import settings
from django.core.cache import cache

from app_job.models import Job


def cache_jobs(ttl=settings.JOBS_TTL_CACHE):
    if 'jobs' in cache:
        jobs = cache.get('jobs')
    else:
        jobs = Job.actived.all()
        cache.set('jobs', jobs, timeout=ttl)

    return jobs
