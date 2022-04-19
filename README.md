# OSDD


![picture alt](images/sample.png "Title is optional")


This project contains the  **Object State Detection Dataset (OSDD)**. The images along with the corresponding annotations can be found in the following links:

- **TRAIN** : https://drive.google.com/file/d/1nZK8wYqShCtZf6jjNkOeOQuXHLC41HCI/view?usp=sharing  
- **VALIDATION** :  https://drive.google.com/file/d/1v1eajK8IwcYSpg_iI8y4uhSnQUh_VmiG/view?usp=sharing   
- **TEST** : https://drive.google.com/file/d/1AsMkY08ZEBTwKYP8TpNcBqTDWh7Op-Sx/view?usp=sharing  
- **DATA FILE** :https://drive.google.com/file/d/1nvUEmFudYMYSvfSiabOCpuPSMAAFUSC4/view?usp=sharing


In order to test your custom images the weights and the configuration file of the network must
be downloaded:
- **WEIGHTS** : https://drive.google.com/file/d/1KIOoVQCdBOtJJLOgL829jiN1pKBxVwTQ/view?usp=sharing
- **CONFIG FILE** : https://drive.google.com/file/d/1jr-YxiP4xUhxpyT43f_xrl-qmMmEjkEs/view?usp=sharing


Plase note the that the annotations follow the YoloV4 format.


# Requirements


- **Python >= 3.6**
- **A Linux-based environment**

- **[OpenCV](https://opencv.org/)**

- **[YoloV4](https://github.com/AlexeyAB/darknet)**


# How to visualize the dataset 


1. Download the images from the links that are presented above. 
2. Change the variable **images_path**  in the **src/paths.py**  so that it points to the directory
where the images are stored (If you have downloaded all three parts of images,
i.e. train,validation and test, 
you have to point to the path of the part you want to visualize).
3. Run the following command in the terminal:
```python
python src/main.py --visualize
```


# How to test the state detector on custom images


1. Download the weights and data and configuration file  from the links that are presented above.
2. Change the variables **weights_path**,**conf_file_path** and **data_file_path**
in the **src/paths.py**  so that they points to the directory
      where the previous files were stored.
3. Install the YoloV4 in your machine as explained in this [link](https://github.com/AlexeyAB/darknet#how-to-compile-on-linuxmacos-using-cmake).
4. Change the variable **detector_exec_path**  in the **src/paths.py**  so that it points to the directory
   where the executable file of Yolo is located. 
5. Run the following command in the terminal:
```python
python src/main.py --test path_where_custom_images_are_found
```



# Citation

If you use our annotations in your research or wish to refer to the baseline results, please use the following BibTeX entry.

@inproceedings{gouidis2022,
title={ Detecting Object States vs Detecting Objects: A New Dataset and a Quantitative Experimental Study},
author={Gouidis, F. and  Patkos, T. and Argyros, A. and Plexousakis, D. },
booktitle={ Proceedings of the 17th International Joint Conference on Computer Vision, Imaging and Computer Graphics Theory and Applications  (VISAPP)},
year={2022},
volume={5},
pages={590--600}
}
