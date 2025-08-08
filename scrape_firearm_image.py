from icrawler.builtin import GoogleImageCrawler


def scrape_firearm_images():
    """
    Scrape firearm images from Google Images.

    :param query: Search query for the images.
    :param max_num: Maximum number of images to scrape.
    """
    max_num = 150  # Set the maximum number of images to scrape per query
    crawler = GoogleImageCrawler(storage={"root_dir": "data/raw_images"})
    crawler.crawl(keyword="firearm", max_num=max_num)
    crawler.crawl(keyword="gun", max_num=max_num)
    crawler.crawl(keyword="pistol", max_num=max_num)
    crawler.crawl(keyword="rifle", max_num=max_num)
    crawler.crawl(keyword="shotgun", max_num=max_num)
    crawler.crawl(keyword="revolver", max_num=max_num)
    crawler.crawl(keyword="assault rifle", max_num=max_num)
    crawler.crawl(keyword="machine gun", max_num=max_num)
    crawler.crawl(keyword="sniper rifle", max_num=max_num)
    crawler.crawl(keyword="handgun", max_num=max_num)
    crawler.crawl(keyword="concealed gun", max_num=max_num)
    crawler.crawl(keyword="firearm accessories", max_num=max_num)
    crawler.crawl(keyword="firearm in dark environment", max_num=max_num)
    crawler.crawl(keyword="firearm in hand", max_num=max_num)
    crawler.crawl(keyword="firearm in movies", max_num=max_num)
    crawler.crawl(keyword="firearms in johnwick", max_num=max_num)
    crawler.crawl(keyword="firearm in action movies", max_num=max_num)
    crawler.crawl(keyword="firearm with scope", max_num=max_num)
    crawler.crawl(keyword="gun on wooden table", max_num=max_num)
    crawler.crawl(keyword="pistol in holster", max_num=max_num)
    crawler.crawl(keyword="rifle close up", max_num=max_num)
    crawler.crawl(keyword="gun silhouette", max_num=max_num)
    crawler.crawl(keyword="person aiming handgun", max_num=max_num)
    crawler.crawl(keyword="firearm partially hidden", max_num=max_num)
    crawler.crawl(keyword="gun with suppressor", max_num=max_num)
    crawler.crawl(keyword="firearm with flashlight", max_num=max_num)
    crawler.crawl(keyword="disassembled gun parts", max_num=max_num)


if __name__ == "__main__":
    scrape_firearm_images()
    print("Image scraping completed.")
