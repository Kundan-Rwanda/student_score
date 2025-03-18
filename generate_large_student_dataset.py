import pandas as pd
import os
import random
import numpy as np

# Function to generate and write data in chunks
def generate_large_dataset(file_name, num_records, chunk_size=100000):
    columns = ["No", "Regno", "Names", "Assign1/10", "Assign2/10", "Practical/10", "MidTerm Exam/30", "Final Exam/40"]

    # Check if file exists to avoid rewriting the header
    file_exists = os.path.exists(file_name)
    
    with open(file_name, 'a') as f:  # Open in append mode
        if not file_exists:
            # Write header only if the file does not exist
            f.write(",".join(columns) + "\n")
        
        for chunk_start in range(1, num_records + 1, chunk_size):
            chunk_end = min(chunk_start + chunk_size, num_records + 1)
            data = []
            
            for i in range(chunk_start, chunk_end):
                regno = f"240{str(i).zfill(7)}"  # Ensure unique student registration numbers
                name = f"Student{i}"
                
                assign1 = random.choice([9, 8, 7]) if random.random() > 0.1 else ''
                assign2 = random.choice([9, 8, 7]) if random.random() > 0.1 else ''
                practical = random.choice([6, 5, 4]) if random.random() > 0.1 else ''
                midterm_exam = random.randint(10, 30) if random.random() > 0.1 else ''
                final_exam = random.randint(20, 40) if random.random() > 0.1 else ''
                
                data.append([i, regno, name, assign1, assign2, practical, midterm_exam, final_exam])
            
            # Convert to DataFrame and write in chunks to reduce memory usage
            df = pd.DataFrame(data, columns=columns)
            df.to_csv(f, mode='a', header=False, index=False)
            
            print(f"Written {chunk_end - 1} records so far...")
    
    print(f"Dataset '{file_name}' with {num_records} records generated successfully.")

# Set the number of records to generate (~15 million for ~1GB file)
num_records = 30000000  # Adjust as needed
file_name = "large_student_scores.csv"
generate_large_dataset(file_name, num_records)
