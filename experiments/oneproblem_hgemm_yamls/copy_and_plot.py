import os
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
base_dir = "/home/ryaswann/Tensile_skoptions/experiments/oneproblem_hgemm_yamls/exploration_results"
files = os.listdir(f"{base_dir}")
print(files)
tempFiles = []
for file in files:
    if ".csv" in file:
        tempFiles.append(file)
files = tempFiles

dfs = []
for infile in (files):
    try:
        #print(f"Loading {infile}")
        out = open("tensile_temp.csv","w")
        input = open(f"{base_dir}/{infile}","r")
        out.write("run,problem-progress,solution-progress,operation,problem-sizes,solution,validation,time-us,gflops,empty,total-gran,tiles-per-cu,num-cus,tile0-gran,tile1-gran,cu-gran,wave-gran,mem-read-bytes,mem-write-bytes,temp-edge,clock-sys,clock-soc,clock-mem,fan-rpm,hardware-samples,gfx-frequency(median),power(median),hotspot-temperature(median),enqueue-time\n")
        #print("hi")
        for line in input:
            #print(line)
            if len(line.split(",")) > 3 and ("Contraction" in line):
                out.write(line)
        #print("Closing")
        out.close()
        df = pd.read_csv("tensile_temp.csv")
        #print(df)
        dfs.append(df)
        #display(df)

    except pd.errors.EmptyDataError:
        print("bleh")

    except UnicodeDecodeError:
        print("heck")

df = pd.concat(dfs).reset_index()
print(df["solution"])
df["Macro_Tile"] = df["solution"].str.split("_",expand=True)[5]
df["Matrix_Instruction"] = df["solution"].str.split("_",expand=True)[6]

df.to_csv("results.csv")
#df = df.loc[df["problem-sizes"] == "(4096,4096,1,4096)"]
#display(df)

thing_to_plot_y="gflops"
thing_to_plot_x = "Macro_Tile"
thing_to_color="Matrix_Instruction"
colors = ["red","blue"]
unique_problem_sizes = df["problem-sizes"].unique()
fig,axs = plt.subplots(len(unique_problem_sizes),1,figsize=(20,100))
problem_size_cnt = 0
for problem_size in tqdm(df["problem-sizes"].unique()):
    #axs[].figure(figsize=(20,5))
    #axs[problem_size_cnt][1].grid()
    temp_df = df.loc[df["problem-sizes"] == problem_size]
    #temp_df = df.loc[df["Matrix_Instruction"] == matrix_instruction]
    sc=axs[problem_size_cnt].scatter(temp_df[thing_to_plot_x],temp_df[thing_to_plot_y])
    axs[problem_size_cnt].set_xticks(temp_df[thing_to_plot_x],temp_df[thing_to_plot_x],rotation=90)

    #plt.title(matrix_instruction)
    if thing_to_color == "gflops":
        plt.colorbar(sc)
    axs[problem_size_cnt].set_title(f"Problem Size {problem_size}")
    #plt.show()
    #plt.clf()
    problem_size_cnt = problem_size_cnt + 1
plt.savefig("out.png")