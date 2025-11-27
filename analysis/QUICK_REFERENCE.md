# BioJava Analysis — Quick Reference Guide

**For:** Developers, Architects, and Technical Leads
**Purpose:** Fast navigation and lookup for the BioJava code analysis

---

## 📁 Where to Find Things

### 🎯 I want to...

#### **Understand the overall project structure**
→ Start here: `/analysis/A8_documentation/README.md`
→ Statistics: `/analysis/STATISTICS_DASHBOARD.md`

#### **See module dependencies**
→ Visualization: `/analysis/dependency_graph.puml`
→ JSON data: `/analysis/A2_modules/project_summary.json`

#### **Find a specific class**
→ Search in: `/analysis/A3_classes/*.json`
→ Example: `grep -r "SequenceTools" analysis/A3_classes/`

#### **Understand how a method works**
→ Look in: `/analysis/A4_methods/*.json`
→ Find: Class name + method name

#### **See UML diagrams**
→ Class diagrams: `/analysis/A6_uml/*_class_diagram.puml`
→ Sequence diagrams: `/analysis/A6_uml/*_sequence_diagram.puml`

#### **Understand a business flow**
→ Flows: `/analysis/A7_business_flows/*.json`
→ Activity diagrams: `/analysis/A7_business_flows/*_activity.puml`

#### **Read comprehensive docs for a module**
→ Module docs: `/analysis/A8_documentation/<module>_documentation.md`

---

## 🗂️ File Naming Conventions

### Module Maps (A2)
```
<module-name>_module_map.json
Example: biojava-core_module_map.json
```

### Class Structures (A3)
```
<module-name>_classes.json
Example: biojava-structure_classes.json
```

### Method Flows (A4)
```
<module-name>_methods.json
Example: biojava-alignment_methods.json
```

### Call Graphs (A5)
```
<module-name>_callgraphs.json
Example: biojava-genome_callgraphs.json
```

### UML Diagrams (A6)
```
<module-name>_class_diagram.puml
<module-name>_sequence_diagram.puml
Example: biojava-core_class_diagram.puml
```

### Business Flows (A7)
```
<module-name>_business_flows.json
<module-name>_<ClassName>_activity.puml
Example: biojava-ws_business_flows.json
```

### Documentation (A8)
```
<module-name>_documentation.md
Example: biojava-ontology_documentation.md
```

---

## 🔍 Common Queries

### "How many classes are in module X?"

```bash
cat analysis/A2_modules/<module>_module_map.json | grep "total_classes"
```

**Example:**
```bash
cat analysis/A2_modules/biojava-core_module_map.json | grep "total_classes"
# Output: "total_classes": 189
```

### "What methods does class X have?"

```bash
grep -A 20 '"class_name": "ClassName"' analysis/A3_classes/*.json
```

**Example:**
```bash
grep -A 20 '"class_name": "SequenceTools"' analysis/A3_classes/*.json
```

### "What are the dependencies of module X?"

```bash
cat analysis/A2_modules/<module>_module_map.json | grep -A 10 "dependencies"
```

### "Which classes use Builder pattern?"

```bash
grep '"name":.*Builder"' analysis/A3_classes/*.json
```

### "Show me all parsers in the project"

```bash
grep '"class_name":.*Parser"' analysis/A3_classes/*.json
```

---

## 📊 JSON Structure Reference

### Module Map (A2)
```json
{
  "module": "module-name",
  "packages": ["pkg1", "pkg2"],
  "total_classes": 100,
  "classes": [
    {
      "name": "ClassName",
      "path": "relative/path.java",
      "type": "class|interface|enum|abstract",
      "package": "org.example.pkg"
    }
  ],
  "dependencies": {
    "external": ["org.slf4j", "junit"],
    "internal": ["org.biojava.other"]
  }
}
```

### Class Structure (A3)
```json
{
  "class_name": "ClassName",
  "package": "org.example",
  "type": "class|interface|enum|abstract",
  "extends": "ParentClass",
  "implements": ["Interface1"],
  "fields": [
    {
      "name": "fieldName",
      "type": "String",
      "visibility": "private|public|protected"
    }
  ],
  "methods": [
    {
      "name": "methodName",
      "params": ["String arg1"],
      "return_type": "void",
      "visibility": "public"
    }
  ],
  "internal_references": ["OtherClass"],
  "external_references": ["@Annotation"]
}
```

### Method Flow (A4)
```json
{
  "class": "ClassName",
  "method": "methodName",
  "steps": ["step1", "step2"],
  "branches": [
    {
      "condition": "if (x > 0)",
      "true_path": ["action1"],
      "false_path": ["action2"]
    }
  ],
  "loops": [
    {
      "type": "for|while|foreach",
      "declaration": "loop declaration"
    }
  ],
  "exceptions": ["IOException"],
  "external_calls": ["obj.method()"]
}
```

### Call Graph (A5)
```json
{
  "class": "ClassName",
  "method": "methodName",
  "calls": [
    {
      "from": "ClassName.methodName",
      "to": "OtherClass.otherMethod"
    }
  ],
  "depth": 1
}
```

### Business Flow (A7)
```json
{
  "feature": "FeatureName",
  "module": "module-name",
  "actor": "User|System|Application",
  "summary": "Description of what this does",
  "steps": [
    "Step 1",
    "Step 2"
  ]
}
```

---

## 🛠️ Analysis Scripts Usage

### Re-run Module Analysis
```bash
python3 analysis/analyze_modules.py
```

### Re-run Class Analysis
```bash
python3 analysis/analyze_classes.py
```

### Re-run Method Analysis
```bash
python3 analysis/analyze_methods.py
```

### Build Call Graphs
```bash
python3 analysis/build_callgraphs.py
```

### Generate UML
```bash
python3 analysis/generate_uml.py
```

### Analyze Business Flows
```bash
python3 analysis/analyze_business_flows.py
```

### Assemble Documentation
```bash
python3 analysis/assemble_documentation.py
```

---

## 🎨 Viewing PlantUML Diagrams

### Online Viewer
1. Copy `.puml` file content
2. Go to: http://www.plantuml.com/plantuml/uml/
3. Paste content
4. View rendered diagram

### VS Code
1. Install extension: "PlantUML"
2. Open `.puml` file
3. Press `Alt+D` to preview

### Command Line (if PlantUML installed)
```bash
plantuml analysis/A6_uml/*.puml
```

---

## 📦 Key Modules at a Glance

| Module | Purpose | Key Classes | Dependencies |
|--------|---------|-------------|--------------|
| **biojava-core** | Foundation | DNASequence, ProteinSequence, FastaReader | None (base) |
| **biojava-structure** | 3D structures | StructureIO, Chain, Atom | core, vecmath, mmtf |
| **biojava-alignment** | Sequence alignment | Alignments, MatrixAligner | core |
| **biojava-genome** | Genomic data | GFF3Reader, FastqReader | core |
| **biojava-ontology** | Biological ontologies | GOParser, OboParser | core |
| **biojava-ws** | Web services | NCBIQBlastService | core |
| **biojava-structure-gui** | Visualization | StructureViewer, Jmol integration | structure, alignment |

---

## 🔗 Cross-Reference Guide

### From Module to Documentation
```
Module Name
  ├─ Module Map: /analysis/A2_modules/<module>_module_map.json
  ├─ Classes: /analysis/A3_classes/<module>_classes.json
  ├─ Methods: /analysis/A4_methods/<module>_methods.json (if exists)
  ├─ Call Graphs: /analysis/A5_callgraphs/<module>_callgraphs.json (if exists)
  ├─ Class Diagram: /analysis/A6_uml/<module>_class_diagram.puml
  ├─ Sequence Diagram: /analysis/A6_uml/<module>_sequence_diagram.puml (if exists)
  ├─ Business Flows: /analysis/A7_business_flows/<module>_business_flows.json (if exists)
  └─ Documentation: /analysis/A8_documentation/<module>_documentation.md
```

---

## 💡 Tips & Tricks

### Find All Classes Implementing an Interface
```bash
grep -r '"implements".*"InterfaceName"' analysis/A3_classes/
```

### Count Methods per Class
```bash
jq '.[] | {class: .class_name, methods: (.methods | length)}' \
  analysis/A3_classes/*.json
```

### Find Classes with Most Dependencies
```bash
jq '.[] | {class: .class_name, refs: (.internal_references | length)}' \
  analysis/A3_classes/*.json | sort -k2 -n
```

### List All Exceptions Used
```bash
jq '.[].exceptions[]' analysis/A4_methods/*.json | sort -u
```

---

**Last Updated:** 2025-11-27
**Maintained By:** Claude Code (Expert Java Engineer Role)
