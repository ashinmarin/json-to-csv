# json-to-csv
Python script to convert a specific format of question-answer pairsjson file in csv format. Extracts only question-answer pairs from the file.

##### Sample Usage:

 * ``python3 json_to_csv.py --infile <parsed-json-file>``

The format of json file should be in the format of:
```
{
    "oral_deposition": {   
        "parsed_examinations": [        
            {
            
                "examiner": "MR. BIGGER",
                
                "examination": [
                
                    {
                    
                        "question": "Miss Bonhomme, good morning.",
                        
                        "answer": "Good morning, Mr. Bigger."
                        
                    },
                    
                    {
                    
                        "question": "It's nice to see you again.",
                        
                        "answer": "Same. Same here."
                        
                    },
                    
                    {
                    
                        "speaker": "MR. GERAGHTY",
                        
                        "spoke": "I'm going to object to the form of that question as it's phrased."
                        
                    }
                    
                   ]
                   
                  }
                  
                 ]
                 
                }
                
               }
               ```
