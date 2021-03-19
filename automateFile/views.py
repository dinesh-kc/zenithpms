from django.shortcuts import render
from .resources import MedicineResouce
from tablib import Dataset
from manage_medicines.models import Medicine

# Create your views here.
def automateFile(request):
    def simple_upload(request):
        if request.method == 'POST':
            medicine_resource = MedicineResouce()
            dataset = Dataset()
            new_medicines = request.FILES['myfile']

            imported_data = dataset.load(new_medicines.read(),format='xlsx')
        #print(imported_data)
            for data in imported_data:
                print(data[1])
                medicines = Medicine(data[0], data[1], data[2], data[3], data[4])
                medicines.save()
                print(medicines)        	     


        	
        
    
    return render(request, 'automateFile.html')