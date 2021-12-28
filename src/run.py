from updateTraitValue import updateTraitValue
from updateDescription import updateDescription
from generateStatistics import generateStatistics
from combineJsonFiles import combineJsonFiles

if True:
    updateTraitValue(globFilePattern="*.json", trait="Whiskers", fromValue="3-long", toValue="3-Long-diff", fromValueCaseSensitive=False, outputDir="updated")
    updateTraitValue(globFilePattern="*.json", trait="Whiskers", fromValue="3-long", toValue="3-Long-diff", fromValueCaseSensitive=False)
    updateTraitValue(globFilePattern="*.json", trait="Whiskers", fromValue="3-Long-diff", toValue="3-Long")

if True:
    updateDescription(globFilePattern="*.json", newDescription="New Description", outputDir="updated")

if True:
    generateStatistics(globFilePattern="*.json", outputJsonFilename="stats.json")
    
if True:
    combineJsonFiles(globFilePattern="*.json", outputJsonFilename="combine.json")