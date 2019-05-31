from google_images_search import GoogleImagesSearch
from PIL import Image as PImage
# if you don't enter api key and cx, the package will try to search
# them from environment variables GCS_DEVELOPER_KEY and GCS_CX
CSE_ID = "007178062085341727974:m2f5nw3vigi"
API_KEY = "AIzaSyDw4F8aq10iiLzWh7AsdbLo-PGOYR-YIzU"
gis = GoogleImagesSearch(API_KEY, CSE_ID)



# Returns a list of url of images
def search(keyword, number_results):
    _search_params = {
    'q': keyword,
    'num':number_results,
    # 'fileType': 'gif',
    # 'imgType': 'clipart|face|lineart|news|photo',
    'imgSize': 'medium',
    # 'searchType': 'image',
    # 'imgDominantColor': 'black|blue|brown|gray|green|pink|purple|teal|white|yellow'
}
    _path_to_dir='/Users/max/Documents/GitHub/wikipython-server/img'
    list_img = []
    gis.search(search_params=_search_params)
    for image in gis.results():
        # image.download(_path_to_dir)
        list_img.append(image.url)
    return list_img

    
