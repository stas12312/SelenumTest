from .core.driver import get_driver


def test_main_page():
    driver = get_driver()

    driver.get("https://test.mywishlists.ru")

    assert driver.title == "MyWishlists - сервис для составления вишлистов"
