from src.sorting import sort_by
import pytest


mock_list_jobs = [
    {
        "date_posted": "2020-04-25",
        "max_salary": "114484",
        "min_salary": "91572",
    },
    {
        "date_posted": "2020-05-08",
        "max_salary": "104769",
        "min_salary": "64829",
    },
    {
        "date_posted": "2020-04-28",
        "max_salary": "87057",
        "min_salary": "65665",
    },
    {
        "date_posted": "2020-04-27",
        "max_salary": "162105",
        "min_salary": "84236",
    },
]

mock_list_jobs_date_posted = [
    {
        "date_posted": "2020-05-08",
        "max_salary": "104769",
        "min_salary": "64829",
    },
    {
        "date_posted": "2020-04-28",
        "max_salary": "87057",
        "min_salary": "65665",
    },
    {
        "date_posted": "2020-04-27",
        "max_salary": "162105",
        "min_salary": "84236",
    },
    {
        "date_posted": "2020-04-25",
        "max_salary": "114484",
        "min_salary": "91572",
    },
]

mock_list_jobs_max_salary = [
    {
        "date_posted": "2020-04-27",
        "max_salary": "162105",
        "min_salary": "84236",
    },
    {
        "date_posted": "2020-04-25",
        "max_salary": "114484",
        "min_salary": "91572",
    },
    {
        "date_posted": "2020-05-08",
        "max_salary": "104769",
        "min_salary": "64829",
    },
    {
        "date_posted": "2020-04-28",
        "max_salary": "87057",
        "min_salary": "65665",
    },
]

mock_list_jobs_min_salary = [
    {
        "date_posted": "2020-05-08",
        "max_salary": "104769",
        "min_salary": "64829",
    },
    {
        "date_posted": "2020-04-28",
        "max_salary": "87057",
        "min_salary": "65665",
    },
    {
        "date_posted": "2020-04-27",
        "max_salary": "162105",
        "min_salary": "84236",
    },
    {
        "date_posted": "2020-04-25",
        "max_salary": "114484",
        "min_salary": "91572",
    },
]


def test_sort_by_criteria():
    sort_by(mock_list_jobs, "max_salary")
    assert mock_list_jobs == mock_list_jobs_max_salary

    sort_by(mock_list_jobs, "min_salary")
    assert mock_list_jobs == mock_list_jobs_min_salary

    sort_by(mock_list_jobs, "date_posted")
    assert mock_list_jobs == mock_list_jobs_date_posted

    with pytest.raises(ValueError, match="invalid sorting criteria: wrok_key"):
        sort_by(mock_list_jobs, "wrok_key")
