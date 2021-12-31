from updateTraitValue import updateTraitValue
from updateDescription import updateDescription
from generateStatistics import generateStatistics
from combineJsonFiles import combineJsonFiles
from updateImageUrlBaseString import updateImageUrlBaseString

updateTraitValue(globFilePattern="*.json", trait="Whiskers", fromValue="3-long", toValue="3-Long-diff", fromValueCaseSensitive=False, outputDir="updated")
updateTraitValue(globFilePattern="*.json", trait="Whiskers", fromValue="3-long", toValue="3-Long-diff", fromValueCaseSensitive=False)
updateTraitValue(globFilePattern="*.json", trait="Whiskers", fromValue="3-Long-diff", toValue="3-Long")

updateDescription(globFilePattern="*.json", newDescription="New Description", outputDir="updated")

updateImageUrlBaseString(globFilePattern="*.json", newUrlBaseString="https://storage", outputDir="updated")

generateStatistics(globFilePattern="*.json", outputJsonFilename="stats.json")

combineJsonFiles(globFilePattern="*.json", outputJsonFilename="combine.json")