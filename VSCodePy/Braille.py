import PIL.Image

# 64 symbols
brailles = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢',
            '⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅',
            '⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵','⠪','⠳','⠻','⠘','⠸']

# corresponding unicodes for Braille symbols
unicodes = [u'\u2800',u'\u282e',u'\u2810',u'\u283c',u'\u282b',u'\u2829',u'\u282f',u'\u2804',
            u'\u2837',u'\u283e',u'\u2821',u'\u282c',u'\u2820',u'\u2824',u'\u2828',u'\u280c',
            u'\u2834',u'\u2802',u'\u2806',u'\u2812',u'\u2832',u'\u2822',u'\u2816',u'\u2836',
            u'\u2826',u'\u2814',u'\u2831',u'\u2830',u'\u2823',u'\u283f',u'\u281c',u'\u2839',
            u'\u2808',u'\u2801',u'\u2803',u'\u2809',u'\u2819',u'\u2811',u'\u280b',u'\u281b',
            u'\u2813',u'\u280a',u'\u281a',u'\u2805',u'\u2807',u'\u280d',u'\u281d',u'\u2815',
            u'\u280f',u'\u281f',u'\u2817',u'\u280e',u'\u281e',u'\u2825',u'\u2827',u'\u283a',
            u'\u282d',u'\u283d',u'\u2835',u'\u282a',u'\u2833',u'\u283b',u'\u2818',u'\u2838']


# corresponding bitwise matrix for Braille symbols
matrixcodes = [
    [[0, 0], [0, 0], [0, 0]],[[0, 1], [1, 0], [1, 1]],[[0, 0], [0, 1], [0, 0]],[[0, 1], [0, 1], [1, 1]],
    [[1, 1], [1, 0], [0, 1]],[[1, 1], [0, 0], [0, 1]],[[1, 1], [1, 0], [1, 1]],[[0, 0], [0, 0], [1, 0]],
    [[1, 0], [1, 1], [1, 1]],[[0, 1], [1, 1], [1, 1]],[[1, 0], [0, 0], [0, 1]],[[0, 1], [0, 0], [1, 1]],
    [[0, 0], [0, 0], [0, 1]],[[0, 0], [0, 0], [1, 1]],[[0, 1], [0, 0], [0, 1]],[[0, 1], [0, 0], [1, 0]],
    [[0, 0], [0, 1], [1, 1]],[[0, 0], [1, 0], [0, 0]],[[0, 0], [1, 0], [1, 0]],[[0, 0], [1, 1], [0, 0]],
    [[0, 0], [1, 1], [0, 1]],[[0, 0], [1, 0], [0, 1]],[[0, 0], [1, 1], [1, 0]],[[0, 0], [1, 1], [1, 1]],
    [[0, 0], [1, 0], [1, 1]],[[0, 0], [0, 1], [1, 0]],[[1, 0], [0, 1], [0, 1]],[[0, 0], [0, 1], [0, 1]],
    [[1, 0], [1, 0], [0, 1]],[[1, 1], [1, 1], [1, 1]],[[0, 1], [0, 1], [1, 0]],[[1, 1], [0, 1], [0, 1]],
    [[0, 1], [0, 0], [0, 0]],[[1, 0], [0, 0], [0, 0]],[[1, 0], [1, 0], [0, 0]],[[1, 1], [0, 0], [0, 0]],
    [[1, 1], [0, 1], [0, 0]],[[1, 0], [0, 1], [0, 0]],[[1, 1], [1, 0], [0, 0]],[[1, 1], [1, 1], [0, 0]],
    [[1, 0], [1, 1], [0, 0]],[[0, 1], [1, 0], [0, 0]],[[0, 1], [1, 1], [0, 0]],[[1, 0], [0, 0], [1, 0]],
    [[1, 0], [1, 0], [1, 0]],[[1, 1], [0, 0], [1, 0]],[[1, 1], [0, 1], [1, 0]],[[1, 0], [0, 1], [1, 0]],
    [[1, 1], [1, 0], [1, 0]],[[1, 1], [1, 1], [1, 0]],[[1, 0], [1, 1], [1, 0]],[[0, 1], [1, 0], [1, 0]],
    [[0, 1], [1, 1], [1, 0]],[[1, 0], [0, 0], [1, 1]],[[1, 0], [1, 0], [1, 1]],[[0, 1], [1, 1], [0, 1]],
    [[1, 1], [0, 0], [1, 1]],[[1, 1], [0, 1], [1, 1]],[[1, 0], [0, 1], [1, 1]],[[0, 1], [1, 0], [0, 1]],
    [[1, 0], [1, 1], [0, 1]],[[1, 1], [1, 1], [0, 1]],[[0, 1], [0, 1], [0, 0]],[[0, 1], [0, 1], [0, 1]]
]

def image_resize(image, new_width=100):
    width, height= image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    image_resize = image.resize((new_width, new_height))
    return (image_resize)
     
def grayscale(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
def pixelBraille(image):
    pixels = image.getdata()
    characters = "".join([brailles[pixels//25] for pixels in pixels])
    return (characters)


    
def main(new_width):
    #attempt to open image from user-input
    path = input("enter a valid pathway to an image:\n")
    try: 
        image = PIL.Image.open(path)
    except:
        print(path, " is not a valid pathname")
     
    new_image_data = pixelBraille(grayscale(image_resize(image))) 
    
    pixel_count = len(new_image_data)
    braille_image= "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count,new_width))
    
    print(braille_image)
    
    with open("braille_image.txt", "w") as f:
        f.write(braille_image)

main(100)