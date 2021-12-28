import os
import glob
import json

def updateTraitValue(globFilePattern, trait, fromValue, toValue, fromValueCaseSensitive=True, outputDir=None):
    """
    updateTraitValue
     update trait_type <trait> <fromValue> -> <toValue> in files defined by <globFilePattern>
     optional  fromValueCaseSensitive is True or False
     optional  outputDir write all files (changed or unchanged) to this existing directory (relative or absolute)
               otherwise files as per globFilePattern are overwritten    
    
    Author: Kurt Hagen
    """
     
    print("updateTraitValue \"" + trait + "\""
              + " from value \"" + fromValue 
              + "\" (case_sensitve=" + str(fromValueCaseSensitive) + ")"
              + " to value \"" + toValue + "\""
              + " outputDir is \"" + str(outputDir) + "\"")
     
    # process each file in the file pattern
    for filename in glob.glob(globFilePattern):
        
        fileChanged = False
        
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
        
        # Process all attributes
        if 'attributes' not in jsonDict.keys():
            print(filename + " -> ignoring JSON file without 'attributes' ")
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
            
            # change the appropriate traits only
            if not(traitType == trait):
                continue
            
            # change appropriate trait with matching case sensitive value
            if fromValueCaseSensitive and (traitValue == fromValue):
                attribute['value'] = toValue;
                print(filename + " -> " + outputFileName + ", changed trait [" + trait + "] from value [" + traitValue + "] to [" + toValue + "]")
                fileChanged = True
                continue
            
            # change appropriate trait with matching case insensitive value
            if not(fromValueCaseSensitive) and (traitValue.casefold() == fromValue.casefold()):
                attribute['value'] = toValue;
                print(filename + " -> " + outputFileName + ", changed trait [" + trait + "] from value [" + traitValue + "] to [" + toValue + "]")
                fileChanged = True
                continue
        
        if not(fileChanged):
            print(filename + " -> " + outputFileName + ", no change")
                    
        with open(outputFileName, "w", newline='\n') as f:
                json.dump(jsonDict, f, indent=4)
        
    # for filename
    
# updateTraitValue

