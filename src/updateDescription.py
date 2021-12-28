import os
import glob
import json

def updateDescription(globFilePattern, newDescription, outputDir=None):
    """
    updateDescription
    update "description" to <newDescription> in files defined by <globFilePattern>
    optional  outputDir write all files (changed or unchanged) to this existing directory (relative or absolute)
              otherwise files as per globFilePattern are overwritten  
    
    Author: Kurt Hagen
    """
     
    print("UpdateDescription \"" + newDescription + "\"")
     
    # process each file in the file pattern
    for filename in glob.glob(globFilePattern):
                
        outputFileName = filename
        if outputDir is not None:
            basename = os.path.basename(filename)
            outputFileName = os.path.join(outputDir, basename)
        
        # Load the JSON file
        try:
            with open(filename) as f:
                jsonDict = json.load(f)
        except:
            print(filename + " -> ignoring non-JSON file ")
            continue
        
        # Update the Description
        if 'description' not in jsonDict.keys():
            print(filename + " -> ignoring JSON file without 'description' ")
            continue
        jsonDict['description'] = newDescription
                    
        with open(outputFileName, "w", newline='\n') as f:
                json.dump(jsonDict, f, indent=4)        
        
        print(filename + " -> " + outputFileName + " description changed")
        
    # for filename
    
# updateDescription

