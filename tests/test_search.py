"""
 Test search duckduckgo
"""
from tests.conftest import browser
from main.keyword import Keyword

def test_search_google(browser):
    keyword = Keyword(browser)
    keyword.go_to_url("https://www.google.com/")
    keyword.set_text("//textarea[@title='Search' or @title='Telusuri']","jakarta")
    keyword.click("(//input[@aria-label='Google Search' or @aria-label='Penelusuran Google'])[1]")

    strValue = keyword.get_text("(//a/h3)[1]")
    print(strValue)
    assert "jakarta" in strValue.lower()

    listValue = keyword.get_all_text("//a/h3")
    for strValue in listValue:
        print(strValue)
