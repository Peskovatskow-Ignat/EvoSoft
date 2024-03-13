from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
import csv
from typing import Iterable


def get_page(url: str) -> str | None:
    """
    Args:
        url (str): _description_

    Returns:
        str | None: _description_
    """
    try:
        driver.get(url)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/header/nav/div[2]/div/div/ul/li[3]/a")
            )
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//html/body/header/nav/div[2]/div/div/ul/li[3]/div/div[1]/div/div[1]/ul/li[1]/a",
                )
            )
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[11]/div/section/div/div/div/div/div/div/div[3]/div/table/tbody",
                )
            )
        )

        data_table = driver.find_element(
            By.XPATH,
            "/html/body/div[11]/div/section/div/div/div/div/div/div/div[3]/div/table/tbody",
        )

        return data_table.get_attribute("outerHTML")
    except (TimeoutException, NoSuchElementException) as e:
        print(f"An error occurred: {e}")

        return None


def generate_csv_data(page: str) -> Iterable[list[str]]:
    """
    Args:
        page (str): _description_

    Returns:
        Iterable[list[str]]: _description_

    Yields:
        Iterator[Iterable[list[str]]]: _description_
    """
    soup = BeautifulSoup(page, "html.parser")
    contents = soup.find_all("tr")

    for content in range(len(contents) - 1):
        name = contents[content].find("a").text.strip()
        price = (
            contents[content]
            .find("td", class_="bold text-right")
            .text.strip()
            .replace(",", "")
        )
        yield [name, price]


if __name__ == "__main__":
    options = Options()
    driver = webdriver.Edge(options=options)
    data_page = get_page("https://www.nseindia.com/")
    if data_page is None:
        exit()

    driver.quit()

    with open("data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONE, escapechar=" ")

        writer.writerows(generate_csv_data(data_page))
