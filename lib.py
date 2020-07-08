def get_thumbnail(media_url):
    if media_url[-4:] == ".gif":
        return media_url
    elif "youtube" in media_url:
        youtube_id = media_url.split("watch?v=")[1]
        youtube_id = youtube_id.split("?t=")[0]
        return f"https://img.youtube.com/vi/{youtube_id}/1.jpg"
    else:
        raise "UnsupportedUrl: Url is not a Gif nor a Youtube video"
