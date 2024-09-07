import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
class knowbe4_Phishing_Reader:
    def __init__(self,path_file,file_to_write):
        self.path_file = path_file
        data = None
        self.toWrite = file_to_write
    def load_data(self):
        try:
            data = pd.read_csv(self.path_file)  # Example: Loading Excel data
            print(data)
            print(f"Data loaded successfully from {self.path_file}")
            return data
        except Exception as e:
            print(f"Error loading data from {self.path_file}: {str(e)}")
    #print("Before get_total clicks")
    def get_total_Clicks(self):
        total_not_delivered = 0
        total_delivered = 0
        total_Clicks = 0
        total_Non_Clicks = 0
        azek_Clicks = 0
        azek_Non_Clicks = 0
        u_clicks = 0
        u_Non_Clicks = 0
        rp_clicks = 0
        rp_Non_Clicks = 0
        int_clicks = 0
        int_Non_Clicks = 0
        vers_Clicks = 0
        vers_Non_Clicks = 0
        cont_clicks = 0
        cont_Non_Clicks = 0
        azek_total = 0
        ultralox_total = 0
        rp_total = 0
        int_total = 0
        vers_total = 0
        cont_total = 0
        #print(5)
        #get all the clicks
        #print("Debug")
        print("\n {self.path_file}")
        dat = self.load_data()
        #print("Hey")
        for i, x in dat.iterrows():
            #They all have to be delivered to
            if not (str((x['Delivered At']))=='nan'):
                #All have to not be contractors
                total_delivered+=1
                if not 'Contractors' in str(x['Group']):
                    #Check if the email contrains the word azek in it
                    if 'azek' in x['Email'] or 'Azek' in x['Email'] or 'Cpgint' in x['Email']:
                        azek_total+=1
                        # Check if there is a click
                        #print("SOmethign wrong with cloicked at: "+ str(x['Clicked At']))
                        if not (str(x['Clicked At']) == "nan"):
                            azek_Clicks+=1
                            #print(azek_Clicks)
                            total_Clicks+=1
                        else:
                            azek_Non_Clicks+=1
                            total_Non_Clicks+=1
                    #Check if the emails contains ultralox
                    if 'Ultralox' in x['Email'] or 'ultralox' in x['Email']:
                        ultralox_total+=1
                        # Check if there is a click
                        if not (str(x['Clicked At']) == "nan"):
                            u_clicks+=1
                            total_Clicks+=1
                        else:
                            u_Non_Clicks+=1
                            total_Non_Clicks+=1
                    #get returnpolymers
                    if 'return' in x['Email'] or 'Return' in x['Email']:
                        rp_total+=1
                        if not (str(x['Clicked At']) == "nan"):
                            rp_clicks+=1
                            total_Clicks+=1
                        else:
                            rp_Non_Clicks+=1
                            total_Non_Clicks+=1
                    #Check for the intex millworks
                    if 'intex' in x['Email'] or 'Intex' in x['Email']:
                        int_total+=1
                        if not (str(x['Clicked At']) == "nan"):
                            int_clicks+=1
                            total_Clicks+=1
                        else:
                            int_Non_Clicks+=1
                            total_Non_Clicks+=1
                    #check for verstatex in the email
                    if 'versatex' in x['Email'] or 'Versatex' in x['Email']:
                        vers_total+=1
                        if not (str(x['Clicked At']) == "nan"):
                            vers_Clicks+=1
                            total_Clicks+=1
                        else:
                            vers_Non_Clicks+=1
                            total_Non_Clicks+=1
                #Check for contractors
                else:
                    cont_total+=1
                    if not (str(x['Clicked At']) == "nan"):
                        cont_clicks+=1
                        total_Clicks+=1   
                    else:
                        cont_Non_Clicks+=1
                        total_Non_Clicks+=1
            else:
                total_not_delivered +=1
        #write to file that you want to write
        # f = open(file_to_write,'w')
        # f.write("Phishing Statistics for the Campaign\n")
        # f.write("Total number of users who got the email: " + str(total_delivered) + "\n")
        # f.write("Total number of users who clicked the email: " + str(total_Clicks) + "\n")
        # f.write("Total number of users who didnt click the email: " + str(total_Non_Clicks) + "\n")
        # f.write("Total number of azek users who clicked the email: " + str(azek_Clicks) + "\n")
        # f.write("Total number of azek users who didnt click the email: " + str(azek_Non_Clicks) + "\n")
        # f.write("Total number of azek users who got the email: " + str(azek_total) + "\n")
        # f.write("Total number of ultralox users who clicked the email: " + str(u_clicks) + "\n")
        # f.write("Total number of ultralox users who didnt click the email: " + str(u_Non_Clicks) + "\n")
        # f.write("Total number of ultralox users who got the email: " + str(ultralox_total) + "\n")
        # f.write("Total number of return polymere users who clicked the email: " + str(rp_clicks) + "\n")
        # f.write("Total number of return polymere users who didnt click the email: " + str(rp_Non_Clicks) + "\n")
        # f.write("Total number of users who got the email: " + str(rp_total) + "\n")
        # f.write("Total number of intex millworks users who clicked the email: " + str(int_clicks) + "\n")
        # f.write("Total number of intex millworks users who didnt click the email: " + str(int_Non_Clicks) + "\n")
        # f.write("Total number of intex millworks users who got the email: " + str(int_total) + "\n")
        # f.write("Total number of versatex users who clicked the email: " + str(vers_Clicks) + "\n")
        # f.write("Total number of versatex users who didnt click the email: " + str(vers_Non_Clicks) + "\n")
        # f.write("Total number of versatex users who got the email: " + str(vers_total) + "\n")
        # f.write("Total number of contractors who clicked the email: " + str(cont_clicks) + "\n")
        # f.write("Total number of contractors who didnt click the email: " + str(cont_Non_Clicks) + "\n")
        # f.write("Total number of contractors who got the email: " + str(cont_total) + "\n")
        # f.close()
        #Graph 1 delivery rate
        labels = ['Delivered', 'Not Delivered']
        sizes = [total_delivered, total_not_delivered]
        explode = (0.1, 0)  # explode the 1st slice
        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.set_title('Delivered Rate',fontsize=18, fontweight='bold')
        plt.savefig('Delivery_Rate.png') 
        plt.close()
        #GRaph 2 Click rate
        labels = ['Clicked', 'No Click']
        sizes = [total_Clicks, total_Non_Clicks]
        explode = (0.1, 0)  # explode the 1st slice
        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.set_title('Click Rate Amongst Employees',fontsize=18, fontweight='bold')
        plt.savefig('click_rate.png') 
        plt.close()

        #Graph 3
        categories = ['Azek', 'Ultralox', 'Return Poly', 'Intex', 'Versatex', 'Contractors']
        clicked = [azek_Clicks, u_clicks, rp_clicks, int_clicks, vers_Clicks, cont_clicks]
        not_clicked = [azek_Non_Clicks, u_Non_Clicks, rp_Non_Clicks, int_Non_Clicks, vers_Non_Clicks, cont_Non_Clicks]
        ind = list(range(len(categories)))  # the x locations for the groups
        width = 0.50  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar([float(i) - width/2 for i in ind], clicked, width, label='Clicked')
        rects2 = ax.bar([float(i)+ width/2 for i in ind], not_clicked, width, label='Did Not Click')
        total = [clicked[i] + not_clicked[i] for i in range(len(categories))]
        ax.set_ylabel('Number of Employees')
        ax.set_title('Click Rate By Domain',fontsize=18, fontweight='bold')
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
        plt.savefig('click_rate_by_domain.png')
        plt.close()
if __name__ == '__main__':
   count = len(sys.argv)
   if count!=3:
       print("Usage: Must give program, fike, file to write")
   phish_file = sys.argv[1]
   output_file = sys.argv[2]
   know4_Phisher = knowbe4_Phishing_Reader(phish_file,output_file)
   know4_Phisher.get_total_Clicks()