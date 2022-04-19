import cv2
import glob
import argparse
import subprocess
from paths import *




def get_coordinates_from_file(file_nane):
    coords_list=[]

    file_coords=open(file_nane,'r')

    for line in file_coords.readlines():

        line_splits=line.split(" ")
        state_name=states_names_dict[int(line_splits[0])]

        x_center=float(line_splits[1])
        y_center=float(line_splits[2])
        width=float(line_splits[3])
        height=float(line_splits[4])

        x1, y1 = x_center-width/2, y_center-height/2
        x2, y2 = x_center+width/2, y_center+height/2
        coords_list.append([state_name,x1,y1,x2,y2])

    return coords_list


def visualize():
    for image_path in glob.glob(images_path+"*.png"):

        img = cv2.imread(image_path, 1)

        coord_file_path=image_path.replace("png","txt")
        coords_list=get_coordinates_from_file(coord_file_path)
        #
        height,width,_=(img.shape)



        x_offset=0
        for coord_list in coords_list:
            state_name,x1, y1, x2, y2 =coord_list
            print(coord_list)
            cv2.rectangle(img, (int(x1*width), int(y1*height)), (int(x2*width), int(y2*height)), (255, 0, 0), 2)
            cv2.putText(img, state_name, (int(x1*width)+x_offset, int(y1*height)+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,99,71), 2)
            x_offset+=45
        cv2.imshow("", img)
        k=cv2.waitKey(0)
        if k & 0xFF == ord("q"):

            break



def test_detector():


    custom_images_path=vars(args)['test']
    dur_command="%s detector test %s %s %s    < %s  " %(detector_exec_path,data_file_path,conf_file_path,weights_path,custom_images_path)
    res=subprocess.call(dur_command, shell=True)


def main_function(args):
    print(vars(args))
    if(vars(args)['visualize']==True):
        visualize()
    elif(vars(args)['test'] is not None):
        test_detector()

if __name__ == '__main__':


    parser = argparse.ArgumentParser(description='Create a ArcHydro schema')
    parser.add_argument('-v','--visualize', required=False,action='store_true',
                        help='visualize dataset')
    parser.add_argument('--test',required=False,
                        help='test on custom images')

    args = parser.parse_args()
    main_function(args)







