import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import csv             
class KnowBe4_training_reader:
    def __init__(self,path_file,file_to_write):
        self.path_file = path_file
        data = None
        self.toWrite = file_to_write
    def load_data(self):
        try:
            data = pd.read_csv(self.path_file)  # Example: Loading Excel data
            #print("Eureka")
            print(self.path_file)
            print(f"Data loaded successfully from {self.path_file}")
            return data
        except Exception as e:
            #print("Eureka Error")
            print(f"Error loading data from {self.path_file}: {str(e)}")
    total_employee_comp = 0
    contractor_comp = 0
    #print(5)
    def get_total_completion(self):
        #Create the metrics for the training
        #print("Hello after get total completon has started")
        total_training = 0
        total_Non_training = 0
        azek_training = 0
        azek_Non_training = 0
        u_training = 0
        u_Non_training = 0
        rp_training = 0
        rp_Non_training = 0
        int_training = 0
        int_Non_training = 0
        vers_training = 0
        vers_Non_training = 0
        cont_training = 0
        cont_Non_training = 0
        azek_total = 0
        ultralox_total = 0
        rp_total = 0
        int_total = 0
        vers_total = 0
        cont_total = 0
        #load the data
        dat = self.load_data()
        #print(dat)
        #iterate through the rows 
        for i, x in dat.iterrows():
            if not 'Contractor' in str(x['Group']):
                #print(str(x['First Name']),str(x['Last Name']),"EMPLOYEE")
                if 'azek' in x['Email'] or 'Azek' in x['Email'] or 'cpgint' in x['Email']:
                    azek_total+=1
                    if '100%' == str(x['Score']):
                        azek_training+=1
                        total_training+=1
                    else:
                        azek_Non_training+=1
                        total_Non_training+=1
                if 'Ultralox' in x['Email'] or 'ultralox' in x['Email']:
                    #print(str(x['First Name']),str(x['Last Name']),"Ultralox")
                    ultralox_total+=1
                    if '100%' == str(x['Score']):
                        u_training+=1
                        total_training+=1
                    else:
                        u_Non_training+=1
                        total_Non_training+=1
                if 'return' in x['Email'] or 'Return' in x['Email']:
                    rp_total+=1
                    if '100%' == str(x['Score']):
                        rp_training+=1
                        total_training+=1
                    else:
                        rp_Non_training +=1
                        total_Non_training+=1
                if 'intex' in x['Email'] or 'Intex' in x['Email']:
                    int_total+=1
                    if '100%' == str(x['Score']):
                        int_training+=1
                        total_training+=1
                    else:
                        int_Non_training+=1
                        total_Non_training+=1
                if 'versatex' in x['Email'] or 'Versatex' in x['Email']:
                    vers_total+=1
                    if '100%' == str(x['Score']):
                        vers_training+=1
                        total_training+=1
                    else:
                        vers_Non_training+=1
                        total_Non_training+=1
            else:
                #print(str(x['First Name']),str(x['Last Name']),"CONTRACTOR")
                cont_total+=1
                if '100%' == str(x['Score']):
                    #print(str(x['First Name']),str(x['Last Name']),"Finished")
                    cont_training+=1
                else:
                    #print(str(x['First Name']),str(x['Last Name']),"DiDnt FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFinish")
                    cont_Non_training+=1

        # f = open(self.toWrite,'w')
        # f.write("\n\nTraining Completion Statistics for the Campaign\n")
        # f.write("Total number of employees who completed training: " + str(total_training) + "\n")
        # f.write("Total number of employees who did not complete training: " + str(total_Non_training) + "\n")
        # f.write("Total number of azek employees who completed training: " + str(azek_training) + "\n")
        # f.write("Total number of azek employees who did not complete training: " + str(azek_Non_training) + "\n")
        # f.write("Total number of azek employees who participated in training: " + str(azek_total) + "\n")
        # f.write("Total number of ultralox employees who completed training: " + str(u_training) + "\n")
        # f.write("Total number of ultralox employees who did not complete training: " + str(u_Non_training) + "\n")
        # f.write("Total number of ultralox employees who participated in training: " + str(ultralox_total) + "\n")
        # f.write("Total number of return polymere employees who completed training: " + str(rp_training) + "\n")
        # f.write("Total number of return polymere employees who did not complete training: " + str(rp_Non_training) + "\n")
        # f.write("Total number of return polymere employees who participated in training: " + str(rp_total) + "\n")
        # f.write("Total number of intex millworks employees who completed training: " + str(int_training) + "\n")
        # f.write("Total number of intex millworks employees who did not complete training: " + str(int_Non_training) + "\n")
        # f.write("Total number of intex millworks employees who participated in training: " + str(int_total) + "\n")
        # f.write("Total number of versatex employees who completed training: " + str(vers_training) + "\n")
        # f.write("Total number of versatex employees who did not complete training: " + str(vers_Non_training) + "\n")
        # f.write("Total number of versatex employees who participated in training: " + str(vers_total) + "\n")
        # f.write("Total number of contractors who completed training: " + str(cont_training) + "\n")
        # f.write("Total number of contractors who did not complete training: " + str(cont_Non_training) + "\n")
        # f.write("Total number of contractors who participated in training: " + str(cont_total) + "\n")
        # f.close()
        labels = ['Completed Training', 'Did Not Complete Training']
        sizes = [total_training, total_Non_training]
        explode = (0.1, 0)  # explode the 1st slice
        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.set_title('Training Completion Status')
        plt.savefig('training_completion.png') 
        plt.close()
        labels = ['Completed Training', 'Did Not Complete Training']
        sizes = [cont_training, cont_Non_training]
        explode = (0.1, 0)  # explode the 1st slice
        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.set_title('Training Completion Status')
        plt.savefig('training_completion_contractors.png') 
        plt.close()
        categories = ['Azek', 'Ultralox', 'Return Poly', 'Intex', 'Versatex', 'Contractors']
        completed = [azek_training, u_training, rp_training, int_training, vers_training, cont_training]
        not_completed = [azek_Non_training, u_Non_training, rp_Non_training, int_Non_training, vers_Non_training, cont_Non_training]
        ind = list(range(len(categories)))  # the x locations for the groups
        width = 0.50  # the width of the bars
        

        fig, ax = plt.subplots()
        rects1 = ax.bar([float(i) - width/2 for i in ind], completed, width, label='Completed Training')
        rects2 = ax.bar([float(i)+ width/2 for i in ind], not_completed, width, label='Did Not Complete Training')
        total = [completed[i] + not_completed[i] for i in range(len(categories))]
        ax.set_ylabel('Number of Employees')
        ax.set_title('Training Completion by Category')
        ax.set_xticks(ind)
        ax.set_xticklabels(categories)
        ax.legend()
        def autolabel(rects, total):
            for rect, tot in zip(rects, total):
                height = rect.get_height()
                percentage = height / tot * 100
                ax.annotate(f'{percentage:.1f}%',
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')
        autolabel(rects1, total)
        autolabel(rects2, total)
        plt.tight_layout()
        plt.savefig('training_completed_output.png')
        plt.close()

#What I can do is take the system arguments and if there is phishing or trainin
#we can do that by the count, if count is just program.py and filename and file to write, so 3, do both
#if the count is 4, then see what the fourth argument is and only do that one
# use sys arg
if __name__ == '__main__':
   count = len(sys.argv)
   if count!=3:
       print("Usage: Must give program, fike, file to write")
   train_file = sys.argv[1]
   output_file = sys.argv[2]
   know4_Training = KnowBe4_training_reader(train_file,output_file)
   know4_Training.get_total_completion()