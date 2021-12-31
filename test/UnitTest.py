'''
Created on Dec. 31, 2021

@author: Kurt Hagen
'''
import os
import unittest
import json
import pathlib
import tempfile

from updateTraitValue import updateTraitValue
from updateDescription import updateDescription
from generateStatistics import generateStatistics
from combineJsonFiles import combineJsonFiles
from updateImageUrlBaseString import updateImageUrlBaseString


class Test(unittest.TestCase):

    def testUpdateTraitValue(self):
        # Validate starting point
        self.assertTrue(isJsonTraitCorrect("0.json", "Personality", "Friendly"))
        self.assertTrue(isJsonTraitCorrect("0.json", "Backgrounds", "Gradient-3"))
        self.assertTrue(isJsonTraitCorrect("0.json", "Earings", "Earing-none"))
        self.assertTrue(isJsonTraitCorrect("1.json", "Personality", "Shy"))
        self.assertTrue(isJsonTraitCorrect("1.json", "Backgrounds", "Psyc-1"))
        self.assertTrue(isJsonTraitCorrect("1.json", "Earings", "Earing-none"))
        self.assertTrue(isJsonTraitCorrect("2.json", "Personality", "Curious"))
        self.assertTrue(isJsonTraitCorrect("2.json", "Backgrounds", "Purple"))
        self.assertTrue(isJsonTraitCorrect("2.json", "Earings", "Earing-none"))
        
        # Validate updates
        updateTraitValue(globFilePattern="*.json", trait="Personality", fromValue="friendly", toValue="TestValue1", fromValueCaseSensitive=False)        
        updateTraitValue(globFilePattern="*.json", trait="Personality", fromValue="shy", toValue="TestValue2", fromValueCaseSensitive=True)       
        updateTraitValue(globFilePattern="*.json", trait="Earings", fromValue="Earing-none", toValue="TestValue3", fromValueCaseSensitive=True)
        
        # Validate modification
        self.assertTrue(isJsonTraitCorrect("0.json", "Personality", "TestValue1"))
        self.assertTrue(isJsonTraitCorrect("0.json", "Backgrounds", "Gradient-3"))
        self.assertTrue(isJsonTraitCorrect("0.json", "Earings", "TestValue3"))
        self.assertTrue(isJsonTraitCorrect("1.json", "Personality", "Shy"))
        self.assertTrue(isJsonTraitCorrect("1.json", "Backgrounds", "Psyc-1"))
        self.assertTrue(isJsonTraitCorrect("1.json", "Earings", "TestValue3"))
        self.assertTrue(isJsonTraitCorrect("2.json", "Personality", "Curious"))
        self.assertTrue(isJsonTraitCorrect("2.json", "Backgrounds", "Purple"))
        self.assertTrue(isJsonTraitCorrect("2.json", "Earings", "TestValue3"))
        
        # Restore the updates
        updateTraitValue(globFilePattern="*.json", trait="Personality", fromValue="TestValue1", toValue="Friendly", fromValueCaseSensitive=True) 
        updateTraitValue(globFilePattern="*.json", trait="Earings", fromValue="TestValue3", toValue="Earing-none", fromValueCaseSensitive=True)
        
        # Validate ending point
        self.assertTrue(isJsonTraitCorrect("0.json", "Personality", "Friendly"))
        self.assertTrue(isJsonTraitCorrect("0.json", "Backgrounds", "Gradient-3"))
        self.assertTrue(isJsonTraitCorrect("0.json", "Earings", "Earing-none"))
        self.assertTrue(isJsonTraitCorrect("1.json", "Personality", "Shy"))
        self.assertTrue(isJsonTraitCorrect("1.json", "Backgrounds", "Psyc-1"))
        self.assertTrue(isJsonTraitCorrect("1.json", "Earings", "Earing-none"))
        self.assertTrue(isJsonTraitCorrect("2.json", "Personality", "Curious"))
        self.assertTrue(isJsonTraitCorrect("2.json", "Backgrounds", "Purple"))
        self.assertTrue(isJsonTraitCorrect("2.json", "Earings", "Earing-none"))
        
        # Test absolute path and output directory
        with tempfile.TemporaryDirectory() as tempOutputDir:
            absPath = pathlib.Path().resolve()
            globPattern = os.path.join(absPath, "0.json")
            updateTraitValue(globFilePattern=globPattern, trait="Backgrounds", fromValue="Gradient-3", toValue="TestValue1", outputDir=tempOutputDir)
            self.assertTrue(isJsonTraitCorrect(os.path.join(tempOutputDir,"0.json"), "Personality", "Friendly"))
            self.assertTrue(isJsonTraitCorrect(os.path.join(tempOutputDir,"0.json"), "Backgrounds", "TestValue1"))
            self.assertTrue(isJsonTraitCorrect(os.path.join(tempOutputDir,"0.json"), "Earings", "Earing-none"))        
        
        pass
    

    def testUpdateDescription(self):
        
        # Validate starting point
        self.assertTrue(isJsonDescriptionCorrect("0.json", "Caturday Tales is a collection of randomly generated NFTs"))
        self.assertTrue(isJsonDescriptionCorrect("1.json", "Caturday Tales is a collection of randomly generated NFTs"))
        self.assertTrue(isJsonDescriptionCorrect("2.json", "Caturday Tales is a collection of randomly generated NFTs"))
        
        # Validate updates
        updateDescription(globFilePattern="*.json", newDescription="New description")
        
        # Validate modification
        self.assertTrue(isJsonDescriptionCorrect("0.json", "New description"))
        self.assertTrue(isJsonDescriptionCorrect("1.json", "New description"))
        self.assertTrue(isJsonDescriptionCorrect("2.json", "New description"))
        
        # Restore the updates
        updateDescription(globFilePattern="*.json", newDescription="Caturday Tales is a collection of randomly generated NFTs")
        
        # Validate ending point
        self.assertTrue(isJsonDescriptionCorrect("0.json", "Caturday Tales is a collection of randomly generated NFTs"))
        self.assertTrue(isJsonDescriptionCorrect("1.json", "Caturday Tales is a collection of randomly generated NFTs"))
        self.assertTrue(isJsonDescriptionCorrect("2.json", "Caturday Tales is a collection of randomly generated NFTs"))
        
        # Test absolute path and output directory
        with tempfile.TemporaryDirectory() as tempOutputDir:
            absPath = pathlib.Path().resolve()
            globPattern = os.path.join(absPath, "0.json")
            updateDescription(globFilePattern=globPattern, newDescription="New description", outputDir=tempOutputDir)
            self.assertTrue(isJsonDescriptionCorrect(os.path.join(tempOutputDir,"0.json"), "New description"))
            self.assertTrue(isJsonTraitCorrect(os.path.join(tempOutputDir,"0.json"), "Personality", "Friendly"))
            self.assertTrue(isJsonTraitCorrect(os.path.join(tempOutputDir,"0.json"), "Backgrounds", "Gradient-3"))
            self.assertTrue(isJsonTraitCorrect(os.path.join(tempOutputDir,"0.json"), "Earings", "Earing-none"))       
        
        pass
    

    def testUpdateImageUrlBaseString(self):
        
        # Validate starting point
        self.assertTrue(isJsonImageUrlCorrect("0.json", "https://storage/images/0.png"))
        self.assertTrue(isJsonImageUrlCorrect("1.json", "https://storage/images/1.png"))
        self.assertTrue(isJsonImageUrlCorrect("2.json", "https://storage/images/2.png"))
        
        # Validate updates
        updateImageUrlBaseString(globFilePattern="*.json", newUrlBaseString="https://new/url")
        
        # Validate modification
        self.assertTrue(isJsonImageUrlCorrect("0.json", "https://new/url/0.png"))
        self.assertTrue(isJsonImageUrlCorrect("1.json", "https://new/url/1.png"))
        self.assertTrue(isJsonImageUrlCorrect("2.json", "https://new/url/2.png"))
        
        # Restore the updates
        updateImageUrlBaseString(globFilePattern="*.json", newUrlBaseString="https://storage/images")
        
        # Validate ending point
        self.assertTrue(isJsonImageUrlCorrect("0.json", "https://storage/images/0.png"))
        self.assertTrue(isJsonImageUrlCorrect("1.json", "https://storage/images/1.png"))
        self.assertTrue(isJsonImageUrlCorrect("2.json", "https://storage/images/2.png"))
        
        # Test absolute path and output directory
        with tempfile.TemporaryDirectory() as tempOutputDir:
            absPath = pathlib.Path().resolve()
            globPattern = os.path.join(absPath, "0.json")
            updateImageUrlBaseString(globFilePattern=globPattern, newUrlBaseString="https://new/url", outputDir=tempOutputDir)
            self.assertTrue(isJsonImageUrlCorrect(os.path.join(tempOutputDir,"0.json"), "https://new/url/0.png"))
            self.assertTrue(isJsonTraitCorrect(os.path.join(tempOutputDir,"0.json"), "Personality", "Friendly"))
            self.assertTrue(isJsonTraitCorrect(os.path.join(tempOutputDir,"0.json"), "Backgrounds", "Gradient-3"))
            self.assertTrue(isJsonTraitCorrect(os.path.join(tempOutputDir,"0.json"), "Earings", "Earing-none"))       
        
        pass
    
    def testGenerateStatistics(self):
        
        with tempfile.TemporaryDirectory() as tempOutputDir:
            statsFile = os.path.join(tempOutputDir,"stats.json")
            generateStatistics(globFilePattern="*.json", outputJsonFilename=statsFile)
            
            try:
                with open(statsFile) as f:
                    jsonDict = json.load(f)
                self.assertEqual(jsonDict['Personality']['Friendly'], 1)
                self.assertEqual(jsonDict['Personality']['Shy'], 1)
                self.assertEqual(jsonDict['Personality']['Curious'], 1)
                self.assertEqual(jsonDict['Backgrounds']['Gradient-3'], 1)
                self.assertEqual(jsonDict['Backgrounds']['Psyc-1'], 1)
                self.assertEqual(jsonDict['Backgrounds']['Purple'], 1)
                self.assertEqual(jsonDict['Earings']['Earing-none'], 3)
            except:
                print(statsFile + " -> ignoring non-JSON file ")
                self.assertTrue(False)
        
        pass
    
    def testCombineJsonFiles(self):
        
        with tempfile.TemporaryDirectory() as tempOutputDir:
            statsFile = os.path.join(tempOutputDir,"combine.json")
            combineJsonFiles(globFilePattern="*.json", outputJsonFilename=statsFile)
            
            try:
                with open(statsFile) as f:
                    jsonDict = json.load(f)
                self.assertEqual(jsonDict['0.json']['image'], "https://storage/images/0.png")
                self.assertEqual(jsonDict['0.json']['tokenId'], 0)
                self.assertEqual(jsonDict['0.json']['name'], "Caturday Cat #0000")
                self.assertEqual(jsonDict['0.json']['description'], "Caturday Tales is a collection of randomly generated NFTs")
                self.assertEqual(jsonDict['0.json']['attributes'][0]['trait_type'], "Personality")
                self.assertEqual(jsonDict['0.json']['attributes'][0]['value'], "Friendly")
                self.assertEqual(jsonDict['0.json']['attributes'][1]['trait_type'], "Backgrounds")
                self.assertEqual(jsonDict['0.json']['attributes'][1]['value'], "Gradient-3")
                self.assertEqual(jsonDict['0.json']['attributes'][2]['trait_type'], "Earings")
                self.assertEqual(jsonDict['0.json']['attributes'][2]['value'], "Earing-none")
                
                self.assertEqual(jsonDict['1.json']['image'], "https://storage/images/1.png")
                self.assertEqual(jsonDict['1.json']['tokenId'], 1)
                self.assertEqual(jsonDict['1.json']['name'], "Caturday Cat #0001")
                self.assertEqual(jsonDict['1.json']['description'], "Caturday Tales is a collection of randomly generated NFTs")
                self.assertEqual(jsonDict['1.json']['attributes'][0]['trait_type'], "Personality")
                self.assertEqual(jsonDict['1.json']['attributes'][0]['value'], "Shy")
                self.assertEqual(jsonDict['1.json']['attributes'][1]['trait_type'], "Backgrounds")
                self.assertEqual(jsonDict['1.json']['attributes'][1]['value'], "Psyc-1")
                self.assertEqual(jsonDict['1.json']['attributes'][2]['trait_type'], "Earings")
                self.assertEqual(jsonDict['1.json']['attributes'][2]['value'], "Earing-none")
                
                self.assertEqual(jsonDict['2.json']['image'], "https://storage/images/2.png")
                self.assertEqual(jsonDict['2.json']['tokenId'], 2)
                self.assertEqual(jsonDict['2.json']['name'], "Caturday Cat #0002")
                self.assertEqual(jsonDict['2.json']['description'], "Caturday Tales is a collection of randomly generated NFTs")
                self.assertEqual(jsonDict['2.json']['attributes'][0]['trait_type'], "Personality")
                self.assertEqual(jsonDict['2.json']['attributes'][0]['value'], "Curious")
                self.assertEqual(jsonDict['2.json']['attributes'][1]['trait_type'], "Backgrounds")
                self.assertEqual(jsonDict['2.json']['attributes'][1]['value'], "Purple")
                self.assertEqual(jsonDict['2.json']['attributes'][2]['trait_type'], "Earings")
                self.assertEqual(jsonDict['2.json']['attributes'][2]['value'], "Earing-none")
            except:
                print(statsFile + " -> ignoring non-JSON file ")
                self.assertTrue(False)
        
        pass
    

def isJsonTraitCorrect(filename, trait, value):
    
    try:
        with open(filename) as f:
            jsonDict = json.load(f)
    except:
        print(filename + " -> ignoring non-JSON file ")
        return False
    
    if 'attributes' not in jsonDict.keys():
        return False
    attributesList = jsonDict['attributes']
    
    for attribute in attributesList:
        if 'trait_type' not in attribute.keys():
            continue       
        traitType =  attribute['trait_type']
        if 'value' not in attribute.keys():
            continue       
        traitValue =  attribute['value']
    
        if not(traitType == trait):
            continue
        
        if traitValue == value:
            print(f"--> Validated that {trait} = {value} in {filename}")
            return True
        
    return False


def isJsonDescriptionCorrect(filename, description):
    
    try:
        with open(filename) as f:
            jsonDict = json.load(f)
    except:
        print(filename + " -> ignoring non-JSON file ")
        return False
    
    if 'description' not in jsonDict.keys():
        return False
    
    
    if description == jsonDict['description']:
        print(f"--> Validated that 'description' = {description} in {filename}")
        return True
        
    return False


def isJsonImageUrlCorrect(filename, imageUrl):
    
    try:
        with open(filename) as f:
            jsonDict = json.load(f)
    except:
        print(filename + " -> ignoring non-JSON file ")
        return False
    
    if 'image' not in jsonDict.keys():
        return False
    
    
    if imageUrl == jsonDict['image']:
        print(f"--> Validated that 'image' = {imageUrl} in {filename}")
        return True
        
    return False
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()