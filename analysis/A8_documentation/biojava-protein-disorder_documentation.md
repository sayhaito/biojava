# biojava-protein-disorder — Technical Documentation

---

## Module Overview

**Module:** `biojava-protein-disorder`  
**Total Classes:** 12  
**Packages:** 2

### Packages

- `org.biojava.nbio.data.sequence`
- `org.biojava.nbio.ronn`

### Dependencies

**External:**
- jakarta.xml.bind
- junit
- org.apache.logging.log4j
- org.glassfish.jaxb
- org.slf4j

**Internal:**
- org.biojava.biojava-core

---

## Business Process Flows

### FastaSequence

**Actor:** User  
**Summary:** User uses FastaSequence to manipulates biological sequences

**Steps:**
1. Retrieve Id
2. Retrieve Sequence
3. Retrieve FormattedFasta
4. Retrieve OnelineFasta
5. Retrieve FormatedSequence
6. Retrieve Length
7. Execute toString
8. Execute hashCode

![Activity Diagram](../A7_business_flows/biojava-protein-disorder_FastaSequence_activity.puml)

### SequenceUtil

**Actor:** User  
**Summary:** User uses SequenceUtil to manipulates biological sequences

**Steps:**
1. Execute isNucleotideSequence
2. Execute isNonAmbNucleotideSequence
3. Execute cleanSequence
4. Execute deepCleanSequence
5. Execute isProteinSequence
6. Execute isAmbiguosProtein
7. Read Fasta

![Activity Diagram](../A7_business_flows/biojava-protein-disorder_SequenceUtil_activity.puml)

### ModelLoader

**Actor:** User  
**Summary:** User uses ModelLoader to perform operations

**Steps:**
1. Execute hashCode
2. Execute equals
3. Execute toString
4. Retrieve Model
5. Execute main

![Activity Diagram](../A7_business_flows/biojava-protein-disorder_ModelLoader_activity.puml)

### NullOutputStream

**Actor:** User  
**Summary:** User uses NullOutputStream to perform operations

**Steps:**
1. Write 

![Activity Diagram](../A7_business_flows/biojava-protein-disorder_NullOutputStream_activity.puml)

---

## Key Classes

### FastaSequence

**Package:** `org.biojava.nbio.data.sequence`  
**Type:** class

**Implements:** `Comparable<FastaSequence>`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `String` | id |
| private | `String` | sequence |
| final | `Pattern` | p |
| final | `Matcher` | m |
| final | `StringBuilder` | sb |
| final | `int` | insPos |
| final | `int` | prime |
| final | `FastaSequence` | other |

**Methods:**

- `String getId()`
- `String getSequence()`
- `String getFormattedFasta()`
- `String getOnelineFasta()`
- `String getFormatedSequence(final int width)`
- `int getLength()`
- `String toString()`
- `int hashCode()`
- `boolean equals(final Object obj)`
- `int compareTo(FastaSequence o)`

### SequenceUtil

**Package:** `org.biojava.nbio.data.sequence`  
**Type:** class


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `Logger` | logger |
| public | `Pattern` | WHITE_SPACE |
| public | `Pattern` | DIGIT |
| public | `Pattern` | NONWORD |
| public | `Pattern` | AA |
| public | `Pattern` | NON_AA |
| public | `Pattern` | AMBIGUOUS_AA |
| public | `Pattern` | NUCLEOTIDE |
| public | `Pattern` | AMBIGUOUS_NUCLEOTIDE |
| public | `Pattern` | NON_NUCLEOTIDE |

**Methods:**

- `boolean isNucleotideSequence(final FastaSequence s)`
- `boolean isNonAmbNucleotideSequence(String sequence)`
- `String cleanSequence(String sequence)`
- `String deepCleanSequence(String sequence)`
- `boolean isProteinSequence(String sequence)`
- `boolean isAmbiguosProtein(String sequence)`
- `List<FastaSequence> readFasta(final InputStream inStream)`

### ModelLoader

**Package:** `org.biojava.nbio.ronn`  
**Type:** class


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `Logger` | logger |
| final | `float` | mu0 |
| final | `float` | mu1 |
| final | `float` | sigma0 |
| final | `float` | sigma1 |
| final | `float[]` | values |
| final | `short[][]` | dbAA |
| final | `short[]` | Length |
| final | `float[]` | W |
| final | `int` | prime |

**Methods:**

- `int hashCode()`
- `boolean equals(final Object obj)`
- `String toString()`
- `Model getModel(final int modelNum)`
- `void main(final String[] args)`

### NullOutputStream

**Package:** `org.biojava.nbio.ronn`  
**Type:** class

**Extends:** `OutputStream`  

**Methods:**

- `void write(final int b)`

### Class Diagram

![Class Diagram](../A6_uml/biojava-protein-disorder_class_diagram.puml)

---

## Method Logic Flows

### FastaSequence.getId()

**Execution Steps:**

1. `return id;`

### FastaSequence.getSequence()

**Execution Steps:**

1. `return sequence;`

### FastaSequence.getFormattedFasta()

**Execution Steps:**

1. `return getFormatedSequence(80);`

### SequenceUtil.readFasta()

**Execution Steps:**

1. `final List<FastaSequence> seqs = new ArrayList<>();`
2. `final BufferedReader infasta = new BufferedReader(`
3. `new InputStreamReader(inStream, "UTF8"), 16000);`
4. `final Pattern pattern = Pattern.compile("`
5. `String sname = "", seqstr = null;`
6. `line = infasta.readLine();`
7. `if ((line == null) || line.startsWith(">")) {`
8. `if (seqstr != null) {`
9. `seqs.add(new FastaSequence(sname.substring(1), seqstr));`
10. `sname = line;`
11. `seqstr = "";`
12. `final String subseq = pattern.matcher(line).replaceAll("");`
13. `seqstr += subseq;`
14. `infasta.close();`
15. `return seqs;`

**Conditional Logic:**

- **Condition:** `(line == null) || line.startsWith(">")`
- **Condition:** `seqstr != null`

**External Calls:**

- `Pattern.compile()`
- `infasta.readLine()`
- `line.startsWith()`
- `seqs.add()`
- `sname.substring()`
- `pattern.matcher()`
- `infasta.close()`

**Exceptions:** `IOException`

### ModelLoader.getModel()

**Execution Steps:**

1. `return ModelLoader.models.get(modelNum);`

**Exceptions:** `IOException`

### Sequence Diagram

![Sequence Diagram](../A6_uml/biojava-protein-disorder_sequence_diagram.puml)

---
