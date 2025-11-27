# biojava-ontology — Technical Documentation

---

## Module Overview

**Module:** `biojava-ontology`  
**Total Classes:** 34  
**Packages:** 4

### Packages

- `org.biojava.nbio.ontology`
- `org.biojava.nbio.ontology.io`
- `org.biojava.nbio.ontology.obo`
- `org.biojava.nbio.ontology.utils`

### Dependencies

**External:**
- junit
- org.apache.logging.log4j
- org.slf4j

---

## Business Process Flows

### Term

**Actor:** User  
**Summary:** User uses Term to perform operations

**Steps:**
1. Execute addSynonym
2. Execute removeSynonym
3. Retrieve Synonyms
4. Retrieve Name
5. Set Annotation
6. Set Synonyms
7. Retrieve Description
8. Retrieve Ontology

![Activity Diagram](../A7_business_flows/biojava-ontology_Term_activity.puml)

### RemoteTerm

**Actor:** User  
**Summary:** User uses RemoteTerm to perform operations

**Steps:**
1. Execute addSynonym
2. Execute removeSynonym
3. Retrieve Synonyms
4. Retrieve Name
5. Retrieve Description
6. Retrieve Ontology
7. Retrieve RemoteTerm
8. Execute toString

![Activity Diagram](../A7_business_flows/biojava-ontology_RemoteTerm_activity.puml)

---

## Key Classes

### Term

**Package:** `org.biojava.nbio.ontology`  
**Type:** interface

**Extends:** `Annotatable`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `long` | serialVersionUID |
| private | `String` | name |
| private | `Ontology` | ontology |
| private | `Annotation` | annotation |
| private | `Set<Object>` | synonyms |

**Methods:**

- `void addSynonym(Object synonym)`
- `void removeSynonym(Object synonym)`
- `Object[] getSynonyms()`
- `String getName()`
- `void setAnnotation(Annotation annotation)`
- `void setSynonyms(Set<Object> synonyms)`
- `String getDescription()`
- `Ontology getOntology()`
- `String toString()`
- `Annotation getAnnotation()`

### Variable

**Package:** `org.biojava.nbio.ontology`  
**Type:** interface

**Extends:** `Term`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `long` | serialVersionUID |

### RemoteTerm

**Package:** `org.biojava.nbio.ontology`  
**Type:** interface

**Extends:** `Term`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `long` | serialVersionUID |
| private | `Ontology` | ontology |
| private | `Term` | remoteTerm |
| private | `String` | name |
| private | `Set` | synonyms |

**Methods:**

- `void addSynonym(Object synonym)`
- `void removeSynonym(Object synonym)`
- `Object[] getSynonyms()`
- `String getName()`
- `String getDescription()`
- `Ontology getOntology()`
- `Term getRemoteTerm()`
- `String toString()`
- `Annotation getAnnotation()`

### OntologyOps

**Package:** `org.biojava.nbio.ontology`  
**Type:** interface


### OntologyFactory

**Package:** `org.biojava.nbio.ontology`  
**Type:** interface


### Triple

**Package:** `org.biojava.nbio.ontology`  
**Type:** interface

**Extends:** `Term`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `long` | serialVersionUID |
| private | `Term` | subject |
| private | `Term` | object |
| private | `Term` | predicate |
| private | `String` | name |
| private | `String` | description |
| private | `Set<Object>` | synonyms |

**Methods:**

- `void addSynonym(Object synonym)`
- `void removeSynonym(Object synonym)`
- `Object[] getSynonyms()`
- `String getName()`
- `String getDescription()`
- `void setDescription(String desc)`
- `Ontology getOntology()`
- `Term getSubject()`
- `Term getObject()`
- `Term getPredicate()`

### OntologyTerm

**Package:** `org.biojava.nbio.ontology`  
**Type:** interface

**Extends:** `Term`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `long` | serialVersionUID |
| private | `Ontology` | ontology |
| private | `Ontology` | target |
| private | `Set` | synonyms |

**Methods:**

- `void addSynonym(Object synonym)`
- `void removeSynonym(Object synonym)`
- `Object[] getSynonyms()`
- `String getName()`
- `String getDescription()`
- `void setDescription(String description)`
- `Ontology getOntology()`
- `Ontology getTargetOntology()`
- `String toString()`
- `Annotation getAnnotation()`

### Ontology

**Package:** `org.biojava.nbio.ontology`  
**Type:** interface


**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `long` | serialVersionUID |
| private | `Set<Triple>` | triples |
| private | `Set<Term>` | localRemoteTerms |
| private | `String` | name |
| private | `String` | description |
| private | `OntologyOps` | ops |
| private | `long` | serialVersionUID |

**Methods:**

- `Set<Term> getRemoteTerms()`
- `String getName()`
- `String getDescription()`
- `void setDescription(String description)`
- `Set<Term> getTerms()`
- `Term getTerm(String name)`
- `Set<Triple> getTriples(Term subject, Term object, Term predicate)`
- `Set<Triple> filterTriples(Set<Triple> base, Term subject, Term object, Term predicate)`
- `void addTerm(Term t)`
- `Term createTerm(String name)`

### Class Diagram

![Class Diagram](../A6_uml/biojava-ontology_class_diagram.puml)

---

## Method Logic Flows

### Term.getSynonyms()

**Execution Steps:**

1. `return this.synonyms.toArray();`

**External Calls:**

- `synonyms.toArray()`

### Term.getName()

**Execution Steps:**

1. `return name;`

### Term.setAnnotation()

**Execution Steps:**

1. `this.annotation = annotation;`

### RemoteTerm.getSynonyms()

**Execution Steps:**

1. `return this.synonyms.toArray();`

**External Calls:**

- `synonyms.toArray()`

### RemoteTerm.getName()

**Execution Steps:**

1. `return getOntology().getName() + ":" + remoteTerm.getName();`

**External Calls:**

- `remoteTerm.getName()`

### Sequence Diagram

![Sequence Diagram](../A6_uml/biojava-ontology_sequence_diagram.puml)

---
