# biojava-aa-prop — Technical Documentation

---

## Module Overview

**Module:** `biojava-aa-prop`  
**Total Classes:** 32  
**Packages:** 4

### Packages

- `org.biojava.nbio.aaproperties`
- `org.biojava.nbio.aaproperties.profeat`
- `org.biojava.nbio.aaproperties.profeat.convertor`
- `org.biojava.nbio.aaproperties.xml`

### Dependencies

**External:**
- jakarta.xml.bind
- junit
- org.apache.logging.log4j
- org.glassfish.jaxb
- org.slf4j

**Internal:**
- org.biojava.biojava-core
- org.biojava.biojava-structure

---

## Business Process Flows

### Convert2SecondaryStructure

**Actor:** User  
**Summary:** User uses Convert2SecondaryStructure to processes molecular structures

**Steps:**
1. Execute convert
2. Retrieve Grouping
3. Retrieve Attribute

![Activity Diagram](../A7_business_flows/biojava-aa-prop_Convert2SecondaryStructure_activity.puml)

### PeptidePropertiesImpl

**Actor:** User  
**Summary:** User uses PeptidePropertiesImpl to perform operations

**Steps:**
1. Retrieve WaterMoleculeWeight
2. Retrieve Sequence
3. Retrieve MolecularWeight
4. Retrieve MolecularWeight
5. Retrieve MolecularWeight
6. Retrieve MolecularWeightBasedOnXML
7. Execute obtainAminoAcidCompositionTable
8. Execute obtainAminoAcidCompositionTable

![Activity Diagram](../A7_business_flows/biojava-aa-prop_PeptidePropertiesImpl_activity.puml)

### Utils

**Actor:** User  
**Summary:** User uses Utils to perform operations

**Steps:**
1. Execute checkSequence
2. Execute checkSequence

![Activity Diagram](../A7_business_flows/biojava-aa-prop_Utils_activity.puml)

### CommandPrompt

**Actor:** User  
**Summary:** User uses CommandPrompt to perform operations

**Steps:**
1. Execute main
2. Execute run
3. Execute printHeader
4. Execute showHelp

![Activity Diagram](../A7_business_flows/biojava-aa-prop_CommandPrompt_activity.puml)

---

## Key Classes

### IPeptideProperties

**Package:** `org.biojava.nbio.aaproperties`  
**Type:** interface


### Convert2SecondaryStructure

**Package:** `org.biojava.nbio.aaproperties.profeat.convertor`  
**Type:** class

**Extends:** `Convertor`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `String[]` | subCategory |

**Methods:**

- `char convert(char c)`
- `String[] getGrouping()`
- `String getAttribute()`

### PeptidePropertiesImpl

**Package:** `org.biojava.nbio.aaproperties`  
**Type:** class

**Implements:** `IPeptideProperties`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| final | `Logger` | logger |
| final | `double` | hydrogenMW |
| final | `double` | hydroxideMW |
| final | `double` | a |
| final | `double` | b |
| final | `double` | difference |
| private | `double[][]` | cPk |
| private | `double` | PH_MIN |
| private | `double` | PH_MAX |
| private | `double` | MAXLOOP |

**Methods:**

- `double getWaterMoleculeWeight()`
- `char[] getSequence(String sequence, boolean ignoreCase)`
- `double getMolecularWeight(ProteinSequence sequence)`
- `double getMolecularWeight(ProteinSequence sequence, File aminoAcidCompositionFile)`
- `double getMolecularWeight(ProteinSequence sequence, File elementMassFile, File aminoAcidCompositionFile)`
- `double getMolecularWeightBasedOnXML(ProteinSequence sequence, AminoAcidCompositionTable aminoAcidCompositionTable)`
- `AminoAcidCompositionTable obtainAminoAcidCompositionTable(File aminoAcidCompositionFile)`
- `AminoAcidCompositionTable obtainAminoAcidCompositionTable(File elementMassFile, File aminoAcidCompositionFile)`
- `double getExtinctionCoefficient(ProteinSequence sequence, boolean assumeCysReduced)`
- `double getAbsorbance(ProteinSequence sequence, boolean assumeCysReduced)`

### Utils

**Package:** `org.biojava.nbio.aaproperties`  
**Type:** class


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| final | `Logger` | logger |
| final | `Set<Character>` | characterSet |

**Methods:**

- `String checkSequence(String sequence)`
- `String checkSequence(String sequence, Set<Character> cSet)`

### CommandPrompt

**Package:** `org.biojava.nbio.aaproperties`  
**Type:** class


**Methods:**

- `void main(String[] args)`
- `void run(String[] args)`
- `void printHeader(PrintStream output, List<Character> propertyList, List<Character> specificList, String delimiter)`
- `void showHelp()`

### Class Diagram

![Class Diagram](../A6_uml/biojava-aa-prop_class_diagram.puml)

---

## Method Logic Flows

### Convert2SecondaryStructure.getGrouping()

**Execution Steps:**

1. `return subCategory;`

### Convert2SecondaryStructure.getAttribute()

**Execution Steps:**

1. `return "Secondary Structure";`

### PeptidePropertiesImpl.getWaterMoleculeWeight()

**Execution Steps:**

1. `final double hydrogenMW = 1.0079;`
2. `final double hydroxideMW = 17.0073;`
3. `return hydrogenMW + hydroxideMW;`

**Exceptions:** `JAXBException`, `FileNotFoundException`

### PeptidePropertiesImpl.getSequence()

**Execution Steps:**

1. `if(ignoreCase){`
2. `return sequence.toUpperCase().toCharArray();`
3. `return sequence.toCharArray();`

**Conditional Logic:**

- **Condition:** `ignoreCase`

**External Calls:**

- `sequence.toUpperCase()`
- `sequence.toCharArray()`

**Exceptions:** `JAXBException`, `FileNotFoundException`

### PeptidePropertiesImpl.getMolecularWeight()

**Execution Steps:**

1. `double value = 0.0;`
2. `AminoAcidCompoundSet aaSet = new AminoAcidCompoundSet();`
3. `char[] seq = getSequence(sequence.toString(), true);`
4. `for(char aa:seq){`
5. `AminoAcidCompound c = aaSet.getCompoundForString(String.valueOf(aa));`
6. `if(Constraints.aa2MolecularWeight.containsKey(c)){`
7. `value += Constraints.aa2MolecularWeight.get(c);`
8. `if(value == 0)`
9. `return value;`
10. `return value + getWaterMoleculeWeight();`

**Conditional Logic:**

- **Condition:** `Constraints.aa2MolecularWeight.containsKey(c)`

**Loops:**

- **Type:** for
- **Type:** foreach

**External Calls:**

- `aaSet.getCompoundForString()`
- `String.valueOf()`
- `aa2MolecularWeight.containsKey()`

**Exceptions:** `JAXBException`, `FileNotFoundException`

### Sequence Diagram

![Sequence Diagram](../A6_uml/biojava-aa-prop_sequence_diagram.puml)

---
