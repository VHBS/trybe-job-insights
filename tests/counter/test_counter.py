from src.counter import count_ocurrences


def test_counter():
    "Retorna o valor correto de quantas vezes javascript foi mencionado"
    assert count_ocurrences("src/jobs.csv", "Javascript") == 122
    assert count_ocurrences("src/jobs.csv", "javascript") == 122
    assert count_ocurrences("src/jobs.csv", "Python") == 1639
    assert count_ocurrences("src/jobs.csv", "python") == 1639
