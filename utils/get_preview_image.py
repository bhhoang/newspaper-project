import requests
import os,shutil,sys

## This function is used to get the preview image of an article and save it to the ../cache/articles/article_{article_id}/preview_image.jpg

def getimage_and_setname(image_url:str, article_id:int = 0) -> str:
    if not os.path.exists('./cache/articles'):
        os.mkdir('./cache/articles')
    if not os.path.exists(f'./cache/articles/article_{article_id}'):
        os.mkdir(f'./cache/articles/article_{article_id}')
    if image_url.find('http') == -1:
        shutil.copyfile(image_url, f'./cache/articles/article_{article_id}/preview_image.jpg')
    if not os.path.exists(f'./cache/articles/article_{article_id}/preview_image.jpg'):
        with open(f'./cache/articles/article_{article_id}/preview_image.jpg', 'wb') as f:
            f.write(requests.get(image_url).content)
    return f'./cache/articles/article_{article_id}/preview_image.jpg'