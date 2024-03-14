import random
 
 
# Constants for simulation
 
 
OFF_TARGET_THRESHOLD = float(input("Input Required Threshold For Binding Accuracy: "))
 
 
def generate_genome(size):
    g = ""
    x = "ATGC"
 
    for i in range(size):
        g = g+(random.choice(x))
 
    return g
 
def generate_gRNA(target):
    res = ""
 
    for i in range(len(target)):
        ch = ""
        if(target[i] == "A"):
            ch = "T"
        if(target[i] == "T"):
            ch = "A"
        if(target[i] == "G"):
            ch = "C"
        if(target[i] == "C"):
            ch = "G"
 
        res = res + ch
 
    return res

 
 
def calculate_binding_score(gRNA, target):
 
    # Simulate binding score calculation based on sequence similarity
 
    
    count = 0
 
    for i in range(len(gRNA)):
        if(gRNA[i] == "A" and target[i] == "T"):
            count = count+1
 
        if(gRNA[i] == "T" and target[i] == "A"):
            count = count+1
 
        if(gRNA[i] == "G" and target[i] == "C"):
            count = count+1
 
        if(gRNA[i] == "C" and target[i] == "G"):
            count = count+1
 
    res = count/len(gRNA)
    return res

 
 
# Function to predict off-target effects (simplified)
simi_arr = []
 
def predict_off_target(target , genome):
 
    off_target = []
 
    for i in range(len(genome) - len(gRNA) + 1):
 
        subsequence = genome[i:i + len(gRNA)]
 
        similarity = calculate_binding_score(gRNA, subsequence)
 
        if similarity >= OFF_TARGET_THRESHOLD:
            simi_arr.append(similarity)
            off_target.append(i)
 
    return off_target
 
 
# Function to simulate CRISPR-Cas9 editing
 
def simulate_crispr_cas9(gRNA, genome):
 
    # print()
    # print()
    # print(type(gRNA))
    # print(type(genome))
    binding_score = calculate_binding_score(gRNA, TARGET)
 
    target_sites = predict_off_target(gRNA, genome)
 
    
 
 
    if binding_score >= OFF_TARGET_THRESHOLD:
 
        if len(target_sites)==1:
 
            edit_position = target_sites[0]
 
            #edited_genome = genome[:edit_position] +"  {"+ gRNA +"}  " + genome[edit_position + len(gRNA):]
 
            return f"Successful binding at position {edit_position}"   #:\n{edited_genome}"
 
        else:
 
            ps = f"Editing failed due to off-target effects at positions {target_sites} \n"
 
            for i in range(len(target_sites)):
                ps = ps + "\n" + genome[target_sites[i]:target_sites[i]+len(gRNA)]+" Similarity = "+ str(simi_arr[i])
            # for i in range(len(target_sites)):
            #     genome = genome[:target_sites[i]] + "  {" + genome[target_sites[i]:target_sites[i]+len(gRNA)] + "}  " + genome[target_sites[i]+len(gRNA):]
 
            return (ps)

 
    else:
 
        return "Editing failed due to weak gRNA-DNA binding"
 
 
# Main simulation
 
# GENOME = input("Input GENOME sequence: ")
 
size = int(input("Input size to generate genome:"))
 
g = generate_genome(size)
 
print(g)
 
TARGET = input("Input TARGET sequence: ")
 
pstr = input(" Do you require a gRNA:")
 
gRNA = input("Input gRNA sequence: ")
 
#gRNA = generate_gRNA(TARGET)
 
#print("gRNA generated:"+gRNA)
 
print(calculate_binding_score(gRNA,TARGET))
 
result = simulate_crispr_cas9(gRNA, g)
 
print(result)
 