import os
import glob
import json

def updateImageUrlBaseString(globFilePattern, newUrlBaseString, outputDir=None):
    """
    updateImageUrlBaseString
    update "image" URL up to the last "/" to <newUrlBaseString> in files defined by <globFilePattern>.
    the <newUrlBaseString> should not have a trailing "/" (i.e. "https://storage" is expected not "https://storage/") 
    optional  outputDir write all files (changed or unchanged) to this existing directory (relative or absolute)
              otherwise files as per globFilePattern are overwritten  
    
    @author: Kurt Hagen
    """
     
    print("updateImageUrlBaseString \"" + newUrlBaseString + "\"")
     
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
        
        # Update the image URL
        if 'image' not in jsonDict.keys():
            print(filename + " -> ignoring JSON file without 'image' ")
            continue
        url = jsonDict['image']
        indexOfLastSlash = url.rfind('/')
        newUrl = url.replace(url[:indexOfLastSlash], newUrlBaseString)
        jsonDict['image'] = newUrl
                    
        with open(outputFileName, "w", newline='\n') as f:
                json.dump(jsonDict, f, indent=4)        
        
        print(filename + " -> " + outputFileName + " image URL changed")
        
    # for filename
    
# updateImageUrlBaseString

