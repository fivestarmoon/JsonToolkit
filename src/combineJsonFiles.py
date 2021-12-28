import os
import glob
import json

def combineJsonFiles(globFilePattern, outputJsonFilename):
    """
    combineJsonFiles
    combines all files defined by <globFilePattern> into <outputJsonFilename>
    
    Author: Kurt Hagen
    """
     
    print("combineJsonFiles to output JSON file \"" + outputJsonFilename + "\"")
    
    combinedDict = {}
     
    # process each file in the file pattern
    for filename in glob.glob(globFilePattern):
        
        if filename == outputJsonFilename:
            print(filename + ", skipping file with same name as output file (prevent recursive) combine ")
            continue
            
        
        
        fileKey = os.path.basename(filename)
        
        # Load the JSON file
        try:
            with open(filename) as f:
                jsonDict = json.load(f)
        except:
            print(filename + ", ignoring non-JSON file ")
            continue
        
        # Process all attributes
        combinedDict[fileKey] = jsonDict
        
        print(filename + " -> processed")
        
    # for filename
                    
    with open(outputJsonFilename, "w", newline='\n') as f:
            json.dump(combinedDict, f, indent=4,  sort_keys=True)
    
# generateStatistics

