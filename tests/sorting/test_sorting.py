from src.sorting import sort_by


def test_sort_by_criteria():
    jobs_list = [
        {
            "min_salary": 44587,
            "max_salary": 82162,
            "rating": 4,
            "date_posted": "2020-05-08",
            "id": 3
        },
        {
            "min_salary": 125410,
            "max_salary": 212901,
            "rating": 3,
            "date_posted": "2020-04-28",
            "id": 4
        },
        {
            "min_salary": 94715,
            "max_salary": 103279,
            "rating": 4.9,
            "date_posted": "2020-05-05",
            "id": 5
        }]

    sort_by(jobs_list, "min_salary")
    assert jobs_list[0]["min_salary"] == 44587

    sort_by(jobs_list, "max_salary")
    assert jobs_list[0]["max_salary"] == 212901

    sort_by(jobs_list, "date_posted")
    assert jobs_list[0]["date_posted"] == "2020-05-08"
