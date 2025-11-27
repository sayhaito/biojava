# biojava-alignment — Technical Documentation

---

## Module Overview

**Module:** `biojava-alignment`  
**Total Classes:** 48  
**Packages:** 5

### Packages

- `org.biojava.nbio.alignment`
- `org.biojava.nbio.alignment.io`
- `org.biojava.nbio.alignment.routines`
- `org.biojava.nbio.alignment.template`
- `org.biojava.nbio.phylo`

### Dependencies

**External:**
- junit
- org.apache.logging.log4j
- org.biojava.thirdparty
- org.slf4j

**Internal:**
- org.biojava.biojava-core

---

## Business Process Flows

### AnchoredPairwiseSequenceAligner

**Actor:** User  
**Summary:** User uses AnchoredPairwiseSequenceAligner to manipulates biological sequences

**Steps:**
1. Retrieve Anchors
2. Set Anchors
3. Execute addAnchor
4. Set Profile

![Activity Diagram](../A7_business_flows/biojava-alignment_AnchoredPairwiseSequenceAligner_activity.puml)

### StockholmStructure

**Actor:** User  
**Summary:** User uses StockholmStructure to processes molecular structures

**Steps:**
1. Retrieve FileAnnotation
2. Retrieve ConsAnnotation
3. Execute appendToSequence
4. Retrieve SequenceAnnotation
5. Execute addGSAccessionNumber
6. Execute addGSDescription
7. Execute addGSdbReference
8. Execute addGSOrganismSpecies

![Activity Diagram](../A7_business_flows/biojava-alignment_StockholmStructure_activity.puml)

### StockholmSequenceAnnotation

**Actor:** User  
**Summary:** User uses StockholmSequenceAnnotation to manipulates biological sequences

**Steps:**
1. Retrieve Description
2. Set Description
3. Execute addToDescription
4. Retrieve DbReferences
5. Set DbReferences
6. Execute addDBReference
7. Retrieve AccessionNumber
8. Set AccessionNumber

![Activity Diagram](../A7_business_flows/biojava-alignment_StockholmSequenceAnnotation_activity.puml)

### StockholmFileParser

**Actor:** System  
**Summary:** System uses StockholmFileParser to parses input data

**Steps:**
1. Parse 
2. Parse 
3. Parse 
4. Parse 
5. Parse Next
6. Execute handleSequenceLine
7. Execute handleFileAnnotation
8. Execute handleConsensusAnnotation

![Activity Diagram](../A7_business_flows/biojava-alignment_StockholmFileParser_activity.puml)

---

## Key Classes

### Alignments

**Package:** `org.biojava.nbio.alignment`  
**Type:** class


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| final | `Logger` | logger |

### AnchoredPairwiseSequenceAligner

**Package:** `org.biojava.nbio.alignment.routines`  
**Type:** class


**Methods:**

- `int[] getAnchors()`
- `void setAnchors(int[] anchors)`
- `void addAnchor(int queryIndex, int targetIndex)`
- `void setProfile(List<Step> sx, List<Step> sy)`

### StockholmStructure

**Package:** `org.biojava.nbio.alignment.io`  
**Type:** class


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| final | `Logger` | logger |
| public | `String` | PFAM |
| public | `String` | RFAM |
| private | `StockholmFileAnnotation` | fileAnnotation |
| private | `StockholmConsensusAnnotation` | consAnnotation |
| public | `String` | EXPERT |
| public | `String` | MIM |
| public | `String` | PFAMB |
| public | `String` | PRINTS |
| public | `String` | PROSITE |

**Methods:**

- `StockholmFileAnnotation getFileAnnotation()`
- `StockholmConsensusAnnotation getConsAnnotation()`
- `void appendToSequence(String seqName, String seqText)`
- `StockholmSequenceAnnotation getSequenceAnnotation(String seqName)`
- `void addGSAccessionNumber(String seqName, String text)`
- `void addGSDescription(String seqName, String text)`
- `void addGSdbReference(String seqName, String text)`
- `void addGSOrganismSpecies(String seqName, String text)`
- `void addGSOrganismClassification(String seqName, String text)`
- `void addGSLook(String seqName, String text)`

### StockholmSequenceAnnotation

**Package:** `org.biojava.nbio.alignment.io`  
**Type:** class


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `String` | accessionNumber |
| private | `CharSequence` | description |
| private | `Set<DatabaseReference>` | dbReferences |
| private | `String` | organism |
| private | `String` | organismClassification |
| private | `String` | look |

**Methods:**

- `String getDescription()`
- `void setDescription(CharSequence description)`
- `void addToDescription(CharSequence description)`
- `Set<DatabaseReference> getDbReferences()`
- `void setDbReferences(Set<DatabaseReference> dbReferences)`
- `void addDBReference(String dbReferenceRepresentingString)`
- `String getAccessionNumber()`
- `void setAccessionNumber(String accessionNumber)`
- `String getOrganism()`
- `void setOrganism(String organism)`

### StockholmFileParser

**Package:** `org.biojava.nbio.alignment.io`  
**Type:** class


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| final | `Logger` | logger |
| public | `int` | INFINITY |
| private | `String` | GENERIC_PER_FILE_ANNOTATION |
| private | `String` | GENERIC_PER_CONSENSUS_ANNOTATION |
| private | `String` | GENERIC_PER_SEQUENCE_ANNOTATION |
| private | `String` | GENERIC_PER_RESIDUE_ANNOTATION |
| private | `String` | GF_ACCESSION_NUMBER |
| private | `String` | GF_IDENTIFICATION |
| private | `String` | GF_DEFINITION |
| private | `String` | GF_AUTHOR |

**Methods:**

- `StockholmStructure parse(String filename)`
- `List<StockholmStructure> parse(String filename, int max)`
- `StockholmStructure parse(InputStream inStream)`
- `List<StockholmStructure> parse(InputStream inStream, int max)`
- `List<StockholmStructure> parseNext(int max)`
- `void handleSequenceLine(String line)`
- `void handleFileAnnotation(String featureName, String value)`
- `void handleConsensusAnnotation(String featureName, String value)`
- `void handleSequenceAnnotation(String seqName, String featureName, String value)`
- `void handleResidueAnnotation(String seqName, String featureName, String value)`

### MatrixAligner

**Package:** `org.biojava.nbio.alignment.template`  
**Type:** interface


### PairwiseSequenceAligner

**Package:** `org.biojava.nbio.alignment.template`  
**Type:** interface


### HierarchicalClusterer

**Package:** `org.biojava.nbio.alignment.template`  
**Type:** interface


### Class Diagram

![Class Diagram](../A6_uml/biojava-alignment_class_diagram.puml)

---

## Method Logic Flows

### AnchoredPairwiseSequenceAligner.getAnchors()

**Execution Steps:**

1. `int[] anchor = new int[getScoreMatrixDimensions()[0] - 1];`
2. `for (int i = 0; i < anchor.length; i++) {`
3. `anchor[i] = -1;`
4. `for (int i = 0; i < anchors.size(); i++) {`
5. `anchor[anchors.get(i).getQueryIndex()] = anchors.get(i).getTargetIndex();`
6. `return anchor;`

**Loops:**

- **Type:** for
- **Type:** for

### AnchoredPairwiseSequenceAligner.setAnchors()

**Execution Steps:**

1. `super.anchors = new ArrayList<>();`
2. `if (anchors != null) {`
3. `for (int i = 0; i < anchors.length; i++) {`
4. `if (anchors[i] >= 0) {`
5. `addAnchor(i, anchors[i]);`

**Conditional Logic:**

- **Condition:** `anchors != null`
- **Condition:** `anchors[i] >= 0`

**Loops:**

- **Type:** for

### AnchoredPairwiseSequenceAligner.setProfile()

**Execution Steps:**

1. `profile = pair = new SimpleSequencePair<>(getQuery(), getTarget(), sx, sy);`

### StockholmStructure.getFileAnnotation()

**Execution Steps:**

1. `return fileAnnotation;`

### StockholmStructure.getConsAnnotation()

**Execution Steps:**

1. `return consAnnotation;`

### Sequence Diagram

![Sequence Diagram](../A6_uml/biojava-alignment_sequence_diagram.puml)

---
