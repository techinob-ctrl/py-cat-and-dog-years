from app import main


def test_should_return_zero_when_ages_are_below_15() -> None:
    assert main.get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_ages_are_between_15_and_23() -> None:
    assert main.get_human_age(15, 15) == [1, 1]
    assert main.get_human_age(23, 23) == [1, 1]


def test_should_return_two_at_24_years_for_both() -> None:
    assert main.get_human_age(24, 24) == [2, 2]


def test_should_increase_cat_human_age_every_4_years_after_24() -> None:
    assert main.get_human_age(27, 24) == [2, 2]
    assert main.get_human_age(28, 24) == [3, 2]


def test_should_increase_dog_human_age_every_5_years_after_24() -> None:
    assert main.get_human_age(24, 28) == [2, 2]
    assert main.get_human_age(24, 29) == [2, 3]


def test_should_convert_large_ages() -> None:
    assert main.get_human_age(100, 100) == [21, 17]
