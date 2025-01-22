from icrawler.builtin import GoogleImageCrawler

def download_images(query, max_images, save_dir):
    # Set up the GoogleImageCrawler with the target save directory
    crawler = GoogleImageCrawler(storage={"root_dir": save_dir})
    # Crawl and download images based on the query
    crawler.crawl(keyword=query, max_num=max_images)

def main():
    # Define your search query directly here
    query = "beautiful landscapes"  # Replace with your desired search term
    save_dir = "downloaded_images"  # Directory where images will be saved
    download_images(query, 100, save_dir)
    print(f"Images downloaded to {save_dir}")

if __name__ == "__main__":
    main()
