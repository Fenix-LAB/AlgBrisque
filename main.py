from brisque import *

#Carga de imágen
#%matplotlib inline
plt.rcParams["figure.figsize"] = 12, 9

url = 'https://r0k.us/graphics/kodak/kodak/kodim05.png'
image = c.load_image(url)
gray_image = c.skimage.color.rgb2gray(image)

_ = skimage.io.imshow(image)

#calculo de coeficientes
#%%time

mscn_coefficients = calculate_mscn_coefficients(gray_image, 7, 7/6)
coefficients = calculate_pair_product_coefficients(mscn_coefficients)

#%matplotlib inline
plt.rcParams["figure.figsize"] = 12, 11

for name, coeff in coefficients.items():
    plot_histogram(coeff.ravel(), name)

plt.axis([-2.5, 2.5, 0, 1.05])
plt.legend()
plt.show()


