import brisque as c

#Carga de imágen
#%matplotlib inline
c.plt.rcParams["figure.figsize"] = 12, 9

url = 'https://r0k.us/graphics/kodak/kodak/kodim05.png'
image = c.load_image(url)
gray_image = c.skimage.color.rgb2gray(image)

_ = c.skimage.io.imshow(image)

#calculo de coeficientes
#%%time

mscn_coefficients = c.calculate_mscn_coefficients(gray_image, 7, 7/6)
coefficients = c.calculate_pair_product_coefficients(mscn_coefficients)

#%matplotlib inline
c.plt.rcParams["figure.figsize"] = 12, 11

for name, coeff in coefficients.items():
    c.plot_histogram(coeff.ravel(), name)

c.plt.axis([-2.5, 2.5, 0, 1.05])
c.plt.legend()
c.plt.show()


