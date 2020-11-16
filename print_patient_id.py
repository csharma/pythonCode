
import os
from pathlib import Path

from pydicom import dcmread
from pydicom.data import get_testdata_file
from pydicom.filereader import read_dicomdir

# fetch the path to the test data                                               
#path = get_testdata_file('DICOMDIR')
path = "/Users/cartik_sharma/Downloads/dicom_files/"


#ds = dcmread(path)
#root_dir = Path(ds.filename).resolve().parent
#print("Root directory: {root_dir}\n")
xyz = "/Users/cartik_sharma/Downloads/dicom_files/"
zList = []
xList = []
yList = []

V = 0
def area(xList, yList, zList):
   n = len(xList)
   a = 0.0
   for i in range(n-1):
      j = (i+1)%n
      a+= abs(xList[i]*yList[j]-yList[i]*xList[j])
   result = abs(a)/2.0
   return result

AList = []

for count, filename in enumerate(os.listdir("/Users/cartik_sharma/Downloads/dicom_files/")) :

   ds = dcmread(xyz+filename,force=True)
   if hasattr(ds, 'PatientID'):
      print("Patient ID.......: "+ds.PatientID)
      if hasattr(ds,'ROIContourSequence'):
         ctrs = ds.ROIContourSequence

         length = len(ctrs)
         i = 0

         while i < length:
            n = ctrs[i].ContourSequence[i].NumberOfContourPoints
#            print(" number of contour points"+str(n))

            zz=ctrs[i].ContourSequence[i].ContourData

            lim = len(zz)-3
            ii = 0
            while ii<lim:
               x = zz[ii]
               y = zz[ii+1]
               z = zz[ii+2]
               
               ii = ii+3
               
               xList.append(x)
               yList.append(y)
               zList.append(z)
               
            A = area(xList,yList,zList)
            AList.append(A)
            AList.append(z)
            i=i+1
            
i = 0

lim = len(AList)-3
i = 0
while i < lim:
   meanA = (AList[i]+AList[i+2])/2
   height = abs(AList[i+1]-AList[i+3])
   i = i+2

   V+= meanA*height
   i=i+2


print("Volume of contours "+str(V))      
print(" number of dicom files "+str(count))
   
   
