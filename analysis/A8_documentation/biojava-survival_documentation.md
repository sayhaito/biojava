# biojava-survival — Technical Documentation

---

## Module Overview

**Module:** `biojava-survival`  
**Total Classes:** 46  
**Packages:** 7

### Packages

- `org.biojava.nbio.survival.cox`
- `org.biojava.nbio.survival.cox.comparators`
- `org.biojava.nbio.survival.cox.matrix`
- `org.biojava.nbio.survival.cox.stats`
- `org.biojava.nbio.survival.data`
- `org.biojava.nbio.survival.kaplanmeier.figure`
- `org.biojava.nbio.survival.kaplanmeier.metadata`

### Dependencies

**External:**
- junit
- org.apache.commons
- org.apache.logging.log4j
- org.slf4j

---

## Business Process Flows

### CompactCharSequence

**Actor:** User  
**Summary:** User uses CompactCharSequence to manipulates biological sequences

**Steps:**
1. Execute charAt
2. Execute length
3. Execute subSequence
4. Execute toString

![Activity Diagram](../A7_business_flows/biojava-survival_CompactCharSequence_activity.puml)

---

## Key Classes

### ChangeValue

**Package:** `org.biojava.nbio.survival.data`  
**Type:** interface


### CompactCharSequence

**Package:** `org.biojava.nbio.survival.data`  
**Type:** class

**Implements:** `CharSequence`, `Serializable`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| static | `long` | serialVersionUID |
| private | `String` | ENCODING |
| private | `int` | offset |
| private | `int` | end |
| private | `byte[]` | data |
| private | `boolean` | nullstring |

**Methods:**

- `char charAt(int index)`
- `int length()`
- `CharSequence subSequence(int start, int end)`
- `String toString()`

### DiscreteQuantizerInterface

**Package:** `org.biojava.nbio.survival.kaplanmeier.metadata`  
**Type:** interface


### CensorStatusSelect

**Package:** `org.biojava.nbio.survival.kaplanmeier.figure`  
**Type:** interface


### CoxComparatorInterface

**Package:** `org.biojava.nbio.survival.cox.comparators`  
**Type:** interface

**Extends:** `Comparator<CoxVariables>`  

### Class Diagram

![Class Diagram](../A6_uml/biojava-survival_class_diagram.puml)

---
