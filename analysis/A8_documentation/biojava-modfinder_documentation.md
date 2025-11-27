# biojava-modfinder — Technical Documentation

---

## Module Overview

**Module:** `biojava-modfinder`  
**Total Classes:** 23  
**Packages:** 4

### Packages

- `org.biojava.nbio.phosphosite`
- `org.biojava.nbio.protmod`
- `org.biojava.nbio.protmod.io`
- `org.biojava.nbio.protmod.structure`

### Dependencies

**External:**
- jakarta.xml.bind
- junit
- org.apache.logging.log4j
- org.glassfish.jaxb
- org.slf4j

**Internal:**
- org.biojava.biojava-structure

---

## Business Process Flows

### ProteinModificationImpl

**Actor:** User  
**Summary:** User uses ProteinModificationImpl to perform operations

**Steps:**
1. Retrieve Id
2. Retrieve PdbccId
3. Retrieve PdbccName
4. Retrieve ResidId
5. Retrieve ResidName
6. Retrieve PsimodId
7. Retrieve PsimodName
8. Retrieve SystematicName

![Activity Diagram](../A7_business_flows/biojava-modfinder_ProteinModificationImpl_activity.puml)

### ProteinModificationRegistry

**Actor:** User  
**Summary:** User uses ProteinModificationRegistry to perform operations

**Steps:**
1. Execute registerCommonProteinModifications
2. Execute init
3. Execute init
4. Execute register
5. Execute unregister
6. Retrieve ById
7. Retrieve ByResidId
8. Retrieve ByPsimodId

![Activity Diagram](../A7_business_flows/biojava-modfinder_ProteinModificationRegistry_activity.puml)

### StructureAtomXMLConverter

**Actor:** User  
**Summary:** User uses StructureAtomXMLConverter to processes molecular structures

**Steps:**
1. Execute toXML
2. Execute toXML
3. Execute fromXML
4. Retrieve Attribute

![Activity Diagram](../A7_business_flows/biojava-modfinder_StructureAtomXMLConverter_activity.puml)

---

## Key Classes

### ProteinModification

**Package:** `org.biojava.nbio.protmod`  
**Type:** interface


### ModificationCondition

**Package:** `org.biojava.nbio.protmod`  
**Type:** interface


### ProteinModificationImpl

**Package:** `org.biojava.nbio.protmod`  
**Type:** class

**Implements:** `ProteinModification`, `Comparable<ProteinModification>`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `String` | id |
| private | `ModificationCondition` | condition |
| private | `ModificationCategory` | category |
| private | `ModificationOccurrenceType` | occurrenceType |
| private | `String` | pdbccId |
| private | `String` | pdbccName |
| private | `String` | residId |
| private | `String` | residName |
| private | `String` | psimodId |
| private | `String` | psimodName |

**Methods:**

- `String getId()`
- `String getPdbccId()`
- `String getPdbccName()`
- `String getResidId()`
- `String getResidName()`
- `String getPsimodId()`
- `String getPsimodName()`
- `String getSystematicName()`
- `String getDescription()`
- `Set<String> getKeywords()`

### ProteinModificationRegistry

**Package:** `org.biojava.nbio.protmod`  
**Type:** class


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `Logger` | logger |
| private | `Set<ProteinModification>` | registry |
| private | `String` | DIR_XML_PTM_LIST |

**Methods:**

- `void registerCommonProteinModifications(InputStream inStream)`
- `void init()`
- `void init(InputStream inStream)`
- `void register(final ProteinModification modification)`
- `void unregister(ProteinModification modification)`
- `ProteinModification getById(final String id)`
- `Set<ProteinModification> getByResidId(final String residId)`
- `Set<ProteinModification> getByPsimodId(final String psimodId)`
- `Set<ProteinModification> getByPdbccId(final String pdbccId)`
- `Set<ProteinModification> getByKeyword(final String keyword)`

### StructureAtomXMLConverter

**Package:** `org.biojava.nbio.protmod.io`  
**Type:** class


**Methods:**

- `String toXML(StructureAtom atom)`
- `void toXML(StructureAtom atom, PrettyXMLWriter xml)`
- `StructureAtom fromXML(Node structureAtomElement)`
- `String getAttribute(Node node, String attr)`

### StructureGroupXMLConverter

**Package:** `org.biojava.nbio.protmod.io`  
**Type:** class


**Methods:**

- `void toXML(StructureGroup group, PrettyXMLWriter xml)`
- `StructureGroup fromXML(Node n)`
- `String getAttribute(Node node, String attr)`

### ProteinModificationXmlReader

**Package:** `org.biojava.nbio.protmod.io`  
**Type:** class


**Methods:**

- `void registerProteinModificationFromXml(InputStream isXml)`

### StructureUtil

**Package:** `org.biojava.nbio.protmod.structure`  
**Type:** class


**Methods:**

- `StructureGroup getStructureGroup(Group group, boolean isAminoAcid)`
- `StructureAtom getStructureAtom(Atom atom, boolean isParentAminoAcid)`
- `double getAtomDistance(Atom atom1, Atom atom2)`
- `boolean hasMetalBond(Atom a1, Atom a2, MetalBondDistance definition)`
- `MetalBondDistance getMetalDistanceCutoff(String name1, String name2)`
- `List<String> getAtomNames(Group group)`
- `List<Group> getAminoAcids(Chain chain)`

### Class Diagram

![Class Diagram](../A6_uml/biojava-modfinder_class_diagram.puml)

---

## Method Logic Flows

### ProteinModificationImpl.getId()

**Execution Steps:**

1. `return id;`

### ProteinModificationImpl.getPdbccId()

**Execution Steps:**

1. `return pdbccId;`

### ProteinModificationImpl.getPdbccName()

**Execution Steps:**

1. `return pdbccName;`

### ProteinModificationRegistry.init()

**Execution Steps:**

1. `lazyInit();`

### ProteinModificationRegistry.init()

**Execution Steps:**

1. `lazyInit();`

### Sequence Diagram

![Sequence Diagram](../A6_uml/biojava-modfinder_sequence_diagram.puml)

---
