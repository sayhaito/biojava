# biojava-ws — Technical Documentation

---

## Module Overview

**Module:** `biojava-ws`  
**Total Classes:** 19  
**Packages:** 3

### Packages

- `org.biojava.nbio.ws.alignment`
- `org.biojava.nbio.ws.alignment.qblast`
- `org.biojava.nbio.ws.hmmer`

### Dependencies

**External:**
- junit
- net.sf.json-lib
- org.apache.logging.log4j
- org.slf4j

**Internal:**
- org.biojava.biojava-core

---

## Key Classes

### RemotePairwiseAlignmentProperties

**Package:** `org.biojava.nbio.ws.alignment`  
**Type:** interface

**Extends:** `Serializable`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| public | `long` | serialVersionUID |

### RemotePairwiseAlignmentService

**Package:** `org.biojava.nbio.ws.alignment`  
**Type:** interface


### RemotePairwiseAlignmentOutputProperties

**Package:** `org.biojava.nbio.ws.alignment`  
**Type:** interface

**Extends:** `Serializable`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| public | `long` | serialVersionUID |

### BlastOutputAlignmentFormatEnum

**Package:** `org.biojava.nbio.ws.alignment.qblast`  
**Type:** enum


### BlastAlignmentParameterEnum

**Package:** `org.biojava.nbio.ws.alignment.qblast`  
**Type:** enum


### NCBIQBlastService

**Package:** `org.biojava.nbio.ws.alignment.qblast`  
**Type:** class

**Implements:** `RemotePairwiseAlignmentService`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| public | `long` | WAIT_INCREMENT |
| private | `MapToStringTransformer` | MAP_TO_STRING_TRANSFORMER |
| private | `String` | SERVICE_URL |
| private | `String` | DEFAULT_EMAIL |
| private | `String` | DEFAULT_TOOL |
| private | `URL` | serviceUrl |
| private | `String` | email |
| private | `String` | tool |

**Methods:**

- `void init(String svcUrl)`
- `String getRemoteBlastInfo()`
- `String sendAlignmentRequest(Sequence<Compound> seq, RemotePairwiseAlignmentProperties rpa)`
- `String sendAlignmentRequest(int gid, RemotePairwiseAlignmentProperties rpa)`
- `String sendAlignmentRequest(String query, RemotePairwiseAlignmentProperties alignmentProperties)`
- `boolean isReady(String id)`
- `boolean isReady(String id, long present)`
- `InputStream getAlignmentResults(String id, RemotePairwiseAlignmentOutputProperties outputProperties)`
- `void sendDeleteRequest(String id)`
- `URLConnection setQBlastServiceProperties(URLConnection conn)`

### NCBIQBlastAlignmentProperties

**Package:** `org.biojava.nbio.ws.alignment.qblast`  
**Type:** class

**Implements:** `RemotePairwiseAlignmentProperties`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `long` | serialVersionUID |

**Methods:**

- `String getAlignmentOption(String key)`
- `void setAlignementOption(String key, String val)`
- `Set<String> getAlignmentOptions()`
- `String getAlignmentOption(BlastAlignmentParameterEnum key)`
- `void setAlignmentOption(BlastAlignmentParameterEnum key, String val)`
- `void removeAlignmentOption(BlastAlignmentParameterEnum key)`
- `BlastProgramEnum getBlastProgram()`
- `void setBlastProgram(BlastProgramEnum program)`
- `String getBlastDatabase()`
- `void setBlastDatabase(String database)`

### HmmerScan

**Package:** `org.biojava.nbio.ws.hmmer`  
**Type:** interface


### Class Diagram

![Class Diagram](../A6_uml/biojava-ws_class_diagram.puml)

---
