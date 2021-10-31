# In this question, you will download 10 images from the Picsum API to your
# current directory. Currently, it takes eight seconds to download all 10
# images, but with threading, it takes two seconds. Use the hints in the main
# method to download the 10 images.

from concurrent.futures import ThreadPoolExecutor
from requests import get # you will need to pip install this
from time import perf_counter

def download_img(url):
    img_bytes = get(url).content
    img_name = ''.join(url.split('/')[4:])
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as f:
        f.write(img_bytes)
        print(f'{img_name} was downloaded.')

def main():
    start = perf_counter()
    
    req = get('https://picsum.photos/v2/list?limit=10')
    download_urls = [url['download_url'] for url in req.json()]
    
    for img in  download_urls:
        download_img(img)
        
    # Instead of using the loop above, refactor to use threads.    
    # Use a context manager with ThreadPoolExecutor() as executor
    # Call the executor's map method - pass in a function & iterable

    finish = perf_counter()
    
    elapsed_time = round(finish - start, 2)
    
    print(f'Process finished in {elapsed_time} second(s)')

if __name__ == '__main__':
    main()
