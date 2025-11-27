# biojava-genome — Technical Documentation

---

## Module Overview

**Module:** `biojava-genome`  
**Total Classes:** 51  
**Packages:** 11

### Packages

- `org.biojava.nbio.genome`
- `org.biojava.nbio.genome.homology`
- `org.biojava.nbio.genome.io.fastq`
- `org.biojava.nbio.genome.parsers.cytoband`
- `org.biojava.nbio.genome.parsers.geneid`
- `org.biojava.nbio.genome.parsers.genename`
- `org.biojava.nbio.genome.parsers.gff`
- `org.biojava.nbio.genome.parsers.twobit`
- `org.biojava.nbio.genome.query`
- `org.biojava.nbio.genome.uniprot`
- `org.biojava.nbio.genome.util`

### Dependencies

**External:**
- com.google.guava
- junit
- junit-addons
- org.apache.logging.log4j
- org.slf4j

**Internal:**
- org.biojava.biojava-alignment
- org.biojava.biojava-core

---

## Business Process Flows

### GeneNamesParser

**Actor:** System  
**Summary:** System uses GeneNamesParser to parses input data

**Steps:**
1. Execute main
2. Retrieve GeneNames
3. Retrieve GeneNames
4. Retrieve GeneName

![Activity Diagram](../A7_business_flows/biojava-genome_GeneNamesParser_activity.puml)

### GeneChromosomePositionParser

**Actor:** System  
**Summary:** System uses GeneChromosomePositionParser to parses input data

**Steps:**
1. Execute main
2. Retrieve ChromosomeMappings
3. Retrieve ChromosomeMappings
4. Retrieve GeneChromosomePosition
5. Retrieve IntegerList

![Activity Diagram](../A7_business_flows/biojava-genome_GeneChromosomePositionParser_activity.puml)

### GFF3Reader

**Actor:** System  
**Summary:** System uses GFF3Reader to reads data from source

**Steps:**
1. Read 
2. Read 
3. Read 
4. Read 
5. Parse Line
6. Execute main

![Activity Diagram](../A7_business_flows/biojava-genome_GFF3Reader_activity.puml)

### GeneIDGFF2Reader

**Actor:** System  
**Summary:** System uses GeneIDGFF2Reader to reads data from source

**Steps:**
1. Read 
2. Parse Line
3. Write 
4. Write Line
5. Execute main

![Activity Diagram](../A7_business_flows/biojava-genome_GeneIDGFF2Reader_activity.puml)

---

## Key Classes

### GeneNamesParser

**Package:** `org.biojava.nbio.genome.parsers.genename`  
**Type:** class


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `Logger` | logger |
| public | `String` | DEFAULT_GENENAMES_URL |

**Methods:**

- `void main(String[] args)`
- `List<GeneName> getGeneNames()`
- `List<GeneName> getGeneNames(InputStream inStream)`
- `GeneName getGeneName(String line)`

### GeneChromosomePositionParser

**Package:** `org.biojava.nbio.genome.parsers.genename`  
**Type:** class


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `Logger` | logger |
| public | `String` | DEFAULT_MAPPING_URL |

**Methods:**

- `void main(String[] args)`
- `List<GeneChromosomePosition> getChromosomeMappings()`
- `List<GeneChromosomePosition> getChromosomeMappings(InputStream inStream)`
- `GeneChromosomePosition getGeneChromosomePosition(String line)`
- `List<Integer> getIntegerList(String lst)`

### FeatureI

**Package:** `org.biojava.nbio.genome.parsers.gff`  
**Type:** interface


### GFF3Reader

**Package:** `org.biojava.nbio.genome.parsers.gff`  
**Type:** class


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `Logger` | logger |
| private | `Pattern` | p |

**Methods:**

- `FeatureList read(String filename, List<String> indexes)`
- `FeatureList read(Path path, List<String> indexes)`
- `FeatureList read(String filename)`
- `FeatureList read(Path path)`
- `Feature parseLine(String s)`
- `void main(String[] args)`

### GeneIDGFF2Reader

**Package:** `org.biojava.nbio.genome.parsers.gff`  
**Type:** class


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `Logger` | logger |

**Methods:**

- `FeatureList read(String filename)`
- `Feature parseLine(String s)`
- `void write(FeatureList features, String filename)`
- `void writeLine(Feature f, BufferedWriter bw)`
- `void main(String[] args)`

### GFF3Writer

**Package:** `org.biojava.nbio.genome.parsers.gff`  
**Type:** class


**Methods:**

- `void write(OutputStream outputStream, Map<String, ChromosomeSequence> chromosomeSequenceList)`
- `String getGFF3Note(List<String> notesList)`

### GeneMarkGTFReader

**Package:** `org.biojava.nbio.genome.parsers.gff`  
**Type:** class


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `Logger` | logger |

**Methods:**

- `FeatureList read(String filename)`
- `Feature parseLine(String s)`
- `void main(String[] args)`

### CytobandParser

**Package:** `org.biojava.nbio.genome.parsers.cytoband`  
**Type:** class


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `Logger` | logger |
| public | `String` | DEFAULT_LOCATION |

**Methods:**

- `void main(String[] args)`
- `SortedSet<Cytoband> getAllCytobands(URL u)`
- `SortedSet<Cytoband> getAllCytobands(InputStream instream)`

### Class Diagram

![Class Diagram](../A6_uml/biojava-genome_class_diagram.puml)

---

## Method Logic Flows

### GeneNamesParser.getGeneNames()

**Execution Steps:**

1. `URL url = new URL(DEFAULT_GENENAMES_URL);`
2. `InputStreamProvider prov = new InputStreamProvider();`
3. `InputStream inStream = prov.getInputStream(url);`
4. `return getGeneNames(inStream);`

**External Calls:**

- `prov.getInputStream()`

**Exceptions:** `IOException`

### GeneNamesParser.getGeneNames()

**Execution Steps:**

1. `URL url = new URL(DEFAULT_GENENAMES_URL);`
2. `InputStreamProvider prov = new InputStreamProvider();`
3. `InputStream inStream = prov.getInputStream(url);`
4. `return getGeneNames(inStream);`

**External Calls:**

- `prov.getInputStream()`

**Exceptions:** `IOException`

### GeneNamesParser.getGeneName()

**Execution Steps:**

1. `if (line == null)`
2. `return null;`
3. `String[] s = line.split("\t");`
4. `if ( s.length != 13) {`
5. `logger.warn("Line does not contain 13 data items, but {}: {}", s.length, line);`
6. `logger.warn(line.replaceAll("\t", "|---|"));`
7. `return null;`
8. `GeneName gn = new GeneName();`
9. `gn.setApprovedSymbol(s[0]);`
10. `gn.setApprovedName(s[1]);`
11. `gn.setStatus(s[2]);`
12. `gn.setPreviousSymbols(s[3]);`
13. `gn.setPreviousNames(s[4]);`
14. `gn.setSynonyms(s[5]);`
15. `gn.setChromosome(s[6]);`
16. `gn.setAccessionNr(s[7]);`
17. `gn.setOmimId(s[8]);`
18. `gn.setRefseqIds(s[9]);`
19. `gn.setEnsemblGeneId(s[10]);`
20. `gn.setUniprot(s[11]);`

**Conditional Logic:**

- **Condition:** `s.length != 13`

**External Calls:**

- `line.split()`
- `logger.warn()`
- `line.replaceAll()`
- `gn.setApprovedSymbol()`
- `gn.setApprovedName()`
- `gn.setStatus()`
- `gn.setPreviousSymbols()`
- `gn.setPreviousNames()`
- `gn.setSynonyms()`
- `gn.setChromosome()`

**Exceptions:** `IOException`

### GeneChromosomePositionParser.getChromosomeMappings()

**Execution Steps:**

1. `URL url = new URL(DEFAULT_MAPPING_URL);`
2. `InputStreamProvider prov = new InputStreamProvider();`
3. `InputStream inStream = prov.getInputStream(url);`
4. `return getChromosomeMappings(inStream);`

**External Calls:**

- `prov.getInputStream()`

**Exceptions:** `IOException`

### GeneChromosomePositionParser.getChromosomeMappings()

**Execution Steps:**

1. `URL url = new URL(DEFAULT_MAPPING_URL);`
2. `InputStreamProvider prov = new InputStreamProvider();`
3. `InputStream inStream = prov.getInputStream(url);`
4. `return getChromosomeMappings(inStream);`

**External Calls:**

- `prov.getInputStream()`

**Exceptions:** `IOException`

### Sequence Diagram

![Sequence Diagram](../A6_uml/biojava-genome_sequence_diagram.puml)

---
