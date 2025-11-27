# biojava-structure-gui — Technical Documentation

---

## Module Overview

**Module:** `biojava-structure-gui`  
**Total Classes:** 113  
**Packages:** 11

### Packages

- `org.biojava.nbio.structure.align.gui`
- `org.biojava.nbio.structure.align.gui.aligpanel`
- `org.biojava.nbio.structure.align.gui.autosuggest`
- `org.biojava.nbio.structure.align.gui.jmol`
- `org.biojava.nbio.structure.align.webstart`
- `org.biojava.nbio.structure.gui`
- `org.biojava.nbio.structure.gui.events`
- `org.biojava.nbio.structure.gui.util`
- `org.biojava.nbio.structure.gui.util.color`
- `org.biojava.nbio.structure.symmetry.gui`
- `org.biojava.nbio.structure.symmetry.jmolScript`

### Dependencies

**External:**
- junit
- net.sourceforge.jmol
- org.apache.logging.log4j
- org.biojava
- org.slf4j

**Internal:**
- org.biojava.biojava-core
- org.biojava.biojava-structure

---

## Business Process Flows

### SequenceDisplay

**Actor:** User  
**Summary:** User uses SequenceDisplay to manipulates biological sequences

**Steps:**
1. Execute main
2. Execute windowClosing
3. Execute clearListeners
4. Execute addAlignmentPositionListener
5. Retrieve StructurePairAligner
6. Set StructurePairAligner
7. Retrieve Idx1
8. Set Idx1

![Activity Diagram](../A7_business_flows/biojava-structure-gui_SequenceDisplay_activity.puml)

### CoordManager

**Actor:** User  
**Summary:** User uses CoordManager to perform operations

**Steps:**
1. Set Length
2. Set Scale
3. Retrieve SeqPos
4. Retrieve PanelPos

![Activity Diagram](../A7_business_flows/biojava-structure-gui_CoordManager_activity.puml)

---

## Key Classes

### Selection

**Package:** `org.biojava.nbio.structure.gui`  
**Type:** interface


### SequenceDisplay

**Package:** `org.biojava.nbio.structure.gui`  
**Type:** class

**Extends:** `JPanel implements ChangeListener`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `long` | serialVersionUID |
| public | `int` | MAX_SCALE |

**Methods:**

- `void main(String[] args)`
- `void windowClosing(WindowEvent e)`
- `void clearListeners()`
- `void addAlignmentPositionListener(AlignmentPositionListener li)`
- `StructurePairAligner getStructurePairAligner()`
- `void setStructurePairAligner(StructurePairAligner structurePairAligner)`
- `int[] getIdx1()`
- `void setIdx1(int[] idx)`
- `int[] getIdx2()`
- `void setIdx2(int[] idx)`

### StructureViewer

**Package:** `org.biojava.nbio.structure.gui`  
**Type:** interface


### CoordManager

**Package:** `org.biojava.nbio.structure.gui.util`  
**Type:** class


**Methods:**

- `void setLength(int length)`
- `void setScale(float scale)`
- `int getSeqPos(int panelPos)`
- `int getPanelPos(int seqPos)`

### StructurePairSelector

**Package:** `org.biojava.nbio.structure.gui.util`  
**Type:** interface


### SequenceMouseListener

**Package:** `org.biojava.nbio.structure.gui.util`  
**Type:** class

**Implements:** `MouseListener`, `MouseMotionListener`  

**Methods:**

- `void clearListeners()`
- `void addAlignmentPositionListener(AlignmentPositionListener li)`
- `void mousePressed(MouseEvent event)`
- `int getSeqPos(MouseEvent e)`
- `void setChain(Chain c)`
- `void setSelectionStart(int start)`
- `void setSelectionEnd(int end)`
- `void mouseDragged(MouseEvent e)`
- `void mouseMoved(MouseEvent e)`
- `void mouseClicked(MouseEvent arg0)`

### SequenceScalePanel

**Package:** `org.biojava.nbio.structure.gui.util`  
**Type:** class

**Extends:** `JPanel`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| static | `long` | serialVersionUID |
| public | `int` | DEFAULT_X_START |
| public | `int` | DEFAULT_X_RIGHT_BORDER |
| public | `int` | DEFAULT_Y_START |
| public | `int` | DEFAULT_Y_STEP |
| public | `int` | DEFAULT_Y_HEIGHT |
| public | `int` | DEFAULT_Y_BOTTOM |
| public | `int` | LINE_HEIGHT |
| public | `int` | MINIMUM_HEIGHT |
| public | `Color` | SEQUENCE_COLOR |

**Methods:**

- `void setPrefSize()`
- `void setAligMap(List<AlignedPosition> apos)`
- `Chain getChain()`
- `void setScale(float scale)`
- `void setPaintDefaults(Graphics2D g2D)`
- `void paintComponent(Graphics g)`
- `int drawScale(Graphics2D g2D, int y)`
- `void drawIdx(Graphics2D g2D, int y)`
- `int drawSequence(Graphics2D g2D, int y)`

### AlternativeAlignmentFrame

**Package:** `org.biojava.nbio.structure.gui.util`  
**Type:** class

**Extends:** `JFrame`  

**Fields:**

| Visibility | Type | Name |
|------------|------|------|
| private | `long` | serialVersionUID |
| private | `Logger` | logger |
| private | `String[]` | columnNames |

**Methods:**

- `void setStructurePairAligner(StructurePairAligner aligner)`
- `void setAlternativeAlignments(AlternativeAlignment[] aligs)`
- `Object[][] getDataFromAligs(AlternativeAlignment[] aligs)`
- `void showDistanceMatrix(int position)`
- `void windowClosing(WindowEvent e)`
- `void showAlternative(int position)`
- `void windowClosing(WindowEvent e)`
- `String[] createRasmolScripts(AlternativeAlignment alig)`
- `void mouseClicked(MouseEvent arg0)`
- `void mousePressed(MouseEvent arg0)`

### Class Diagram

![Class Diagram](../A6_uml/biojava-structure-gui_class_diagram.puml)

---

## Method Logic Flows

### SequenceDisplay.getStructurePairAligner()

**Execution Steps:**

1. `return structurePairAligner;`

### SequenceDisplay.setStructurePairAligner()

**Execution Steps:**

1. `this.structurePairAligner = structurePairAligner;`

### SequenceDisplay.getIdx1()

**Execution Steps:**

1. `return idx1;`

### CoordManager.setLength()

**Execution Steps:**

1. `chainLength = length;`

### CoordManager.setScale()

**Execution Steps:**

1. `this.scale = scale;`

### Sequence Diagram

![Sequence Diagram](../A6_uml/biojava-structure-gui_sequence_diagram.puml)

---
