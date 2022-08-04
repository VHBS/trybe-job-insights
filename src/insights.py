from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    result = set()
    for job in jobs:
        result.add(job["job_type"])
    return list(result)


def filter_by_job_type(jobs, job_type):
    result = []
    for job in jobs:
        if job['job_type'] == job_type:
            result.append(job)
    return result


def get_unique_industries(path):
    jobs = read(path)
    result = set()
    for job in jobs:
        if job["industry"] != "":
            result.add(job["industry"])
    return list(result)


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    jobs = read(path)
    result = 0
    for job in jobs:
        if job["max_salary"].isdigit() and int(job["max_salary"]) > result:
            result = int(job["max_salary"])
    return result


def get_min_salary(path):
    jobs = read(path)
    result = 100000
    for job in jobs:
        if job["min_salary"].isdigit() and int(job["min_salary"]) < result:
            result = int(job["min_salary"])
    return result


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
