import requests

#list of urls to reference
kitten_picture_urls = [
    'https://loremflickr.com/320/240',
    'https://loremflickr.com/cache/resized/65535_53496367964_e68c1c8cb8_320_240_nofilter.jpg',
    'https://loremflickr.com/cache/resized/65535_52925571326_585fc45528_n_320_240_nofilter.jpg',
    'https://loremflickr.com/cache/resized/65535_53800837363_86a2a43974_n_320_240_nofilter.jpg'
]

for index, url in enumerate(kitten_picture_urls):
    response = requests.get(url)

    filename = f'kitten_{index}.jpg'
    with open(filename, 'wb') as file:
        for chunk in response.iter_content():
            file.write(chunk)

