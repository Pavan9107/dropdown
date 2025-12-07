def test_launch_google(driver):
    driver.get('https://google.com')
    assert driver.title == 'Google'

