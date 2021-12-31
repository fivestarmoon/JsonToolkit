import glob
import json

def generateStatistics(globFilePattern, outputJsonFilename):
    """
    generateStatistics
    generate the trait type and value counts from files defined by <globFilePattern>
    
    @author: Kurt Hagen
    """
     
    print("generateStatistics to output JSON file \"" + outputJsonFilename + "\"")
    
    statsDict = {}
     
    # process each file in the file pattern
    for filename in glob.glob(globFilePattern):
        
        # Load the JSON file
        try:
            with open(filename) as f:
                jsonDict = json.load(f)
        except:
            print(filename + ", ignoring non-JSON file ")
            continue
        
        # Process all attributes
        if 'attributes' not in jsonDict.keys():
            print(filename + ", ignoring JSON file without 'attributes' ")
            continue
        attributesList = jsonDict['attributes']        
        for attribute in attributesList:
            
            # get the trait type and value
            if 'trait_type' not in attribute.keys():
                continue       
            traitType =  attribute['trait_type']
            if 'value' not in attribute.keys():
                continue       
            traitValue =  attribute['value']
            
            if traitType not in statsDict.keys():
                statsDict[traitType] = {}
            traitDict = statsDict[traitType]
            
            if traitValue not in traitDict.keys():
                traitDict[traitValue] = 0
                
            traitDict[traitValue] = traitDict[traitValue] + 1
        
        print(filename + " -> processed")
        
    # for filename
                    
    with open(outputJsonFilename, "w", newline='\n') as f:
            json.dump(statsDict, f, indent=4,  sort_keys=True)
    
# generateStatistics

