import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from google.cloud import bigquery
import os, json, sys
from time import time
import pandas as pd


class SliderGraph:

    def __init__(self, master):
        self.master = master
        # with open(self.resource_path(config_file)) as fp:
        #     self.config = json.load(fp)
        # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.resource_path(creds_file)
        # self.projectID = self.config['projectID']
        # self.datasetID = self.config['datasetID']
        # last_used_freq = self.config['last_used_frequency']
        # last_used_delta = self.config['last_used_delta']

        self.bounds = 1
        self.frame = tk.Frame(master)
        self.fig = Figure()
        row = 0

        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlabel("Run Numbers")
        self.ax.set_ylabel("UDD")
        self.ax.set_ylim([-self.bounds,self.bounds])

        self.canvas = FigureCanvasTkAgg(self.fig, master=master)  # , width=win_width, height=(win_height-50))
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=row, columnspan=2, sticky='nsew')
        row+=1

        self.table_label = tk.Label(master, text="Enter BigQuery Table Name")
        self.table_label.grid(row=row, column=0)
        # row += 1

        self.table_name = tk.Entry(master)
        # self.table_name.insert(0,self.config['last_used_table'])
        self.table_name.grid(row=row, column=1, sticky='ew')
        row += 1

        self.get_table_button = tk.Button(master, text="Get Table Data and Plot", command=self.plot_data)
        self.get_table_button.grid(row=row, columnspan=2)
        row += 1

        self.frequency_slider = tk.Scale(master, from_=400, to=4500, orient=tk.HORIZONTAL, command=self.update_plot)
        # self.frequency_slider.set(last_used_freq)
        self.frequency_slider.grid(row=row,columnspan=2, sticky="nsew")
        row += 1

        self.frequency_entry = tk.Entry(master)
        # self.frequency_entry.insert(0,last_used_freq)
        self.frequency_entry.grid(row=row, columnspan=2)
        row += 1

        self.delta_slider = tk.Scale(master, from_=-500, to=500, orient=tk.HORIZONTAL, command=self.update_plot)
        # self.delta_slider.set(last_used_delta)
        self.delta_slider.grid(row=row, columnspan=2, sticky="ensw")
        row += 1

        self.delta_entry = tk.Entry(master)
        # self.delta_entry.insert(0, last_used_delta)
        self.delta_entry.grid(row=row, columnspan=2)
        row += 1

        self.get_table_button = tk.Button(master, text="Autoscale", command=self.autoscale)
        self.get_table_button.grid(row=row,columnspan=2)
        row += 1

        tk.Grid.columnconfigure(master, 0, weight=1)
        tk.Grid.columnconfigure(master, 1, weight=1)
        tk.Grid.rowconfigure(master, 0, weight=5)
        for x in range(1,row):
            tk.Grid.rowconfigure(master, x, weight=0)

        master.protocol('WM_DELETE_WINDOW', self.close)

        self.df = None
        self.frequency_list = []
        self.series = None
        self.elapsed = time()*1000

    def plot_data(self):
        self.ax.clear()
        self.client = bigquery.Client(project=self.projectID)
        self.tableID = f"`{self.datasetID}.{self.table_name.get()}`"

        QUERY = (
            f"SELECT * EXCEPT (testCount,elapsed_run_time_ms_,moleculeValue,onboardTemp1,onboardTemp2,temp,tempControl,\
             logamp, txrx,timestamp) FROM {self.tableID} ORDER BY runCount ASC;"
        )
        # query_job = self.client.query(QUERY)
        # rows = query_job.result()
        self.df = pd.read_gbq(QUERY,self.projectID)

        for col in self.df.columns:
            if 'runCount' in col:
                continue
            self.frequency_list.append(int(col.replace('_','')))
        self.frequency_slider.configure(from_=min(self.frequency_list),to=max(self.frequency_list))
        self.delta_slider.configure(from_=-max(self.frequency_list),to=max(self.frequency_list))

        freq = f'_{self.frequency_slider.get()}'
        freq2 = f'_{self.frequency_slider.get() + self.delta_slider.get()}'
        self.series = self.df[freq] - self.df[freq2]
        self.series.plot(ax=self.ax)
        self.ax.set_ylim([-self.bounds,self.bounds])

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        pass

    def update_plot(self, newslider):
        try:

            self.ax.clear()
            freq = f'_{self.frequency_slider.get()}'
            freq2 = f'_{self.frequency_slider.get() + self.delta_slider.get()}'
            self.series = self.df[freq] - self.df[freq2]
            self.series.plot(ax=self.ax)
            zero = self.series.mean()
            self.ax.set_ylim([zero-self.bounds, zero+self.bounds])
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()
            # self.master.update_idletasks()

            if ((time()*1000)-self.elapsed > 100):
                self.elapsed = time()*1000
                self.frequency_entry.delete(0,'end')
                self.frequency_entry.insert(0,freq.replace('_',''))
                self.delta_entry.delete(0,'end')
                self.delta_entry.insert(0,self.delta_slider.get())
        except:
            pass

    def play_runs(self):
        pass

    def autoscale(self):
        self.ax.clear()
        self.series.plot(ax=self.ax)
        self.ax.relim()
        self.ax.autoscale()
        zero = self.series.mean()
        self.bounds = self.series.max() - self.series.min()
        self.ax.set_ylim([zero-self.bounds,zero+self.bounds])
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def close(self):

        self.master.destroy()

if __name__=="__main__":
    root = tk.Tk()
    slider_fig = SliderGraph(root)
    root.mainloop()