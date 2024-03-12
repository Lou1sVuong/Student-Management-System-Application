
  <h1 align="center">
  - Student Management System Application -
</h1>

## Introduction
<p>This program was written by me at the end of my first year of university, it is mainly written in python and its UI is supported by the QT designer to make it easy. Even though my code can run all the features, it doesn't look pretty when looking at it haha, if you have any way to make the main.py file more neat, please help me.
</p>
<p>If it helps you in any way, don't forget to leave 1 star for me ^^</p>

## Demo
<img src="https://github.com/Lou1sVuong/Student-Management-System-Application/assets/110114506/eeeb01ce-257f-439d-8a55-085629bae609" width="33%" alt="image">
<img src="https://github.com/Lou1sVuong/Student-Management-System-Application/assets/110114506/2b87b541-b361-4a9a-afad-8e163a2e3776" width="33%" alt="image">
<img src="https://github.com/Lou1sVuong/Student-Management-System-Application/assets/110114506/f4461d9e-5ee3-471a-86cd-3cc43518d1f7" width="33%" alt="image">

## Program Features
  <ul>
      <li>Register and Login form</li>
      <li>Insert new STD</li>
      <li>Update STD</li>
      <li>Delete STD</li>
      <li>Search STD in table</li>
      <li>Sort STD in table order by ...</li>
  </ul>

## User Manual
<p><b>To run the main.py file in source, we first need to install the PyQt5 library (paste this into terminal): </b></p>


```shell
pip install PyQt5

```

<p><b>If you want to tweak the UI a bit </b></p>
<p>Download and learn how to use QT Designer software :</p>
<p> <a href="https://build-system.fman.io/qt-designer-download">Dowload QT Designer here</a></p>

Then open the UI file in `file UI` with `QT Designer` software, if opening the UI file requires a qrc file, select the corresponding qrc file, after you finish editing, save it as `file-name.ui`
<p></p>

Finally, you need to convert the `.ui` file and `.qrc` file to `.py` by :

<p></p>

`input-file.ui` to `output-file.py` (paste this into terminal):

```shell
pyuic5 input-file.ui -o output-file.py
```

`input-file.qrc` to `output-file.py` (paste this into terminal):

```shell
pyrcc5 input-file.qrc -o output-file.py
```

> **Note**
> Then you replace the converted files with the old files, and remember to import them again!.







