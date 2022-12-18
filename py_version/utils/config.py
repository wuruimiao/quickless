import yaml

with open("config.yaml") as f:
    _config = yaml.safe_load(f)


download_page = _config["download_page"]
video_page = _config["video_page"]
print(download_page, video_page)
