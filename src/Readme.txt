common input parameters
	globFilePattern			selected file set to process (i.e., "*.json")
   	fromValueCaseSensitive 	(optional) by default True
   	outputDir 				(optional) write all files (changed or unchanged) to this existing directory (relative or absolute)
   		                 		otherwise files are overwritten 

updateTraitValue.py
   	updateTraitValue(globFilePattern, trait, fromValue, toValue, fromValueCaseSensitive=True, outputDir=None)  
   	where
   		trait 		"trait_type" to update
   		fromValue 	"value" to update (use fromValueCaseSensitive to control string comparison case sensitive)
   		toValue		new "value" to use
   	example
   		updateTraitValue(globFilePattern="*.json", trait="Whiskers", fromValue="3-long", toValue="3-Long-diff", fromValueCaseSensitive=False)

updateDescription.py
   	updateDescription(globFilePattern, newDescription, outputDir=None)
   		newDescription	update all "description" with this new text
   	example
   		updateDescription(globFilePattern="*.json", newDescription="New Description", outputDir="updated")

generateStatistics.py
    generateStatistics(globFilePattern, outputJsonFilename)
    	outputJsonFilename	update the JSON formatted statistics to this file (relative or absolute)
    example
    	generateStatistics(globFilePattern="*.json", outputJsonFilename="stats.json")
    	
combineJsonFiles.py
    combineJsonFiles(globFilePattern, outputJsonFilename)
    	combines all files defined by <globFilePattern> into <outputJsonFilename> (relative or absolute)
    example
    	combineJsonFiles(globFilePattern="*.json", outputJsonFilename="combine.json")
    	