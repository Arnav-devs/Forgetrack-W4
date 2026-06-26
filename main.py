import time
from pathlib import Path

import pandas as pd
import requests
import schedule
from bs4 import BeautifulSoup

CSV_FILE = "internship_results.csv"
BASE_URL = "https://internshala.com"


def get_page(keyword):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    address = f"{BASE_URL}/internships/keywords-{keyword}/"

    response = requests.get(address, headers=headers, timeout=15)
    response.raise_for_status()

    return response.text


def parse_page(html):

    soup = BeautifulSoup(html, "html.parser")

    cards = soup.find_all("div", internshipid=True)

    internships = []

    for card in cards:

        try:
            title = "N/A"
            company = "N/A"
            location = "N/A"
            link = "N/A"
            posted = "Not Available"

            title_element = card.find("a", class_="job-title-href")
            if title_element:
                title = title_element.get_text(strip=True)
                link = BASE_URL + title_element["href"]

            company_element = card.find("p", class_="company-name")
            if company_element:
                company = company_element.get_text(strip=True)

            location_element = card.find("div", class_="row-1-item locations")
            if location_element:
                location = location_element.get_text(strip=True)

            date_element = card.find("div", class_="status-success")
            if date_element:
                posted = date_element.get_text(strip=True)

            internships.append({
                "Title": title,
                "Company": company,
                "Location": location,
                "Link": link,
                "Date Posted": posted
            })

        except Exception as e:
            print("Skipped one internship:", e)

    return internships


def save_results(records):

    if not records:
        print("\nNo internships found.")
        return

    new_df = pd.DataFrame(records).drop_duplicates()

    if Path(CSV_FILE).exists():

        old_df = pd.read_csv(CSV_FILE)

        new_df = (
            pd.concat([old_df, new_df], ignore_index=True)
            .drop_duplicates()
        )

    new_df.to_csv(CSV_FILE, index=False)

    print("\nSaved Successfully!")
    print(f"Records in file : {len(new_df)}")
    print(f"Output file     : {CSV_FILE}")


def scrape(keyword=None):

    print("\n========== Internship Scraper ==========\n")

    if keyword is None:
        keyword = input("Enter skill keyword: ").strip().lower()

    try:

        print("Fetching internships...")

        html = get_page(keyword)

        time.sleep(1)

        data = parse_page(html)

        print(f"Found {len(data)} internships.")

        save_results(data)

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except requests.exceptions.ConnectionError:
        print("Internet connection unavailable.")

    except Exception as e:
        print("Error:", e)


def scheduled_job(keyword):

    print("\nRunning scheduled scrape...\n")

    scrape(keyword)


def menu():

    print("\n===== MENU =====")
    print("1. Run Once")
    print("2. Daily Automation")

    choice = input("\nChoose an option: ").strip()

    if choice == "1":

        scrape()

    elif choice == "2":

        keyword = input("Enter skill keyword: ").strip().lower()

        scheduled_job(keyword)

        schedule.every().day.at("10:00").do(scheduled_job, keyword)

        print("\nAutomation started.")
        print("Runs every day at 10:00 AM.")
        print("Press Ctrl+C to stop.\n")

        try:
            while True:
                schedule.run_pending()
                time.sleep(60)

        except KeyboardInterrupt:
            print("\nAutomation stopped.")

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    menu()