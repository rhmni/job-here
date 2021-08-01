from datetime import datetime, timedelta

from celery import shared_task
from django.conf import settings

from app_job.models import Job


@shared_task
def expire_jobs():
    """
        Expire jobs
    """

    Job.actived.filter(
        register_date__lte=datetime.now() - timedelta(days=settings.EXPIRE_JOBS_DAY)
    ).update(
        is_expire=True,
    )
