# biojava-core — Technical Documentation

---

## Module Overview

**Module:** `biojava-core`  
**Total Classes:** 186  
**Packages:** 23

### Packages

- `org.biojava.nbio.core.alignment`
- `org.biojava.nbio.core.alignment.matrices`
- `org.biojava.nbio.core.alignment.template`
- `org.biojava.nbio.core.exceptions`
- `org.biojava.nbio.core.search.io`
- `org.biojava.nbio.core.search.io.blast`
- `org.biojava.nbio.core.sequence`
- `org.biojava.nbio.core.sequence.compound`
- `org.biojava.nbio.core.sequence.edits`
- `org.biojava.nbio.core.sequence.features`
- `org.biojava.nbio.core.sequence.io`
- `org.biojava.nbio.core.sequence.io.embl`
- `org.biojava.nbio.core.sequence.io.template`
- `org.biojava.nbio.core.sequence.io.util`
- `org.biojava.nbio.core.sequence.loader`

### Dependencies

**External:**
- jakarta.xml.bind
- junit
- org.apache.logging.log4j
- org.glassfish.jaxb
- org.junit.jupiter
- org.junit.vintage
- org.slf4j

---

## Business Process Flows

### PrettyXMLWriter

**Actor:** User  
**Summary:** User uses PrettyXMLWriter to writes data to destination

**Steps:**
1. Execute declareNamespace
2. Execute handleDeclaredNamespaces
3. Write Indent
4. Execute _openTag
5. Execute allocPrefix
6. Execute openTag
7. Execute openTag
8. Execute attribute

![Activity Diagram](../A7_business_flows/biojava-core_PrettyXMLWriter_activity.puml)

### SequenceTools

**Actor:** User  
**Summary:** User uses SequenceTools to manipulates biological sequences

**Steps:**
1. Execute permuteCyclic
2. Execute percentNucleotideSequence
3. Execute isNucleotideSequence
4. Execute equalLengthSequences

![Activity Diagram](../A7_business_flows/biojava-core_SequenceTools_activity.puml)

### BlastHitBuilder

**Actor:** User  
**Summary:** User uses BlastHitBuilder to constructs objects

**Steps:**
1. Set HitNum
2. Set HitId
3. Set HitDef
4. Set HitAccession
5. Set HitLen
6. Set HitSequence
7. Set Hsps
8. Create BlastHit

![Activity Diagram](../A7_business_flows/biojava-core_BlastHitBuilder_activity.puml)

---

## Key Classes

### XMLWriter

**Package:** `org.biojava.nbio.core.util`  
**Type:** interface


### PrettyXMLWriter

**Package:** `org.biojava.nbio.core.util`  
**Type:** class

**Implements:** `XMLWriter`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `int` | indentUnit |
| private | `PrintWriter` | writer |
| private | `boolean` | isOpeningTag |
| private | `boolean` | afterNewline |
| private | `int` | indent |
| private | `int` | namespaceSeed |
| private | `LinkedList<List<String>>` | namespaceBindings |
| private | `List<String>` | namespacesDeclared |

**Methods:**

- `void declareNamespace(String nsURI, String prefixHint)`
- `void handleDeclaredNamespaces()`
- `void writeIndent()`
- `void _openTag()`
- `String allocPrefix(String nsURI)`
- `void openTag(String nsURI, String localName)`
- `void openTag(String qName)`
- `void attribute(String nsURI, String localName, String value)`
- `void attribute(String qName, String value)`
- `void _closeTag()`

### SequenceTools

**Package:** `org.biojava.nbio.core.util`  
**Type:** class


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| protected | `String` | NUCLEOTIDE_LETTERS |

**Methods:**

- `String permuteCyclic(String string, int n)`
- `int percentNucleotideSequence(String sequence)`
- `boolean isNucleotideSequence(String sequence)`
- `boolean equalLengthSequences(ProteinSequence[] sequences)`

### ResultFactory

**Package:** `org.biojava.nbio.core.search.io`  
**Type:** interface


### BlastHitBuilder

**Package:** `org.biojava.nbio.core.search.io.blast`  
**Type:** class


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `int` | hitNum |
| private | `String` | hitId |
| private | `String` | hitDef |
| private | `String` | hitAccession |
| private | `int` | hitLen |
| private | `Sequence` | hitSequence |
| private | `List<Hsp>` | hsps |

**Methods:**

- `BlastHitBuilder setHitNum(int hitNum)`
- `BlastHitBuilder setHitId(String hitId)`
- `BlastHitBuilder setHitDef(String hitDef)`
- `BlastHitBuilder setHitAccession(String hitAccession)`
- `BlastHitBuilder setHitLen(int hitLen)`
- `BlastHitBuilder setHitSequence(Sequence s)`
- `BlastHitBuilder setHsps(List<Hsp> hsps)`
- `BlastHit createBlastHit()`

### BlastResultBuilder

**Package:** `org.biojava.nbio.core.search.io.blast`  
**Type:** class


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `String` | program |
| private | `String` | version |
| private | `String` | reference |
| private | `String` | dbFile |
| private | `int` | iterationNumber |
| private | `String` | queryID |
| private | `String` | queryDef |
| private | `int` | queryLength |
| private | `Sequence` | querySequence |
| private | `List<Hit>` | hits |

**Methods:**

- `BlastResultBuilder setProgram(String program)`
- `BlastResultBuilder setVersion(String version)`
- `BlastResultBuilder setReference(String reference)`
- `BlastResultBuilder setDbFile(String dbFile)`
- `BlastResultBuilder setProgramSpecificParameters(Map<String, String> programSpecificParameters)`
- `BlastResultBuilder setIterationNumber(int iterationNumber)`
- `BlastResultBuilder setQueryID(String queryID)`
- `BlastResultBuilder setQueryDef(String queryDef)`
- `BlastResultBuilder setQueryLength(int queryLength)`
- `BlastResultBuilder setHits(List<Hit> hits)`

### BlastHspBuilder

**Package:** `org.biojava.nbio.core.search.io.blast`  
**Type:** class


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `int` | hspNum |
| private | `double` | hspBitScore |
| private | `int` | hspScore |
| private | `double` | hspEvalue |
| private | `int` | hspQueryFrom |
| private | `int` | hspQueryTo |
| private | `int` | hspHitFrom |
| private | `int` | hspHitTo |
| private | `int` | hspQueryFrame |
| private | `int` | hspHitFrame |

**Methods:**

- `BlastHspBuilder setHspNum(int hspNum)`
- `BlastHspBuilder setHspBitScore(double hspBitScore)`
- `BlastHspBuilder setHspScore(int hspScore)`
- `BlastHspBuilder setHspEvalue(double hspEvalue)`
- `BlastHspBuilder setHspQueryFrom(int hspQueryFrom)`
- `BlastHspBuilder setHspQueryTo(int hspQueryTo)`
- `BlastHspBuilder setHspHitFrom(int hspHitFrom)`
- `BlastHspBuilder setHspHitTo(int hspHitTo)`
- `BlastHspBuilder setHspQueryFrame(int hspQueryFrame)`
- `BlastHspBuilder setHspHitFrame(int hspHitFrame)`

### BlastXMLParser

**Package:** `org.biojava.nbio.core.search.io.blast`  
**Type:** class

**Implements:** `ResultFactory`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `File` | targetFile |

**Methods:**

- `void setFile(File f)`
- `void readFile(String blastFile)`
- `List<Result> createObjects(double maxEScore)`
- `List<String> getFileExtensions()`
- `void setQueryReferences(List<Sequence> sequences)`
- `void setDatabaseReferences(List<Sequence> sequences)`
- `void mapIds()`
- `void storeObjects(List<Result> results)`

### Class Diagram

![Class Diagram](../A6_uml/biojava-core_class_diagram.puml)

---

## Method Logic Flows

### PrettyXMLWriter.writeIndent()

**Execution Steps:**

1. `for (int i = 0; i < indent * indentUnit; ++i) {`
2. `writer.write(' ');`

**Loops:**

- **Type:** for

**External Calls:**

- `writer.write()`

**Exceptions:** `IOException`

### PrettyXMLWriter._closeTag()

**Execution Steps:**

1. `isOpeningTag = false;`
2. `afterNewline = true;`
3. `List<String> hereBindings = namespaceBindings.removeLast();`
4. `if (hereBindings != null) {`
5. `for (Iterator<String> bi = hereBindings.iterator(); bi.hasNext(); ) {`
6. `namespacePrefixes.remove(bi.next());`

**Conditional Logic:**

- **Condition:** `hereBindings != null`

**Loops:**

- **Type:** for

**External Calls:**

- `namespaceBindings.removeLast()`
- `hereBindings.iterator()`
- `bi.hasNext()`
- `namespacePrefixes.remove()`
- `bi.next()`

**Exceptions:** `IOException`

### PrettyXMLWriter.closeTag()

**Execution Steps:**

1. `String prefix = namespacePrefixes.get(nsURI);`
2. `if (prefix == null) {`
3. `throw new IOException("Assertion failed: unknown namespace when closing tag");`
4. `if (isOpeningTag) {`
5. `writer.println(" />");`
6. `if (afterNewline) {`
7. `writeIndent();`
8. `writer.print("</");`
9. `writer.print(prefix);`
10. `writer.print(':');`
11. `writer.print(localName);`
12. `writer.println('>');`
13. `_closeTag();`

**Conditional Logic:**

- **Condition:** `prefix == null`
- **Condition:** `isOpeningTag`
- **Condition:** `afterNewline`

**External Calls:**

- `writer.println()`
- `writer.print()`

**Exceptions:** `IOException`

### BlastHitBuilder.setHitNum()

**Execution Steps:**

1. `this.hitNum = hitNum;`
2. `return this;`

### BlastHitBuilder.setHitId()

**Execution Steps:**

1. `this.hitId = hitId;`
2. `return this;`

### Sequence Diagram

![Sequence Diagram](../A6_uml/biojava-core_sequence_diagram.puml)

---
