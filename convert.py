import os
from xml.dom import minidom

country_name = 'Czech'
lut = {}
lut["D00"] = 0
lut["D10"] = 1
lut["D20"] = 2
lut["D40"] = 3


def convert_coordinates(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_xml2yolo(lut):
    xml_dir = f"../RDD2022_{country_name}/{country_name}/train/annotations/xmls"
    for fname in os.listdir(xml_dir):
        if fname.endswith(".xml"):
            xml_path = os.path.join(xml_dir, fname)
            xmldoc = minidom.parse(xml_path)
            fname_out = f"../RDD2022_{country_name}/{country_name}/train/labels/{fname[:-4]}.txt"

            with open(fname_out, "w") as f:
                itemlist = xmldoc.getElementsByTagName('object')
                size = xmldoc.getElementsByTagName('size')[0]
                width = int((size.getElementsByTagName('width')[0]).firstChild.data)
                height = int((size.getElementsByTagName('height')[0]).firstChild.data)

                for item in itemlist:
                    # get class label
                    classid = (item.getElementsByTagName('name')[0]).firstChild.data
                    if classid in lut:
                        label_str = str(lut[classid])

                        # get bbox coordinates
                        xmin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmin')[0]).firstChild.data
                        ymin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymin')[0]).firstChild.data
                        xmax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmax')[0]).firstChild.data
                        ymax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymax')[0]).firstChild.data
                        b = (float(xmin), float(xmax), float(ymin), float(ymax))
                        bb = convert_coordinates((width, height), b)
                        f.write(label_str + " " + " ".join([("%.6f" % a) for a in bb]) + '\n')

            print("wrote %s" % fname_out)


def main():
    convert_xml2yolo(lut)


if __name__ == '__main__':
    main()
