# DatasetHelper
This Python script uses the icrawler library to automate image downloading from Google Images. It fetches up to 100 images based on a predefined search query, saves them in a specified folder (downloaded_images), and runs without user interaction.


# Image Downloader Script

## Overview
This script automates the process of downloading images from Google Images based on a predefined search query. It uses the `icrawler` library to fetch and store up to 100 images in a specified directory, with no user interaction required.

---

## Features
- Automated image crawling and downloading.
- Fetches up to 100 images for a specific search query.
- Organizes downloaded images in a dedicated folder.
- Requires no runtime user input; the search query is predefined in the code.

---

## Prerequisites
1. Python 3.7 or higher installed.
2. Required Python libraries:
   - `icrawler`

Install the library using:
```bash
pip install icrawler
```

## Usage
1. Clone or download this repository.
2. Open the script file.
3. Modify the `query` variable in the script to your desired search term. Example:
```Python
query = "beautiful landscapes"
```
4. Run the script:
```bash
python script_name.py
```
5. The images will be downloaded and saved in the `downloaded_images` directory.

---
## Code Structure
- `query:` The predefined search term for Google Images.
- `save_dir:` The directory where downloaded images will be stored.
- `GoogleImageCrawler:` Handles the crawling and downloading process.
---

## Customization
- Change the number of images to download: Modify the max_num parameter in the `crawler.crawl()` method.
```python
crawler.crawl(keyword=query, max_num=50)  # Downloads 50 images
```
- Change the save directory: Update the save_dir variable to your desired folder path.
```python
save_dir = "my_images"
```
---
## Example Output
- Images will be saved in the folder:
```markdown
downloaded_images/
    image_1.jpg
    image_2.jpg
    ...
    image_100.jpg
```
---
## Limitations
- The script relies on Google Images, so results may vary based on search term relevance.
- Avoid excessive use to prevent IP blocking by Google.
---
## License
- This script is open-source and available for personal and educational use.

```vbnet
Let me know if you need further adjustments!
```
