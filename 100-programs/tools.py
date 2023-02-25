import matplotlib.pyplot as plt

def show_image(image):
    if image.ndim == 2:
        plt.imshow(image, cmap=plt.cm.gray)
    else:
        plt.imshow(image)
    plt.show()