# biojava-structure — Technical Documentation

---

## Module Overview

**Module:** `biojava-structure`  
**Total Classes:** 406  
**Packages:** 44

### Packages

- `org.biojava.nbio.structure`
- `org.biojava.nbio.structure.align`
- `org.biojava.nbio.structure.align.ce`
- `org.biojava.nbio.structure.align.client`
- `org.biojava.nbio.structure.align.fatcat`
- `org.biojava.nbio.structure.align.fatcat.calc`
- `org.biojava.nbio.structure.align.helper`
- `org.biojava.nbio.structure.align.model`
- `org.biojava.nbio.structure.align.multiple`
- `org.biojava.nbio.structure.align.multiple.mc`
- `org.biojava.nbio.structure.align.multiple.util`
- `org.biojava.nbio.structure.align.pairwise`
- `org.biojava.nbio.structure.align.quaternary`
- `org.biojava.nbio.structure.align.seq`
- `org.biojava.nbio.structure.align.util`

### Dependencies

**External:**
- com.fasterxml.jackson.core
- jakarta.xml.bind
- java3d
- junit
- org.apache.logging.log4j
- org.glassfish.jaxb
- org.jgrapht
- org.junit.jupiter
- org.junit.vintage
- org.rcsb

**Internal:**
- org.biojava.biojava-alignment
- org.biojava.biojava-core

---

## Business Process Flows

### StructureIO

**Actor:** User  
**Summary:** User uses StructureIO to processes molecular structures

**Steps:**
1. Retrieve Structure
2. Execute checkInitAtomCache
3. Set AtomCache
4. Retrieve AtomCache
5. Retrieve BiologicalAssembly
6. Retrieve BiologicalAssembly
7. Retrieve BiologicalAssembly
8. Retrieve BiologicalAssembly

![Activity Diagram](../A7_business_flows/biojava-structure_StructureIO_activity.puml)

### StructureTools

**Actor:** User  
**Summary:** User uses StructureTools to processes molecular structures

**Steps:**
1. Retrieve NrAtoms
2. Retrieve NrGroups
3. Retrieve AtomArray
4. Retrieve AllAtomArray
5. Retrieve AllAtomArray
6. Retrieve AllAtomArray
7. Retrieve UnalignedGroups
8. Retrieve LigandsByProximity

![Activity Diagram](../A7_business_flows/biojava-structure_StructureTools_activity.puml)

---

## Key Classes

### PDBRecord

**Package:** `org.biojava.nbio.structure`  
**Type:** interface

**Extends:** `Serializable`  

### Chain

**Package:** `org.biojava.nbio.structure`  
**Type:** interface

**Extends:** `Serializable`  

### Atom

**Package:** `org.biojava.nbio.structure`  
**Type:** interface

**Extends:** `Cloneable, PDBRecord`  

### StructureIO

**Package:** `org.biojava.nbio.structure`  
**Type:** class


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `AtomCache` | cache |

**Methods:**

- `Structure getStructure(String name)`
- `void checkInitAtomCache()`
- `void setAtomCache(AtomCache c)`
- `AtomCache getAtomCache()`
- `Structure getBiologicalAssembly(String pdbId, boolean multiModel)`
- `Structure getBiologicalAssembly(String pdbId)`
- `Structure getBiologicalAssembly(String pdbId, int biolAssemblyNr, boolean multiModel)`
- `Structure getBiologicalAssembly(String pdbId, int biolAssemblyNr)`
- `List<Structure> getBiologicalAssemblies(String pdbId, boolean multiModel)`
- `List<Structure> getBiologicalAssemblies(String pdbId)`

### StructureTools

**Package:** `org.biojava.nbio.structure`  
**Type:** class


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `Logger` | logger |
| public | `String` | CA_ATOM_NAME |
| public | `String` | N_ATOM_NAME |
| public | `String` | C_ATOM_NAME |
| public | `String` | O_ATOM_NAME |
| public | `String` | CB_ATOM_NAME |
| public | `String` | C1_ATOM_NAME |
| public | `String` | C2_ATOM_NAME |
| public | `String` | C3_ATOM_NAME |
| public | `String` | C4_ATOM_NAME |

**Methods:**

- `int getNrAtoms(Structure s)`
- `int getNrGroups(Structure s)`
- `Atom[] getAtomArray(Structure s, String[] atomNames)`
- `Atom[] getAllAtomArray(Structure s)`
- `Atom[] getAllAtomArray(Structure s, int model)`
- `Atom[] getAllAtomArray(Chain c)`
- `List<Group> getUnalignedGroups(Atom[] ca)`
- `List<Group> getLigandsByProximity(Collection<Group> target, Atom[] query, double cutoff)`
- `Chain addGroupToStructure(Structure s, Group g, int model, Chain chainGuess, boolean clone)`
- `void addGroupsToStructure(Structure s, Collection<Group> groups, int model, boolean clone)`

### StructureImpl

**Package:** `org.biojava.nbio.structure`  
**Type:** class

**Implements:** `Structure`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `long` | serialVersionUID |
| private | `Logger` | logger |
| private | `PdbId` | pdbId |
| private | `List<Model>` | models |
| private | `List<EntityInfo>` | entityInfos |
| private | `List<DBRef>` | dbrefs |
| private | `List<Bond>` | ssbonds |
| private | `List<Site>` | sites |
| private | `String` | name |
| private | `StructureIdentifier` | structureIdentifier |

**Methods:**

- `Structure clone()`
- `Group findGroup(String chainName, String pdbResnum, int modelIdx)`
- `Group findGroup(String chainName, String pdbResnum)`
- `void setName(String nam)`
- `String getName()`
- `StructureIdentifier getStructureIdentifier()`
- `void setStructureIdentifier(StructureIdentifier structureIdentifier)`
- `void addChain(Chain chain)`
- `void addChain(Chain chain, int modelIdx)`
- `Chain getChainByIndex(int number)`

### SeqMisMatch

**Package:** `org.biojava.nbio.structure`  
**Type:** interface


### AminoAcid

**Package:** `org.biojava.nbio.structure`  
**Type:** interface

**Extends:** `Group`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| public | `String` | ATOMRECORD |
| public | `String` | SEQRESRECORD |

### Class Diagram

![Class Diagram](../A6_uml/biojava-structure_class_diagram.puml)

---

## Method Logic Flows

### StructureIO.getStructure()

**Execution Steps:**

1. `checkInitAtomCache();`
2. `return cache.getStructure(name);`

**External Calls:**

- `cache.getStructure()`

**Exceptions:** `IOException`, `StructureException`

### StructureIO.checkInitAtomCache()

**Execution Steps:**

1. `if (cache == null) {`
2. `cache = new AtomCache();`

**Conditional Logic:**

- **Condition:** `cache == null`

**Exceptions:** `IOException`, `StructureException`

### StructureIO.setAtomCache()

**Execution Steps:**

1. `cache = c;`

**Exceptions:** `IOException`, `StructureException`

### StructureTools.getNrAtoms()

**Execution Steps:**

1. `int nrAtoms = 0;`
2. `Iterator<Group> iter = new GroupIterator(s);`
3. `while (iter.hasNext()) {`
4. `Group g = iter.next();`
5. `nrAtoms += g.size();`
6. `return nrAtoms;`

**Loops:**

- **Type:** while

**External Calls:**

- `iter.hasNext()`
- `iter.next()`

**Exceptions:** `StructureException`

### StructureTools.getNrGroups()

**Execution Steps:**

1. `int nrGroups = 0;`
2. `List<Chain> chains = s.getChains(0);`
3. `for (Chain c : chains) {`
4. `nrGroups += c.getAtomLength();`
5. `return nrGroups;`

**Loops:**

- **Type:** for
- **Type:** foreach

**External Calls:**

- `s.getChains()`
- `c.getAtomLength()`

**Exceptions:** `StructureException`

### Sequence Diagram

![Sequence Diagram](../A6_uml/biojava-structure_sequence_diagram.puml)

---
