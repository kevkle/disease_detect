# disease_detect
Given a german disease name we will find the ICD for these diseases

Arterienriss: I77.2

Harnblaseninfektion: N30.9

Klaviculafraktur: S42.00

Ovarialzyste: N83.2

Schädelprellung: S00.95

Schenkelhalsfraktur: S72.00

Zungengrundkarzinom: C01


However in german for instance "Zungengrundkarzinom" can also be written as a combination of split up words given by "Karzinom des Zungengrundes".

This web application is set to adress this problem by inputing either the compound noun or the split up words and still giving back the same ICD code for either representation.


To run the code you first clone the repository and then in this folder create a conda environment through the shell with $conda create -n environ python=3.7 flask$.

Finally you activate the conda environment with $conda activate environ$ and then run the app by $python3 app.py$. In the local host you then will see a window where you can enter the diagnosis and by clicking on the button below will receive the corresponding ICD code.
