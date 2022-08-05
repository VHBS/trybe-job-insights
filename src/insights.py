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
    result = []
    for job in jobs:
        if job['industry'] == industry:
            result.append(job)
    return result


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
    if job.get("min_salary") is None or job.get("max_salary") is None:
        raise ValueError("Salario minimo ou máximo não informado")

    elif type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError("Salario minimo ou máximo não numerico")

    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("Salario minimo maior que o salario máximo")

    else:
        return matches_salary_range_check_salary(job, salary)


def matches_salary_range_check_salary(job, salary):
    if type(salary) != int:
        raise ValueError("Salario não numerico")
    elif job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


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
