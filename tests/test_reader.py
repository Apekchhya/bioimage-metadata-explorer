from bioimage_metadata.reader import read_image_info


image = "data/sample_images/tubhiswt_C0.ome.tif"

result = read_image_info(image)

print(result)